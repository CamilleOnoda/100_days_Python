from tkinter import *



window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)
canvas = Canvas(width=200,height=200)
img = PhotoImage(file="logo.png")
window.iconphoto(False, img)
canvas.create_image(130, 100, image=img)
canvas.grid(column=1, row=0)


website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


website_entry = Entry(width=50)
website_entry.grid(column=1,row=1, columnspan=2)
email_username_entry = Entry(width=50)
email_username_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)


generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, padx=(0,10))
add_button = Button(text="Add")
add_button.grid(column=2, row=4, ipadx=5, padx=(0,80))






window.mainloop()
