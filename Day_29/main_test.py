from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
import random
import pyperclip
import string
import os
import json


# -----------------------User interface-----------------------------------------
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)
img = PhotoImage(file="logo.png")
window.iconphoto(False, img)
canvas = Canvas(width=300,height=200)
canvas.create_image(150, 100, image=img)
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
    website = website_entry.get().lower().strip()
    email = email_username_entry.get()
    password = password_entry.get()

    if not website or not email or not password:
        error_label.config(text="Please fill in all required information", fg="red")
    else:
        encrypted_password = encrypt_data(password, encryption_key)
        data = read_data()

        if website in data:
            update(data, website, email, encrypted_password)
            clear_entries()
            error_label.config(text="")

        else:
            create(data, website, email, encrypted_password)
            clear_entries()
            error_label.config(text="")
                

def clear_entries():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def read_data():
    """Read the json file. If it doesn't exist, it creates a new JSON dict."""
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
        return data


def create(data, website, email, encrypted_password):
    """If the data doesn't exist, ask the user if they want to create a new entry."""
    create = messagebox.askokcancel(title=website, message=f"Website: {website} \n"
                                        f" Email: {email} \n Do you want to save?")
    if create:
        data[website] = {"email": email, "password": encrypted_password}
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4, default=lambda x: x.decode() if isinstance(x, bytes) else x) 
        messagebox.showinfo(title=None, message="New entry created!")  
    return data


def update(data, website, email, encrypted_password):
    """If the data exists, ask the user if they want to update the information."""
    if website in data:
        update = messagebox.askyesno(title=website, message=f"The website '{website}'"
                                            " already exists in the data file."
                                            " Do you want to update its information?")
        if update == True:
            data[website] = {"email": email, "password": encrypted_password}
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4, default=lambda x: x.decode() if isinstance(x, bytes) else x)
            messagebox.showinfo(title=None, message="Data updated!")
    return data

def search_password():
    """The user enters the name of a website and retrieves the decrypted password."""
    website = website_entry.get().lower()
    data = read_data()
    decrypted_password = get_decrypted_password(website, data)
    
    if decrypted_password:
        pyperclip.copy(decrypted_password)
        messagebox.showinfo(title=None, message=f"Password for {website} copied to clipboard.")
    else:
        messagebox.showerror(title=None, message=f"Password for {website} not found or could not be decrypted.")


def get_decrypted_password(website, data):
    """Decrypt the password using the encryption key"""
    if website in data:
        encrypted_password = data[website]["password"]
        decrypted_password = decrypt_data(encrypted_password, encryption_key)
        return decrypted_password
    
    return None


def delete_website():
    """The user can delete all data associated with a website."""
    website = website_entry.get().lower()
    data = read_data()
    delete = messagebox.askokcancel(title=website, message=f"Do you want to delete information for: {website}?")
    if delete:
        if website in data:
            del data[website]
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
            messagebox.showinfo(title=None, message=f"Information for: {website} has been deleted.")
        else:
            messagebox.showerror(title=None, message=f"Information for: {website} not found.")


# -----------------------Generate random password-------------------------------
# -----------------------Get the length of the password-------------------------
password_len = IntVar()
length = Spinbox(from_= 6, to_= 12, textvariable=password_len, width=22)
length.grid(column=0, row=5, ipady=2, columnspan=2)

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
website_label = Label(text="Website", font=('Times',12))
website_label.grid(column=0, row=1,sticky=W)
email_username_label = Label(text="Email/Username", font=('Times',12))
email_username_label.grid(column=0, row=3,sticky=W)
password_label = Label(text="Random Password", font=('Times',12))
password_label.grid(column=0, row=4,sticky=W)
password_length_label = Label(text="Password length (6 - 12)", font=('Times',12))
password_length_label.grid(column=0, row=5,sticky=W)


# -----------------------Entries------------------------------------------------
website_entry = Entry(width=50)
website_entry.grid(column=1,row=1)
website_entry.focus()
email_username_entry = Entry(width=50)
email_username_entry.grid(column=1, row=3)
email_username_entry.insert(0, "info@camilleonoda.com")
password_entry = Entry(textvariable=generated_password, width=50)
password_entry.grid(column=1, row=4)


# -----------------------Buttons------------------------------------------------
generate_password_button = Button(text="Generate a password", font=('Times',12), command=randPassGen)
generate_password_button.grid(column=1, row=6, sticky=W, padx=(24,0))
save_button = Button(text="Save", font=('Times',12), command=save)
save_button.grid(column=1, row=8, sticky=W, padx=(24,0))
clipboard = Button(text="Copy to clipboard", font=('Times',12), command=copy_password)
clipboard.grid(column=1, row=7, sticky=W, padx=(24,0))
search_button = Button(text="Search Password", width=12, font=('Times',12), command=search_password)
search_button.grid(column=2, row=2)
delete_button = Button(text="Delete Website", width=12, font=('Times',12), command=delete_website)
delete_button.grid(column=2, row=1)


# -----------------------Error label--------------------------------------------
error_label = Label(text="", fg="red")
error_label.grid(column=1, row=5)


window.mainloop()