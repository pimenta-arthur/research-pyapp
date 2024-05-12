import customtkinter
from views.ler_prevs import LerPrevs
from views.niveis_partida import NiveisPartida

# customtkinter.set_appearance_mode("dark")
# customtkinter.set_appearance_mode("light")


class App(customtkinter.CTk):
    def __init__(self, title, size, sidebar_width):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")

        # create widgets
        self.main = Main(self)
        self.sidebar = SideBar(self, sidebar_width, self.main.views)


class SideBar(customtkinter.CTkFrame):
    def __init__(self, parent, width, views):
        super().__init__(parent, width)

        self.parent = parent

        # create sidebar views
        self.create_widgets(views)

        # define layout
        self.pack(fill="y", side="left")
        self.pack_propagate(0)

    def create_widgets(self, views):
        for view_name, view in views.items():
            print("DADA", view_name)
            customtkinter.CTkButton(
                self,
                text=view_name,
                corner_radius=0,
                # fg_color="transparent",
                # text_color="black",
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
    def __init__(self, parent):
        super().__init__(parent)

        # load views
        self.views = {
            "Ler Prevs": LerPrevs(self),
            "Niveis de Partida": NiveisPartida(self),
        }

        # open home view
        self.open_view("Niveis de Partida")

        # define layout
        self.pack(expand=True, fill="both", side="right", padx=(10, 0), pady=0)
        self.pack_propagate(0)

    def open_view(self, view_name):
        view = self.views[view_name]
        view.pack(expand=True, fill="both")


if __name__ == "__main__":
    # setting
    title = "PyResarch"
    size = (800, 1000)
    sidebar_width = 150

    # initialize app
    app = App(title, size, sidebar_width)
    app.mainloop()
