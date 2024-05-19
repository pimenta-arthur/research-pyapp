import customtkinter
from views.ler_prevs import LerPrevs

# from views.niveis_partida import NiveisPartida
from views.niveis_partida_hom import NiveisPartidaHOM as NiveisPartida

# customtkinter.set_appearance_mode("dark")
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("assets/themes/light-default.json")


class App(customtkinter.CTk):
    def __init__(self, title, size, sidebar_width, fg_color_sidebar, fg_color_main):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")

        # create widgets
        self.main = Main(self, fg_color_main)
        self.sidebar = SideBar(self, sidebar_width, fg_color_sidebar, self.main.views)


class SideBar(customtkinter.CTkFrame):
    def __init__(self, parent, sidebar_width, fg_color_sidebar, views):
        super().__init__(
            parent, width=sidebar_width, corner_radius=0, fg_color=fg_color_sidebar
        )

        self.parent = parent

        # create sidebar views
        self.create_widgets(views)

        # define layout
        self.pack(fill="y", side="left")
        self.pack_propagate(0)

    def create_widgets(self, views):
        for view_name, view in views.items():
            customtkinter.CTkButton(
                self,
                text=5 * " " + view_name,
                corner_radius=0,
                fg_color="transparent",
                hover_color="#dbdbdb",
                text_color="black",
                font=customtkinter.CTkFont(size=13),
                # compound="left",
                anchor="w",
                command=lambda view_name=view_name: self.switch_view(view_name),
            ).pack(fill="x")

    def switch_view(self, view_name):
        print("Cliquei em:", view_name)
        # print("button", self.text)
        # print("Sidebar widgets:", self.winfo_children())
        # print("Main widgets", self.parent.main.winfo_children())
        # print("App widgets", self.parent.winfo_children())

        # clear main frame and open view
        self.clear_frame(self.parent.main)
        self.parent.main.open_view(view_name)

    def clear_frame(self, frame):
        for widgets in frame.winfo_children():
            widgets.pack_forget()


class Main(customtkinter.CTkFrame):
    def __init__(self, parent, fg_color_views):
        super().__init__(parent)

        # load views
        self.views = {
            "Ler Prevs": LerPrevs(self),
            "Niveis de Partida": NiveisPartida(self),
        }

        # open home view
        self.open_view("Niveis de Partida")

        # define layout
        self.pack(expand=True, fill="both", side="right", padx=(0, 0), pady=0)
        self.pack_propagate(0)

    def open_view(self, view_name):
        view = self.views[view_name]
        view.pack(expand=True, fill="both")


if __name__ == "__main__":
    # setting
    title = "PyResarch"
    size = (1000, 900)
    sidebar_width = 180
    fg_color_sidebar = "#e2e3e2"
    fg_color_main = "#e7ebf1"

    # initialize app
    app = App(title, size, sidebar_width, fg_color_sidebar, fg_color_main)
    app.mainloop()
