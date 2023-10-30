from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import string


# -----------------------User interface-----------------------------------------
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)
canvas = Canvas(width=200,height=200)
img = PhotoImage(file="logo.png")
window.iconphoto(False, img)
canvas.create_image(130, 100, image=img)
canvas.grid(column=1, row=0)


# -----------------------Data processing-----------------------------------------
def save():
    """Save data into a txt file."""
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if not website or not email or not password:
        error_label.config(text="Please fill in all required information", fg="red")
    else:
        lines = read_data()

        if website_exists(website, lines):
            update_data(website, email, password, lines)
        else:
            validate = messagebox.askokcancel(title=website, message=f"Website: {website} \n"
                                        f" Emai: {email} \n Password: {password} \n Do you want to save?")
            if validate:
                with open("data.txt", "a") as file:
                    file.write(f"{website} | {email} | {password}\n")
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
                messagebox.showinfo(title=None, message="Data saved!")
                error_label.config(text="")


def read_data():
    """Read the txt file."""
    with open("data.txt", "r") as file:
        lines = file.readlines()
    return lines


def website_exists(website, lines):
    """Verify if the data entered already exists."""
    for x, line in enumerate(lines):
        data = line.strip().split(" | ")
        if data[0] == website:
            return x
    return None        


def update_data(website, email, password, lines):
    """If the data exists, ask the user if they want to update the information."""
    update = messagebox.askyesno(title=website, message=f"The website '{website}'"
                                            " already exists in the data file."
                                            " Do you want to update its information?")
    if update:
        index = website_exists(website, lines)
        if index is not None:
            lines[index] = f"{website} | {email} | {password}\n"
            with open("data.txt", "w") as file:
                file.writelines(lines)
            messagebox.showinfo(title=None, message="Data updated!")


# -----------------------Generate random password-------------------------------
# -----------------------Get the length of the password-------------------------
password_len = IntVar()
length = Spinbox(from_= 6, to_ = 15, textvariable=password_len)
length.grid(column=2, row=4)

generated_password = StringVar()
combination = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]
def randPassGen():
    password = ""
    for char in range(password_len.get()):
        char = random.choice(combination)
        password = password + random.choice(char)
    generated_password.set(password)


# -----------------------Copy to clipboard--------------------------------------
def copy_password():
    pyperclip.copy(generated_password.get())
    messagebox.showinfo(title=None, message="Password copied to clipboard.")


# -----------------------Labels-------------------------------------------------
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Random Password:")
password_label.grid(column=0, row=3)
password_length_label = Label(text="Password length (6-15)")
password_length_label.grid(column=2, row=3)


# -----------------------Entries------------------------------------------------
website_entry = Entry(width=50)
website_entry.grid(column=1,row=1, columnspan=2)
website_entry.focus()
email_username_entry = Entry(width=50)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "info@camilleonoda.com")
password_entry = Entry(textvariable=generated_password, width=28)
password_entry.grid(column=1, row=3)


# -----------------------Buttons------------------------------------------------
generate_password_button = Button(text="Generate Password", command=randPassGen)
generate_password_button.grid(column=2, row=5, padx=(0,10))
add_button = Button(text="Add", command=save)
add_button.grid(column=2, row=6, ipadx=5, padx=(0,80))
clipboard = Button(text="Copy to clipboard", command=copy_password)
clipboard.grid(column=1, row=4, padx=(0,62))


# -----------------------Error label--------------------------------------------
error_label = Label(text="", fg="red")
error_label.grid(column=1, row=5)


window.mainloop()
