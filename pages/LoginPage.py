import tkinter as tk
from tkinter import ttk


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = ttk.Label(self, text="Login", font=("Helvetica", 20))
        self.label.pack(pady=10)

        self.username_label = ttk.Label(self, text="Username:")
        self.username_label.pack(pady=5)

        self.username_entry = ttk.Entry(self)
        self.username_entry.configure(width=20)
        self.username_entry.pack(pady=5, padx=20, ipadx=10, ipady=5)

        self.password_label = ttk.Label(self, text="Password:")
        self.password_label.pack(pady=5)

        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.configure(width=20)
        self.password_entry.pack(pady=5, padx=20, ipadx=10, ipady=5)

        self.login_button = ttk.Button(self, text="Login",command=self.login)
        self.login_button.pack(pady=10)
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "user" and password == "pass":
            self.controller.show_frame(ViewSalesPage)
        else:
            # Add code to handle invalid login, e.g., show an error message
            pass



from pages.ViewSales import ViewSalesPage