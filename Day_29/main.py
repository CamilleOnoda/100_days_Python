from tkinter import *
from tkinter import messagebox
import cryptography
from cryptography.fernet import Fernet
import random
import pyperclip
import string
import os


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.password_manager = PasswordManager(self.username)

class PasswordManager:
    def __init__(self, username):
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=30, pady=30)
        self.canvas = Canvas(width=200, height=200)
        img = PhotoImage(file="logo.png")
        self.window.iconphoto(False, img)
        self.canvas.create_image(130, 100, image=img)
        self.canvas.image = img
        self.canvas.grid(column=1, row=0)

        self.username = username

        # Initialize encryption key
        self.encryption_key = self.load_key()

        # Create and configure UI elements
        self.create_ui()

    def create_ui(self):
        self.website_label = Label(text="Website:")
        self.website_label.grid(column=0, row=1)
        self.email_username_label = Label(text="Email/Username:")
        self.email_username_label.grid(column=0, row=2)
        self.password_label = Label(text="Random Password:")
        self.password_label.grid(column=0, row=3)
        self.password_len = IntVar()
        self.password_length_label = Label(text="Password length (6-15)")
        self.password_length_label.grid(column=2, row=3)
        self.length = Spinbox(from_=6, to_=15, textvariable=self.password_len)
        self.length.grid(column=2, row=4)

        self.website_entry = Entry(width=50)
        self.website_entry.grid(column=1, row=1, columnspan=2)
        self.website_entry.focus()
        self.email_username_entry = Entry(width=50)
        self.email_username_entry.grid(column=1, row=2, columnspan=2)
        self.email_username_entry.insert(0, "info@camilleonoda.com")
        self.password_entry = Entry(width=28)
        self.password_entry.grid(column=1, row=3)

        self.generated_password = StringVar()
        self.generate_password_button = Button(text="Generate Password", command=self.rand_pass_gen)
        self.generate_password_button.grid(column=2, row=5, padx=(0, 10))
        self.add_button = Button(text="Add", command=self.save)
        self.add_button.grid(column=2, row=6, ipadx=5, padx=(0, 79))
        self.clipboard = Button(text="Copy to clipboard", command=self.copy_password)
        self.clipboard.grid(column=1, row=4, padx=(0, 62))
        self.search_button = Button(text="Search Password", command=self.search_password)
        self.search_button.grid(column=2, row=7, padx=(0, 24))

        self.error_label = Label(text="", fg="red")
        self.error_label.grid(column=1, row=5)

    def load_key(self):
        key_file_path = "secret.key"
        if not os.path.isfile(key_file_path):
            print("Encryption key file not found. Please generate the key first.")
            return None
        with open(key_file_path, "rb") as key_file:
            key = key_file.read()

        if key is None:
            print("Error: Encryption key is missing or invalid.")
        
        return key


    def generate_key(self):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        print("Generated key and stored securely")

        self.generate_key()

    def encrypt_data(self, data):
        fernet = Fernet(self.encryption_key)
        encrypted_data = fernet.encrypt(data.encode())
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        fernet = Fernet(self.encryption_key)
        try:
            decrypted_data = fernet.decrypt(encrypted_data).decode()
            return decrypted_data
        except cryptography.fernet.InvalidToken:
            return "Invalid or corrupted data"


    def save(self):
        website = self.website_entry.get().lower()
        email = self.email_username_entry.get()
        password = self.password_entry.get()

        if not website or not email or not password:
            self.error_label.config(text="Please fill in all required information", fg="red")
        else:
            encrypted_password = self.encrypt_data(password)
            lines = self.read_data()

            if self.website_exists(website, lines):
                self.update_data(self.username, website, email, encrypted_password, lines)
            else:
                validate = messagebox.askokcancel(
                    title=website, message=f"Website: {website} \n Emai: {email} \n Password: {password} \n Do you want to save?"
                )
                if validate:
                    with open("data.txt", "a") as file:
                        file.write("Username | Website | Email | Encrypted password\n")
                        file.write(f"{self.username} | {website} | {email} | {encrypted_password}\n")
                    self.clear_entries()
                    messagebox.showinfo(title=None, message="Data saved!")
                    self.error_label.config(text="")

    def clear_entries(self):
        self.website_entry.delete(0, END)
        self.password_entry.delete(0, END)

    def read_data(self):
        file_path = "data.txt"
        if not os.path.exists(file_path):
            with open(file_path, "w"):
                pass

        with open(file_path, "r") as file:
            lines = file.readlines()
        return lines

    def website_exists(self, website, lines):
        for x, line in enumerate(lines):
            data = line.strip().split(" | ")
            if data[1].strip().lower() == website:
                return x
        return None

    def update_data(self, username, website, email, password, lines):
        update = messagebox.askyesno(
            title=website,
            message=f"The website '{website}' already exists in the data file. Do you want to update its information?",
        )
        if update:
            index = self.website_exists(website, lines)
            if index is not None:
                lines[index] = f"{self.username} | {website} | {email} | {password}\n"
                with open("data.txt", "w") as file:
                    file.writelines(lines)
                self.clear_entries()
                messagebox.showinfo(title=None, message="Data updated!")

    def rand_pass_gen(self):
        password = ""
        password_len = int(self.password_len.get())
        combination = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]
        character = ''.join(combination)

        for _ in range(password_len):
            password += random.choice(character)
        self.password_entry.insert(0, password)

    def get_decrypted_password(self, website, lines):
        for x, line in enumerate(lines):
            data = line.strip().split(" | ")
            if len(data) >= 2 and data[1].strip().lower() == website:
                encrypted_password = data[3]
                decrypted_password = self.decrypt_data(encrypted_password)
                return decrypted_password

        return None

    def search_password(self):
        website = self.website_entry.get()
        decrypted_password = self.get_decrypted_password(website, self.read_data())

        if decrypted_password:
            pyperclip.copy(decrypted_password)
            messagebox.showinfo(title=None, message=f"Password for {website} copied to clipboard.")
        else:
            messagebox.showerror(title=None, message=f"Password for {website} not found or could not be decrypted.")

    def copy_password(self):
        pyperclip.copy(self.password_entry.get())
        messagebox.showinfo(title=None, message="Password copied to clipboard.")

    def run(self):
        self.window.mainloop()

