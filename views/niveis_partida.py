import customtkinter
import tkinter


class NiveisPartida(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        # titulo
        customtkinter.CTkLabel(
            self, text="Niveis de Partida", bg_color="yellow", anchor="w"
        ).grid(row=0, columnspan=3, sticky="we", padx=10, pady=10)

        # main frame
        main_frame = MainFrame(self)
        main_frame.grid(
            row=1, column=0, columnspan=3, sticky="nsew", padx=(10, 10), pady=(0, 0)
        )

        # footer
        customtkinter.CTkProgressBar(self, corner_radius=0).grid(
            row=2, column=0, columnspan=3, sticky="we"
        )


class MainFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="red", corner_radius=0)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(0, minsize=100)
        self.columnconfigure(2, minsize=100)

        # self.rowconfigure(1, pad=10)

        # carregar dadger
        customtkinter.CTkLabel(self, text="PATH", bg_color="yellow").grid(
            row=0, column=1, sticky="we"
        )
        customtkinter.CTkButton(self, text="Abrir DADGER").grid(row=0, column=2)

        # # carregar confhd
        customtkinter.CTkLabel(self, text="PATH", bg_color="yellow").grid(
            row=1, column=1
        )
        customtkinter.CTkButton(self, text="Abrir CONFHD").grid(row=1, column=2)

        # # selecionar fonte (rdh ou relato)
        radio_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        radio_var = tkinter.IntVar(value=1)
        customtkinter.CTkRadioButton(
            radio_frame,
            text="RDH",
            command=lambda: self.radiobutton_event(radio_var),
            variable=radio_var,
            value=1,
        ).pack(side="left")

        customtkinter.CTkRadioButton(
            radio_frame,
            text="Relato",
            command=lambda: self.radiobutton_event(radio_var),
            variable=radio_var,
            value=2,
        ).pack(side="right")
        radio_frame.grid(row=2, column=0, columnspan=3)

        for child in self.winfo_children():
            child.grid_configure(padx=0, pady=(10, 0))

    def radiobutton_event(self, radio_var):
        print("radiobutton toggled, current value:", radio_var.get())
