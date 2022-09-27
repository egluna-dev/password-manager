from tkinter import *


class UserInterface:
    def __init__(self, save_password, password_gen, search_password):
        self.window = Tk()
        self.window.title("Password Generator & Manager")
        self.window.config(padx=50, pady=50, bg="white")

        self.canvas = Canvas(width=200, height=200,
                             bg="white", highlightthickness=0)
        app_image = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=app_image)
        self.canvas.grid(row=0, column=1)

        # --------------LABELS--------------------#
        self.website_label = Label(text="Website:", bg="white")
        self.website_label.grid(row=1, column=0)

        self.email_label = Label(text="Email/Username:", bg="white")
        self.email_label.grid(row=2, column=0)

        self.password_label = Label(text="Password:", bg="white")
        self.password_label.grid(row=3, column=0)

        # --------------INPUTS--------------------#
        self.website_input = Entry(width=21)
        self.website_input.focus()
        self.website_input.grid(row=1, column=1)

        self.email_input = Entry(width=35)
        self.email_input.insert(0, "email@server.com")
        self.email_input.grid(row=2, column=1, columnspan=2)

        self.password_input = Entry(width=21)
        self.password_input.grid(row=3, column=1)

        # --------------BUTTONS--------------------#
        self.add_button = Button(text="Add", width=36, command=save_password)
        self.add_button.grid(row=4, column=1, columnspan=2)

        self.generate_button = Button(text="Generate Password",
                                      width=13, command=password_gen)
        self.generate_button.grid(row=3, column=2, columnspan=2)

        self.search_button = Button(
            text="Search", width=13, command=search_password)
        self.search_button.grid(row=1, column=2, columnspan=2)

        self.window.mainloop()
