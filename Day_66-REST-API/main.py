from flask import Flask, render_template, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException, NotFound
import random


app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def as_dict(self):
        return {"id": self.id,
                "name": self.name,
                "map_url": self.map_url,
                "img_url": self.img_url,
                "location": self.location,
                "seats": self.seats,
                "has_toilet": self.has_toilet,
                "has_wifi": self.has_wifi,
                "has_sockets": self.has_sockets,
                "can_take_calls": self.can_take_calls,
                "coffee_price": self.coffee_price,
                }


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

# HTTP GET a random cafe
@app.route("/random", methods=['GET'])
def get_random_cafe():
    all_cafes = list(db.session.execute(db.select(Cafe)).scalars())
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe={"id":random_cafe.id,
                         "name":random_cafe.name,
                         "map_url":random_cafe.map_url,
                         "img_url":random_cafe.img_url,
                         "location":random_cafe.location,
                         "seats":random_cafe.seats,
                         "has_toilet":random_cafe.has_toilet,
                         "has_wifi":random_cafe.has_wifi,
                         "has_sockets":random_cafe.has_sockets,
                         "can_take_calls":random_cafe.can_take_calls,
                         "coffee_price":random_cafe.coffee_price,
                         })

# HTTP GET all cafes
@app.route("/all", methods=['GET'])
def get_cafe():
    all_cafes = list(db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars())
    return jsonify(cafes=[cafe.as_dict() for cafe in all_cafes])

# HTTP GET Find a cafe
@app.route("/search", methods=['GET'])
def find_cafe():
    query_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.as_dict() for cafe in all_cafes])
    else:
        abort(404, description=f"No cafes found for location: {query_location}")


# HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def add_new_cafe():
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe_name = request.form.get("name")
        existing_cafe = Cafe.query.filter_by(name=cafe_name).first()
        if existing_cafe:
            abort(409, description=f"A cafe with the name '{cafe_name}' already exists.")          
        new_cafe=Cafe(
            name=cafe_name,
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            seats=request.form.get("seats"),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            has_sockets=bool(request.form.get("sockets")),
            can_take_calls=bool(request.form.get("calls")),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})
    else:
        abort(403, description="Sorry, that's not allowed. Make sure you have the correct api-key."), 403

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Sucessfully updated the price."}), 200
    else:
        abort(404, description=f"Sorry, a cafe with id: {cafe_id}, was not found in the database")

# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        try:
            cafe = db.get_or_404(Cafe, cafe_id)
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted this cafe from the database."}), 200  
        except NotFound:
            abort(404, description="Sorry, a cafe with that id was not found in the database."), 404
    else:
        abort(403, description="Sorry, that's not allowed. Make sure you have the correct api-key."), 403

# Error handling
@app.errorhandler(HTTPException)
def handle_exception(e):
    return jsonify({"message": e.description}), e.code


if __name__ == '__main__':
    app.run(debug=True)
