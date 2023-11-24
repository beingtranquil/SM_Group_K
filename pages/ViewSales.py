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

        # Function to load and display CSV data
        def display_csv_data():
            try:
                with open("generated_data.csv", 'r') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    data = [row for row in csv_reader]
                    data = data[1:]
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

        display_csv_data()

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
        department_dropdown = ttk.Combobox(input_frame, textvariable=department_var, values=["Marketing", "HR", "IT", "Sales"])
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
        def add_sale():
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
            display_csv_data()

        tk.Label(input_frame, text="").grid(row=1,column=0)
        print_button = tk.Button(input_frame, text="Add Sale", command=add_sale)
        print_button.grid(row=2, column=4)
        # print_button.pack()


        def custom_average():
            handler = HandleData()
            ans = handler.sales_METRICSTICS()

            min_ = "Minumum = " + str(ans[0])
            min_variable.set(min_)

            max_ = "Maximum = " + str(ans[1])
            max_variable.set(max_)

            mode_ = "Mode = "
            for x in ans[2]:
                mode_ += " " + str(x) + ","
            mode_variable.set(mode_[:-1])

            median_ = "Median = " + str(ans[3])
            median_variable.set(median_)

            mean_ = "Mean = " + str(ans[4])
            mean_variable.set(mean_)

            mad_ = "Mean absolute deviation = " + str(ans[5])
            mad_variable.set(mad_)

            sig_ = "Standard deviation = " + str(ans[6])
            sig_variable.set(sig_)

            print(ans)
        
        tk.Label(input_frame, text="").grid(row=3,column=0)
        
        min_variable = tk.StringVar()
        min_variable.set("Minumum = ")
        min_label = tk.Label(input_frame, textvariable=min_variable)
        min_label.grid(row=4, column=0)

        max_variable = tk.StringVar()
        max_variable.set("Maximum = ")
        max_label = tk.Label(input_frame, textvariable=max_variable)
        max_label.grid(row=5, column=0)

        mode_variable = tk.StringVar()
        mode_variable.set("Mode = ")
        mode_label = tk.Label(input_frame, textvariable=mode_variable)
        mode_label.grid(row=6, column=0)

        median_variable = tk.StringVar()
        median_variable.set("Median = ")
        median_label = tk.Label(input_frame, textvariable=median_variable)
        median_label.grid(row=7, column=0)

        mean_variable = tk.StringVar()
        mean_variable.set("Mean = ")
        mean_label = tk.Label(input_frame, textvariable=mean_variable)
        mean_label.grid(row=8, column=0)

        mad_variable = tk.StringVar()
        mad_variable.set("Mean absolute deviation = ")
        mad_label = tk.Label(input_frame, textvariable=mad_variable)
        mad_label.grid(row=9, column=0)

        sig_variable = tk.StringVar()
        sig_variable.set("Standard deviation = ")
        sig_label = tk.Label(input_frame, textvariable=sig_variable)
        sig_label.grid(row=10, column=0)

        custom_avg_button = tk.Button(input_frame, text="Calculate  Metristics", command=custom_average)
        custom_avg_button.grid(row=4,column=4)

        tk.Label(input_frame, text="").grid(row=11,column=0)

        # button = tk.Button(input_frame, text="Logout",command=lambda: controller.show_frame(LoginPage))
        # button.grid(row=12, column=4)


from pages.LoginPage import LoginPage