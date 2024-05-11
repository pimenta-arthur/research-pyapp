from customtkinter import CTkFrame, CTkLabel, CTkButton


class Page2:
    def __init__(self, root):
        self.root = root
        self.frame = CTkFrame(root, width=200, height=100)
        self.frame.pack(pady=20)

        self.label = CTkLabel(self.frame, text="This is page 2!")
        self.label.pack(padx=10, pady=10)

        self.button = CTkButton(
            self.frame, text="Click me!", command=lambda: print("You clicked me!")
        )
        self.button.pack(padx=10, pady=10)
