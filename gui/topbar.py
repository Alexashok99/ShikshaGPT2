
#gui/topbar.py
import ttkbootstrap as ttk
from tkinter import StringVar
from logic.switch_logic import FrameSwitcher as fsl


class TopBar(ttk.Frame):
    def __init__(self, master, main_gui, *args, **kwargs):
        super().__init__(master, bootstyle="secondary", *args, **kwargs)
        self.main_gui = main_gui

        # Buttons
        self.back_btn = ttk.Button(self, text="⬅ Back", bootstyle="info-outline",
                                   command=lambda: fsl.go_back(main_gui))
        self.back_btn.pack(side="left", padx=5, pady=5)

        self.forward_btn = ttk.Button(self, text="➡ Forward", bootstyle="info-outline",
                                      command=lambda: fsl.go_forward(main_gui))
        self.forward_btn.pack(side="left", padx=5, pady=5)

        self.home_btn = ttk.Button(self, text="🏠 Home", bootstyle="info-outline",
                                   command=lambda: fsl.go_home(main_gui))
        self.home_btn.pack(side="left", padx=5, pady=5)

        # Label for showing current frame name
        self.frame_name_var = StringVar(value="Home")
        self.frame_label = ttk.Label(self, textvariable=self.frame_name_var,
                                     bootstyle="inverse-secondary", font=("Arial", 12, "bold"))
        self.frame_label.pack(side="left", padx=10)

        # Search bar
        self.search_btn = ttk.Button(self, text="🔍 Search", bootstyle="info-outline")
        self.search_btn.pack(side="right", padx=10, pady=5)

        self.search_entry = ttk.Entry(self)
        self.search_entry.pack(side="right", padx=10, pady=5)

    def update_frame_name(self, name: str):
        """Update label when frame changes"""
        self.frame_name_var.set(name)
