from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_gen(num_letters=4, num_symbols=4, num_numbers=4):
    letter_list = []
    symbol_list = []
    number_list = []

    def element_list_populate(element_count, element_type_list, element_list):
        for _ in range(element_count):
            random_element_index = random.randint(
                0, len(element_type_list) - 1)
            random_element = element_type_list[random_element_index]
            element_list.append(str(random_element))

    element_list_populate(num_letters, letters, letter_list)
    element_list_populate(num_symbols, symbols, symbol_list)
    element_list_populate(num_numbers, numbers, number_list)

    password_list = letter_list + symbol_list + number_list

    mixed_password = []

    for _ in range(0, len(password_list)):
        random_index = random.randint(0, len(password_list) - 1)
        random_element = password_list[random_index]
        mixed_password.append(str(random_element))
        password_list.pop(random_index)

    generated_password = "".join(mixed_password)

    password_input.insert(0, generated_password)

    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Insufficient website and/or password length",
                             message="Website and/or password info shold not be blank")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"There are the details entered:\nEmail: {email}\nPassword: {password}\nClick Ok to confirm your entry.")
        if is_ok:
            try:
                with open("saved_passwords.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("saved_passwords.json", "w") as data_file:
                    data = json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("saved_passwords.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            finally:
                messagebox.showinfo(title="Success",
                                    message=f"Entry for {website} successfully saved.")

                website_input.delete(0, "end")
                email_input.delete(0, "end")
                password_input.delete(0, "end")

# ---------------------------- SEARCH FUNCTION ------------------------------- #


def search_password():
    search_query = website_input.get()
    if len(search_query) == 0:
        messagebox.showerror(title="Search Error",
                             message="Search query cannot be empty.")
    else:
        with open("saved_passwords.json", "r") as data_file:
            data = json.load(data_file)
            website_found = False
            for website in data:
                if search_query.lower() == website.lower():
                    email = data[str(website)]["email"]
                    password = data[str(website)]["password"]
                    messagebox.showinfo(
                        title="Found Entry", message=f"Information for {website}:\nEmail: {email}\nPassword: {password}.")
                    website_found = True
                    break
                else:
                    pass
            if not website_found:
                messagebox.showinfo(title="Not Found",
                                    message="So such entry found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator & Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
app_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=app_image)
canvas.grid(row=0, column=1)

# --------------LABELS--------------------#
website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

# --------------INPUTS--------------------#
website_input = Entry(width=21)
website_input.focus()
website_input.grid(row=1, column=1)

email_input = Entry(width=35)
email_input.insert(0, "email@server.com")
email_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# --------------BUTTONS--------------------#
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

generate_button = Button(text="Generate Password",
                         width=13, command=password_gen)
generate_button.grid(row=3, column=2, columnspan=2)

search_button = Button(text="Search", width=13, command=search_password)
search_button.grid(row=1, column=2, columnspan=2)


window.mainloop()
