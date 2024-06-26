import customtkinter
import tkinter
from tkinter import ttk
from CTkTable import CTkTable


class NiveisPartida(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0)

        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # header
        header = Header(self)
        header.grid(row=0, columnspan=3, sticky="we", padx=15)

        # main frame
        main_frame = MainFrame(self)
        main_frame.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=(15))

        # footer
        customtkinter.CTkProgressBar(self, corner_radius=0).grid(
            row=3, column=0, columnspan=3, sticky="we"
        )


class Header(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0, fg_color="pink")

        font = customtkinter.CTkFont(size=17)
        customtkinter.CTkLabel(
            self,
            font=font,
            text="Niveis de Partida",
            anchor="w",
        ).pack(fill="x", pady=(15, 15))

        ttk.Separator(self, orient="horizontal").pack(fill="x", pady=(0, 10))


class MainFrame(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0, fg_color="red")

        self.columnconfigure(1, weight=1)
        self.columnconfigure(0, minsize=100)
        self.columnconfigure(2, minsize=100)

        # carregar dadger
        customtkinter.CTkLabel(
            self, text="Arquivo:", anchor="w", bg_color="yellow"
        ).grid(row=0, column=0, sticky="we")
        customtkinter.CTkLabel(
            self, text="DADGER", anchor="center", bg_color="blue"
        ).grid(row=0, column=1, sticky="we")
        customtkinter.CTkButton(self, text="Alterar", corner_radius=4, width=100).grid(
            row=0, column=2
        )

        # # carregar confhd
        customtkinter.CTkLabel(
            self, text="CONFHD", anchor="center", bg_color="blue"
        ).grid(row=1, column=1, sticky="we")
        customtkinter.CTkButton(self, text="Alterar", corner_radius=4, width=100).grid(
            row=1, column=2
        )

        # # selecionar fonte (rdh ou relato)
        radio_fonte_frame = customtkinter.CTkFrame(self, fg_color="pink")
        radio_var = tkinter.IntVar(value=1)
        customtkinter.CTkRadioButton(
            radio_fonte_frame,
            text="RDH",
            command=lambda: self.radiobutton_fonte_event(radio_var),
            variable=radio_var,
            value=1,
        ).pack(side="left", anchor="e")

        customtkinter.CTkRadioButton(
            radio_fonte_frame,
            text="Relato",
            command=lambda: self.radiobutton_fonte_event(radio_var),
            variable=radio_var,
            value=2,
        ).pack(side="right", anchor="e")
        radio_fonte_frame.grid(row=2, column=1)

        customtkinter.CTkButton(self, text="Abrir", corner_radius=4, width=100).grid(
            row=3, column=2
        )

        # table earm
        CTkTable(self, row=4, column=7, header_color="white").grid(row=4, column=1)

        # # semana relato
        radio_semana_frame = customtkinter.CTkFrame(self, fg_color="pink")
        radio_semana_var = tkinter.IntVar(value=1)
        for s in range(6):
            customtkinter.CTkRadioButton(
                radio_semana_frame,
                text=f"Semana {s}",
                command=lambda: self.radiobutton_semana_event(radio_semana_var),
                variable=radio_semana_var,
                value=1,
            ).pack(side="left", anchor="e")
        radio_semana_frame.grid(row=5, column=1)

        # entry earm
        entry_earm_frame = customtkinter.CTkFrame(self, fg_color="pink")
        customtkinter.CTkEntry(entry_earm_frame, placeholder_text="SE", width=70).grid(
            row=0, column=0, padx=3
        )
        customtkinter.CTkEntry(entry_earm_frame, placeholder_text="S", width=70).grid(
            row=0, column=1, padx=3
        )
        customtkinter.CTkEntry(entry_earm_frame, placeholder_text="NE", width=70).grid(
            row=0, column=2, padx=3
        )
        customtkinter.CTkEntry(entry_earm_frame, placeholder_text="N", width=70).grid(
            row=0, column=3, padx=3
        )
        customtkinter.CTkEntry(
            entry_earm_frame, placeholder_text="Itapu", width=70
        ).grid(row=1, column=0, pady=(6, 0))
        entry_earm_frame.grid(row=6, column=1)

        # checkbox saida
        checkbox_saida_frame = customtkinter.CTkFrame(self, fg_color="pink")
        check_blocouh_var = customtkinter.StringVar(value="on")
        customtkinter.CTkCheckBox(
            checkbox_saida_frame,
            text="Bloco UH",
            variable=check_blocouh_var,
            onvalue="on",
            offvalue="off",
        ).pack(side="left")
        check_confhd_var = customtkinter.StringVar(value="off")
        customtkinter.CTkCheckBox(
            checkbox_saida_frame,
            text="CONFHD",
            variable=check_confhd_var,
            onvalue="on",
            offvalue="off",
        ).pack(side="left")
        checkbox_saida_frame.grid(row=7, column=1)

        customtkinter.CTkButton(self, text="Gerar", corner_radius=4, width=100).grid(
            row=8, column=2
        )

        for child in self.winfo_children()[:]:
            child.grid_configure(padx=0, pady=(20, 0))

    def radiobutton_fonte_event(self, radio_var):
        print("radiobutton toggled, current value:", radio_var.get())
