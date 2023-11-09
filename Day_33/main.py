from tkinter import *
import requests


def get_quote():
    reponse = requests.get("https://zenquotes.io/api/today")
    reponse.raise_for_status()
    data = reponse.json()
    quote = data[0]["q"]
    canvas.itemconfig(quote_text, text=quote)
    

window = Tk()
window.title("Zen quotes...")
window.config(padx=50, pady=50)

canvas = Canvas(width=600, height=150)
background_img = PhotoImage(file="background.png")
canvas.create_image(300, 200, image=background_img)
quote_text = canvas.create_text(300, 90, text="", width=250, font=("Verdana", 12, "bold"), fill="black")
canvas.grid(row=0, column=0)

img = PhotoImage(file="grandpa.png")
grandpa_button = Button(image=img, highlightthickness=0, command=get_quote)
grandpa_button.grid(row=1, column=0)


window.mainloop()