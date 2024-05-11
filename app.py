import customtkinter


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
        customtkinter.CTkLabel(self, bg_color="red").pack(expand=True, fill="both")

        self.pack(fill="y", side="left")
        self.pack_propagate(0)


class Main(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        customtkinter.CTkLabel(self, bg_color="green").pack(expand=True, fill="both")

        self.pack(expand=True, fill="both", padx=(10, 0), pady=0)
        self.pack_propagate(0)


if __name__ == "__main__":
    # setting
    title = "PyResarch"
    size = (800, 1000)
    sidebar_width = 300

    # initialize app
    app = App(title, size, sidebar_width)
    app.mainloop()
