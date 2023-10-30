from json import load
from tkinter import *
from tkinter import messagebox
from turtle import clear
from cryptography.fernet import Fernet
import random
import pyperclip
import string
import os


# -----------------------User interface-----------------------------------------
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)
canvas = Canvas(width=200,height=200)
img = PhotoImage(file="logo.png")
window.iconphoto(False, img)
canvas.create_image(130, 100, image=img)
canvas.grid(column=1, row=0)


# -----------------------Encryption key handling-----------------------------------------
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    key_file_path = "secret.key"
    if not os.path.isfile(key_file_path):
        generate_key()
    with open(key_file_path, "rb") as key_file:
        return key_file.read()


encryption_key = load_key()

# -----------------------Data processing-----------------------------------------

def save():
    """Save data into a txt file."""
    website = website_entry.get().lower()
    email = email_username_entry.get()
    password = password_entry.get()

    if not website or not email or not password:
        error_label.config(text="Please fill in all required information", fg="red")
    else:
        encrypted_password = encrypt_data(password, encryption_key)

        lines = read_data()

        if website_exists(website, lines):
            update_data(website, email, encrypted_password, lines)
        else:
            validate = messagebox.askokcancel(title=website, message=f"Website: {website} \n"
                                        f" Emai: {email} \n Password: {password} \n Do you want to save?")
            if validate:
                with open("data.txt", "a") as file:
                    file.write(f"{website} | {email} | {encrypted_password}\n")
                clear_entries()
                messagebox.showinfo(title=None, message="Data saved!")
                error_label.config(text="")


def clear_entries():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def read_data():
    """Read the txt file."""
    with open("data.txt", "r") as file:
        lines = file.readlines()
    return lines


def website_exists(website, lines):
    """Verify if the data entered already exists."""
    for x, line in enumerate(lines):
        data = line.strip().split(" | ")
        if data[0].lower() == website:
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
            clear_entries()
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


def get_decrypted_password(website):
    lines = read_data()
    for line in lines:
        data = line.strip().split(" | ")
        if data[0].lower() == website.lower():
            encrypted_password = data[2][2:-1]  # Extract the encrypted password from the line
            decrypted_password = decrypt_data(encrypted_password, encryption_key)
            return decrypted_password

    return None  # Return None if the website is not found

def search_password():
    website = website_entry.get()
    decrypted_password = get_decrypted_password(website)
    
    if decrypted_password:
        pyperclip.copy(decrypted_password)
        messagebox.showinfo(title=None, message=f"Password for {website} copied to clipboard.")
    else:
        messagebox.showerror(title=None, message=f"Password for {website} not found or could not be decrypted.")


# -----------------------Copy to clipboard--------------------------------------
def copy_password():
    pyperclip.copy(generated_password.get())
    messagebox.showinfo(title=None, message="Password copied to clipboard.")


# -----------------------Data encryption and decryption-------------------------
def encrypt_data(data, key):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data


def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data


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
search_button = Button(text="Search Password", command=search_password)
search_button.grid(column=2, row=7, padx=(0,10))


# -----------------------Error label--------------------------------------------
error_label = Label(text="", fg="red")
error_label.grid(column=1, row=5)


window.mainloop()
