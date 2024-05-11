import customtkinter
from views.ler_prevs import LerPrevs
from views.niveis_partida import NiveisPartida


class App(customtkinter.CTk):
    def __init__(self, title, size, sidebar_width):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")

        # create widgets
        self.sidebar = SideBar(self, sidebar_width)
        self.main = Main(self)


class SideBar(customtkinter.CTkFrame):
    def __init__(self, parent, width):
        super().__init__(parent, width)

        self.parent = parent

        # create sidebar views
        self.create_widgets()

        # define layout
        self.pack(fill="y", side="left")
        self.pack_propagate(0)

    def create_widgets(self):
        customtkinter.CTkButton(
            self,
            text="Ler Prevs",
            corner_radius=0,
            fg_color="transparent",
            text_color="black",
            command=lambda: self.switch_view(LerPrevs),
        ).pack(fill="x")

        customtkinter.CTkButton(
            self,
            text="Niveis de Partida",
            corner_radius=0,
            fg_color="transparent",
            text_color="black",
            command=lambda: self.switch_view(NiveisPartida),
        ).pack(fill="x")

    def switch_view(self, View):
        print("Cliquei em:")
        # print(self.winfo_children())
        # print(self.parent.main.winfo_children())

        # clear main frame and open view
        self.clear_frame(self.parent.main)
        self.parent.main.open_view(View)

    def clear_frame(self, frame):
        for widgets in frame.winfo_children():
            widgets.destroy()


class Main(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # open home view
        self.open_view(LerPrevs)

        # define layout
        self.pack(expand=True, fill="both", side="right", padx=(10, 0), pady=0)
        self.pack_propagate(0)

    def open_view(self, View):
        view = View(self)
        view.pack(expand=True, fill="both")


if __name__ == "__main__":
    # setting
    title = "PyResarch"
    size = (800, 1000)
    sidebar_width = 150

    # initialize app
    app = App(title, size, sidebar_width)
    app.mainloop()
