import tkinter as tk
from customtkinter import CTkFrame, CTkLabel, CTkButton
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class Page1(CTkFrame):
    def __init__(self, root):
        CTkFrame.__init__(self, root)
        self.root = root
        self.frame = CTkFrame(root, width=200, height=100)
        # self.frame.pack(pady=20)

        self.label = CTkLabel(self.frame, text="This is page 1!")
        self.label.pack(padx=10, pady=10)

        self.button = CTkButton(
            self.frame, text="Click me!", command=lambda: print("You clicked me!")
        )
        self.button.pack(padx=10, pady=10)

        # Create a matplotlib figure and canvas
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot([1, 2, 3], [1, 2, 3])
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
