import customtkinter


class LerPrevs(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        customtkinter.CTkLabel(self, bg_color="red").pack(expand=True, fill="both")
