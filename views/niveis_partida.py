import customtkinter
import tkinter


class NiveisPartida(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # customtkinter.CTkLabel(self, bg_color="yellow").pack(expand=True, fill="both")

        # footer
        # self.load_bar = customtkinter.CTkProgressBar(self)
        # self.load_bar.pack(expand=False, fill="x", side="bottom")

        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, pad=10)
        self.rowconfigure(3, pad=20)

        # titulo
        customtkinter.CTkLabel(self, text="Niveis de Partida", bg_color="yellow").grid(
            row=0, columnspan=2, sticky="w"
        )

        # carregar dadger
        customtkinter.CTkLabel(self, text="PATH", bg_color="yellow").grid(
            row=1, column=0
        )
        customtkinter.CTkButton(self, text="Carregar DADGER").grid(row=1, column=1)

        # carregar confhd
        customtkinter.CTkLabel(self, text="PATH", bg_color="yellow").grid(
            row=2, column=0
        )
        customtkinter.CTkButton(self, text="Carregar CONFHD").grid(row=2, column=1)

        # selecionar fonte (rdh ou relato)
        radio_var = tkinter.IntVar(value=1)
        customtkinter.CTkRadioButton(
            self,
            text="RDH",
            command=lambda: self.radiobutton_event(radio_var),
            variable=radio_var,
            value=1,
        ).grid(row=3, column=0)

        customtkinter.CTkRadioButton(
            self,
            text="Relato",
            command=lambda: self.radiobutton_event(radio_var),
            variable=radio_var,
            value=2,
        ).grid(row=3, column=1)

    def radiobutton_event(self, radio_var):
        print("radiobutton toggled, current value:", radio_var.get())
