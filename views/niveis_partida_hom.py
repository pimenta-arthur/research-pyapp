from customtkinter import (
    CTkFrame,
    CTkButton,
    CTkCheckBox,
    CTkEntry,
    CTkRadioButton,
    StringVar,
    CTkProgressBar,
    CTkLabel,
    CTkFont,
    filedialog,
)
from widgets import CTkAppButton
import tkinter
from tkinter import ttk, PhotoImage
from CTkTable import CTkTable
from PIL import Image


class NiveisPartidaHOM(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0, fg_color="transparent")

        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # header
        header = Header(self)
        header.grid(row=0, columnspan=3, sticky="we", padx=0)

        # main frame
        main_frame = MainFrame(self)
        main_frame.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=(20))

        # footer
        self.progress_bar = CTkProgressBar(self, corner_radius=0).grid(
            row=3, column=0, columnspan=3, sticky="we"
        )


class Header(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0, fg_color="transparent")

        font = CTkFont(size=17)
        CTkLabel(
            self,
            font=font,
            text="Niveis de Partida",
            anchor="w",
        ).pack(fill="x", pady=(20, 15), padx=20)

        ttk.Separator(self, orient="horizontal").pack(fill="x", pady=(0, 10), padx=20)


class MainFrame(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0, fg_color="transparent")

        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, minsize=0)
        self.columnconfigure(3, minsize=100)

        self.input_config_files()  # carregar dadger e confhd
        self.input_source_file()  # selecionar fonte (rdh ou relato)
        self.display_table()  # exibir niveis de earm por semana
        self.output_config()  # define opções de saida

        for child in self.winfo_children()[:]:
            child.grid_configure(padx=0, pady=(15, 0))

    def input_config_files(self):
        # dadger
        CTkLabel(self, text="DADGER", anchor="center", bg_color="transparent").grid(
            row=0, column=1, sticky="we"
        )
        CTkAppButton(
            self,
            text="Alterar",
        ).grid(row=0, column=3)

        # confhd
        CTkLabel(self, text="CONFHD", anchor="center", bg_color="transparent").grid(
            row=1, column=1, sticky="we"
        )
        CTkAppButton(
            self,
            text="Alterar",
            command=lambda: filedialog.askopenfile(),
        ).grid(row=1, column=3)

    def input_source_file(self):
        def open_file(label):
            file = filedialog.askopenfile()
            label.configure(text=file.name)

        radio_fonte_frame = CTkFrame(self, fg_color="transparent")
        radio_var = tkinter.IntVar(value=1)
        CTkRadioButton(
            radio_fonte_frame,
            text="RDH",
            command=lambda: self.radiobutton_fonte_event(radio_var),
            variable=radio_var,
            value=1,
        ).pack(side="left", anchor="e")

        CTkRadioButton(
            radio_fonte_frame,
            text="Relato",
            command=lambda: self.radiobutton_fonte_event(radio_var),
            variable=radio_var,
            value=2,
        ).pack(side="right", anchor="e")
        radio_fonte_frame.grid(row=2, column=1)

        source_label = CTkLabel(self, text="")
        source_label.grid(row=3, column=1)

        # open file
        CTkAppButton(
            self, text="Abrir", command=lambda label=source_label: open_file(label)
        ).grid(row=3, column=3)

    def display_table(self):
        # table earm
        CTkTable(
            self,
            row=4,
            column=7,
            header_color="white",
            corner_radius=5,
            border_width=0,
            colors=["#e2e3e2", "#e2e3e2"],
        ).grid(row=4, column=1)

        # semana relato
        radio_semana_frame = CTkFrame(self, fg_color="transparent")
        radio_semana_var = tkinter.IntVar(value=1)
        for s in range(1, 7):
            CTkRadioButton(
                radio_semana_frame,
                text=f"Semana {s}",
                command=lambda: self.radiobutton_semana_event(radio_semana_var),
                variable=radio_semana_var,
                value=s,
            ).pack(side="left", anchor="e")
        radio_semana_frame.grid(row=5, column=1)

    def entry_earm_box(self):
        # entrada earm
        entry_earm_frame = CTkFrame(self, fg_color="transparent")
        CTkEntry(entry_earm_frame, placeholder_text="SE", width=70).grid(
            row=0, column=0, padx=3
        )
        CTkEntry(entry_earm_frame, placeholder_text="S", width=70).grid(
            row=0, column=1, padx=3
        )
        CTkEntry(entry_earm_frame, placeholder_text="NE", width=70).grid(
            row=0, column=2, padx=3
        )
        CTkEntry(entry_earm_frame, placeholder_text="N", width=70).grid(
            row=0, column=3, padx=3
        )
        CTkEntry(entry_earm_frame, placeholder_text="Itapu", width=70).grid(
            row=1, column=0, pady=(6, 0)
        )
        entry_earm_frame.grid(row=6, column=1)

    def output_config(self):
        # checkbox saida
        checkbox_saida_frame = CTkFrame(self, fg_color="transparent")
        check_blocouh_var = StringVar(value="on")
        CTkCheckBox(
            checkbox_saida_frame,
            text="Bloco UH",
            variable=check_blocouh_var,
            onvalue="on",
            offvalue="off",
        ).pack(side="left")
        check_confhd_var = StringVar(value="off")
        CTkCheckBox(
            checkbox_saida_frame,
            text="CONFHD",
            variable=check_confhd_var,
            onvalue="on",
            offvalue="off",
        ).pack(side="left")
        checkbox_saida_frame.grid(row=7, column=1)

        CTkAppButton(self, text="Gerar", width=80, height=25).grid(row=8, column=3)

    def radiobutton_fonte_event(self, radio_var):
        print("radiobutton toggled, current value:", radio_var.get())
