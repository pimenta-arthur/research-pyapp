import customtkinter as ct
from customtkinter import CTkLabel, CTkButton


class Page3(ct.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Page 3")

        # Create content
        label = CTkLabel(self, text="This is page 3")
        button = CTkButton(
            self,
            text="Go back to Page 1",
            command=lambda: print("Going back to page 1"),
        )
        label.pack(fill="both", expand=True)
        button.pack()
