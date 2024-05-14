import customtkinter
import tkinter
from tkinter import ttk


class NiveisPartida(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0)

        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # header
        header = Header(self)
        header.grid(row=0, columnspan=3, sticky="we", padx=15, pady=(15, 5))

        # main frame
        main_frame = MainFrame(self)
        main_frame.grid(
            row=2, column=0, columnspan=3, sticky="nsew", padx=(15, 15), pady=(0, 0)
        )

        # footer
        customtkinter.CTkProgressBar(self, corner_radius=0).grid(
            row=3, column=0, columnspan=3, sticky="we"
        )


class Header(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0, fg_color="transparent")

        font = customtkinter.CTkFont(size=17)
        customtkinter.CTkLabel(
            self,
            font=font,
            text="Niveis de Partida",
            anchor="w",
        ).pack(fill="x", pady=(0, 15))

        ttk.Separator(self, orient="horizontal").pack(fill="x")


class MainFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0, fg_color="transparent")

        self.columnconfigure(1, weight=1)
        self.columnconfigure(0, minsize=100)
        self.columnconfigure(2, minsize=100)

        # carregar dadger
        customtkinter.CTkLabel(
            self, text="c/temp/test-file.txt.", anchor="w", bg_color="transparent"
        ).grid(row=0, column=1, sticky="we")
        customtkinter.CTkButton(
            self, text="Abrir DADGER", corner_radius=4, width=100
        ).grid(row=0, column=2)

        # # carregar confhd
        customtkinter.CTkLabel(
            self, text="Arquivo:", anchor="w", bg_color="yellow"
        ).grid(row=1, column=0, sticky="we")
        customtkinter.CTkButton(
            self, text="Abrir CONFHD", corner_radius=4, width=100
        ).grid(row=1, column=2)

        # # selecionar fonte (rdh ou relato)
        radio_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        radio_var = tkinter.IntVar(value=1)
        customtkinter.CTkRadioButton(
            radio_frame,
            text="RDH",
            command=lambda: self.radiobutton_event(radio_var),
            variable=radio_var,
            value=1,
        ).pack(side="left", anchor="e")

        customtkinter.CTkRadioButton(
            radio_frame,
            text="Relato",
            command=lambda: self.radiobutton_event(radio_var),
            variable=radio_var,
            value=2,
        ).pack(side="right", anchor="e")
        radio_frame.grid(row=2, column=0, columnspan=3)

        for child in self.winfo_children()[:]:
            child.grid_configure(padx=0, pady=(10, 0))

    def radiobutton_event(self, radio_var):
        print("radiobutton toggled, current value:", radio_var.get())
