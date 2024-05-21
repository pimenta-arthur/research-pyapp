from customtkinter import CTkButton


class CTkAppButton(CTkButton):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.configure(width=80, height=25)
