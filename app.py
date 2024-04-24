import tkinter as tk
from customtkinter import CTk, CTkFrame
from tkinter import ttk


class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Custom Tkinter Application")
        self.create_widgets()

    def create_widgets(self):
        # Create the sidebar frame
        self.sidebar_frame = CTkFrame(self, corner_radius=0, width=200, height=400)
        self.sidebar_frame.pack(side=tk.LEFT, fill="y")

        # Create the main frame
        self.main_frame = CTkFrame(self, corner_radius=0, width=800, height=600)
        self.main_frame.pack(side=tk.RIGHT, expand=True)

        # Create the treeview widget inside the sidebar frame
        # self.treeview = ttk.Treeview(
        #     self.sidebar_frame,
        #     columns=("Column1", "Column2", "Column3"),
        #     show="headings",
        # )
        # self.treeview.column("Column1", width=100)
        # self.treeview.column("Column2", width=200)
        # self.treeview.column("Column3", width=200)
        # self.treeview.heading("Column1", text="Column 1")
        # self.treeview.heading("Column2", text="Column 2")
        # self.treeview.heading("Column3", text="Column 3")

        self.treeview = ttk.Treeview(self.sidebar_frame)
        self.treeview.pack(side=tk.TOP, fill="both", expand=True)

        # Insert data into the Treeview
        items = [
            {"Item 1": ["Subitem1", "Subitem 11", "Subitem2", "Subitem 12"]},
            {"Item 2": ["Subitem1", "Subitem 21", "Subitem2", "Subitem 22"]},
            # {"Item": "Item 3", "Subitem1": "Subitem 31", "Subitem2": "Subitem 32"},
            # {"Item": "Item 4", "Subitem1": "Subitem 41", "Subitem2": "Subitem 42"},
            # {"Item": "Item 5", "Subitem1": "Subitem 51", "Subitem2": "Subitem 52"},
        ]

        items = {
            "Item 1": ["Subitem1", "Subitem 11", "Subitem2", "Subitem 12"],
            "Item 2": ["Subitem1", "Subitem 21", "Subitem2"],
        }

        for item, subitems in items.items():
            i = self.treeview.insert("", tk.END, text=item, open=True)
            for subitem in subitems:
                self.treeview.insert(i, tk.END, text=subitem)
            # self.treeview.insert("", tk.END, values=list(item.values()))

        # item = self.treeview.insert("", tk.END, text="Item 1")
        # self.treeview.insert(item, tk.END, text="Subitem 1")


if __name__ == "__main__":
    app = App()
    app.mainloop()
