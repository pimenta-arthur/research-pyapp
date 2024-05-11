import customtkinter


class NiveisPartida(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        customtkinter.CTkLabel(self, bg_color="yellow").pack(expand=True, fill="both")
