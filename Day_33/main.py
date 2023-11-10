from tkinter import *
import requests


def get_quote():
    reponse = requests.get("https://zenquotes.io/api/today")
    reponse.raise_for_status()
    data = reponse.json()
    quote = data[0]["q"]
    author = data[0]["a"]
    canvas.itemconfig(quote_text, text=f"{quote}\n-{author}")
    

window = Tk()
window.title("Zen quotes...")
window.config(padx=30, pady=30)
canvas = Canvas(width=600, height=200)
background_img = PhotoImage(file="background.png")
canvas.create_image(300, 200, image=background_img)
quote_text = canvas.create_text(300, 110, text="", width=200, font=("Verdana", 10, "bold"), fill="black")
canvas.grid(row=0, column=0)

img = PhotoImage(file="grandpa3.png")
grandpa_button = Button(image=img, highlightthickness=0, command=get_quote)
grandpa_button.grid(row=1, column=0)


window.mainloop()