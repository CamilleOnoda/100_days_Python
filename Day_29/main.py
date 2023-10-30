from cgitb import text
from tkinter import *
from tkinter import messagebox


# Save data in a file
def save():
    global add_button

    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    validate = messagebox.askokcancel(title=website, message=f"Emai: {email} \n Password: {password} \n Do you want to save?")

    if not website or not email or not password:
        error_label.config(text="Please fill in all required information", fg="red")
    elif validate:
        with open("data.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

        messagebox.showinfo(title=None, message="Data saved!")


# User interface
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)
canvas = Canvas(width=200,height=200)
img = PhotoImage(file="logo.png")
window.iconphoto(False, img)
canvas.create_image(130, 100, image=img)
canvas.grid(column=1, row=0)


# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


# Entries
website_entry = Entry(width=50)
website_entry.grid(column=1,row=1, columnspan=2)
website_entry.focus()
email_username_entry = Entry(width=50)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "info@camilleonoda.com")
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)


# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, padx=(0,10))
add_button = Button(text="Add", command=save)
add_button.grid(column=2, row=4, ipadx=5, padx=(0,80))


# Error label
error_label = Label(text="", fg="red")
error_label.grid(column=1, row=5)

window.mainloop()
