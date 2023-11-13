import tkinter as tk
from tkinter import ttk
import csv
from handle_data import HandleData

class ViewSalesPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        result_label = tk.Label(self, text="")
        result_label.pack()
        tree = ttk.Treeview(self, columns=("Sales Representative", "Department", "Manager", "Price","Date"))
        try:
            with open("sales_data.csv", 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                data = [row for row in csv_reader]
                data = data[1:]
                # display_csv_data(data)
                for i in tree.get_children():
                    tree.delete(i)
                for row in data:
                    tree.insert('', 'end', values=row)
        except FileNotFoundError:
            result_label.config(text="File not found")

         # Adjust columns as needed
        tree.heading("#1", text="Sales Representative")
        tree.heading("#2", text="Department")
        tree.heading("#3", text="Manager")
        tree.heading("#4", text="Price")
        tree.heading("#5", text="Date")
        tree.pack()

        # Add input fields and button
        input_frame = tk.Frame(self)
        input_frame.pack()

        # Sales Representative Textfield
        sales_rep_label = tk.Label(input_frame, text="Sales Representative")
        sales_rep_label.grid(row=0, column=0)
        sales_rep_entry = tk.Entry(input_frame)
        sales_rep_entry.grid(row=0, column=1)

        # Department Dropdown
        department_label = tk.Label(input_frame, text="Department")
        department_label.grid(row=0, column=2)
        department_var = tk.StringVar()
        department_dropdown = ttk.Combobox(input_frame, textvariable=department_var, values=["Dept1", "Dept2", "Dept3"])
        department_dropdown.grid(row=0, column=3)

        # Manager Textfield
        manager_label = tk.Label(input_frame, text="Manager")
        manager_label.grid(row=0, column=4)
        manager_entry = tk.Entry(input_frame)
        manager_entry.grid(row=0, column=5)

        # Price Textfield
        price_label = tk.Label(input_frame, text="Price")
        price_label.grid(row=0, column=6)
        price_entry = tk.Entry(input_frame)
        price_entry.grid(row=0, column=7)

        # Date Date Selection
        date_label = tk.Label(input_frame, text="Date")
        date_label.grid(row=0, column=8)
        date_input = tk.Entry(input_frame)
        date_input.grid(row=0, column=9)

        # Function to print user input
        def print_user_input():
            sales_rep = sales_rep_entry.get()
            department = department_var.get()
            manager = manager_entry.get()
            price = price_entry.get()
            date = date_input.get()

            print("Sales Representative:", sales_rep)
            print("Department:", department)
            print("Manager:", manager)
            print("Price:", price)
            print("Date:", date)

            handler = HandleData()
            handler.addNewSale(row=[sales_rep, department, manager, price, date])

            sales_rep_entry.delete(0, tk.END)
            # department_var.delete(0, tk.END)
            manager_entry.delete(0, tk.END)
            price_entry.delete(0, tk.END)
            date_input.delete(0, tk.END)

        # Print Button
        print_button = tk.Button(self, text="Print User Input", command=print_user_input)
        print_button.pack()

        button = tk.Button(self, text="Go to Start Page",command=lambda: controller.show_frame(LoginPage))
        button.pack()


from pages.LoginPage import LoginPage