class PasswordPrompt:
    def __init__(self):
        self.password_prompt = Tk()
        self.password_prompt.title("Enter your credentials")
        self.password_prompt.config(padx=30, pady=30)
        self.password_prompt.geometry("300x150")

        self.username_label = Label(self.password_prompt, text="Username:")
        self.username_label.grid(column=0, row=1)
        self.username_entry = Entry(self.password_prompt)
        self.username_entry.grid(column=1, row=1)
        self.username_entry.focus()

        self.password_prompt_label = Label(self.password_prompt, text="Password:")
        self.password_prompt_label.grid(column=0, row=2)
        self.password_prompt_entry = Entry(self.password_prompt, show="*")
        self.password_prompt_entry.grid(column=1, row=2)

        self.password_submit_password = Button(self.password_prompt, text="Submit", command=self.check_credentials)
        self.password_submit_password.grid(column=1, row=3)

    def check_credentials(self):
        entered_username = self.username_entry.get()
        entered_password = self.password_prompt_entry.get()
        if entered_username == "camille" and entered_password == "1234":
            self.password_prompt.destroy()
            user = User(entered_username, entered_password)
            user.password_manager.run()
        else:
            self.credentials_error = Label(text="Incorrect username or password", fg="red")
            self.credentials_error.grid(column=1, row=4)

    def run(self):
        self.password_prompt.mainloop()

if __name__ == "__main__":
    password_prompt = PasswordPrompt()
    password_prompt.run()