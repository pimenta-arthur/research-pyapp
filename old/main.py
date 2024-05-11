import tkinter as tk
from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton
from page1 import Page1
from page2 import Page2
from page3 import Page3


class App(CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Custom Tkinter App")
        self.geometry("800x600")

        # Create sidebar frame
        self.sidebar_frame = CTkFrame(self, corner_radius=10)
        self.sidebar_frame.pack(side=tk.LEFT, fill="y")

        # Create navigation buttons
        self.nav_buttons = []
        for i in range(3):
            button = CTkButton(
                self.sidebar_frame,
                text=f"Page {i+1}",
                command=lambda i=i: self.switch_page(i),
            )
            button.pack(fill="x")
            self.nav_buttons.append(button)

        # Create page frames
        self.page_frames = [CTkFrame(self, corner_radius=10) for _ in range(3)]
        for frame in self.page_frames:
            frame.pack(side=tk.LEFT, fill="both", expand=True)

        # Set initial page
        self.current_page = 0
        self.page_frames[0].pack_forget()
        self.page_frames[1].pack_forget()
        self.page_frames[2].pack_forget()
        self.page_frames[self.current_page].pack(fill="both", expand=True)
        self.show_page()

    def switch_page(self, page_num):
        for i in range(3):
            if i == page_num:
                self.page_frames[i].pack(fill="both", expand=True)
            else:
                self.page_frames[i].pack_forget()
        self.current_page = page_num
        self.show_page()

    def show_page(self):
        if self.current_page == 0:
            self.page_frames[0].grid_slaves()[0].focus_set()
        elif self.current_page == 1:
            self.page_frames[1].grid_slaves()[0].focus_set()
        else:
            self.page_frames[2].grid_slaves()[0].focus_set()


if __name__ == "__main__":
    app = App()
    app.mainloop()
