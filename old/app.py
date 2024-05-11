import tkinter as tk
import customtkinter
from customtkinter import CTk, CTkFrame
from tkinter import ttk
from page1 import Page1
from page2 import Page2

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Custom Tkinter Application")
        self.create_widgets()

    def create_widgets(self):
        # Create the sidebar frame
        self.sidebar_frame = CTkFrame(self, corner_radius=0, width=200, height=400)
        self.sidebar_frame.pack(side=tk.LEFT, fill="y")

        self.pages = [Page1(self), Page2(self)]

        # Create the main frame
        self.main_frame = CTkFrame(self, corner_radius=0, width=800, height=600)
        self.main_frame.pack(side=tk.RIGHT, expand=True)

        # Create the treeview widget inside the sidebar frame
        self.treeview = ttk.Treeview(self.sidebar_frame)
        self.treeview.pack(side=tk.TOP, fill="both", expand=True)

        # Insert data into the Treeview
        items = {
            "Item 1": ["Subitem11", "Subitem 12", "Subitem13", "Subitem 14"],
            "Item 2": ["Subitem21", "Subitem 22", "Subitem23"],
        }

        # for item, subitems in items.items():
        #     i = self.treeview.insert("", tk.END, text=item, open=True)
        #     for subitem in subitems:
        #         self.treeview.insert(i, tk.END, text=subitem)

        for page in self.pages:
            i = self.treeview.insert(
                "", tk.END, text=page.label.cget("text"), open=True
            )

    def switch_page(self, event):
        selected_item = self.treeview.selection()[0]
        page_name = self.treeview.item(selected_item)["values"][0]
        for page in self.pages:
            if page.label.cget("text") == page_name:
                page.frame.config(relief=tk.SUNKEN)
                break


if __name__ == "__main__":
    app = App()
    app.mainloop()
