import tkinter as tk
from pages.LoginPage import LoginPage
from pages.ViewSales import ViewSalesPage

class Metricstics(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Metristics")
        # self.geometry("400x300")
        self.state('zoomed')

        # self.configure(bg="black")

        # Create a container frame to hold all pages
        container = tk.Frame(self, bg="black")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # Create multiple pages as separate frames
        for F in (LoginPage, ViewSalesPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)
    
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()



if __name__ == "__main__":
    app = Metricstics()
    app.mainloop()