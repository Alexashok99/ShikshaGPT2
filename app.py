# app.py

import tkinter as tk
import ttkbootstrap as ttk

from gui.topbar import TopBar
from gui.home_left_frame import HomeLeft
from gui.home_right_frame import HomeRight
from logic.switch_logic import FrameSwitcher as logic

from setting.settings import *


class MainApp(ttk.Window):
    def __init__(self):
        super().__init__(themename=THEME2)
        self.title(TITLE)
        self.geometry(f"{WSIZE[0]}x{WSIZE[1]}+{POS[0]}+{POS[1]}")
        self.iconbitmap(ICON)
        self.minsize(WSIZE[0], WSIZE[1])

        # Back history stack
        self.history = []
        self.forward_stack = []

        # Define home frames for navigation system
        self.home_left_class = HomeLeft
        self.home_right_class = HomeRight
        
        # self.top_bar_frame()
        # Topbar
        self.topbar = TopBar(self, self)
        self.topbar.pack(side="top", fill="x")

        # Main container
        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.container.grid_columnconfigure(0, weight=1, uniform="group1")
        self.container.grid_columnconfigure(1, weight=4, uniform="group1")
        self.container.grid_rowconfigure(0, weight=1)

        self.left_frame_container()
        self.rigt_frame_container()


    def rigt_frame_container(self):
        # Left + Right containers
        self.container_right = ttk.Frame(self.container, bootstyle="light")
        self.container_right.grid(row=0, column=1, sticky="nsew")

        self.right_frame = HomeRight(self.container_right, self)
        self.right_frame.pack(fill="both", expand=True)

    def left_frame_container(self):
        # Start with Home Screen
        self.container_left = ttk.Frame(self.container, bootstyle="dark")
        self.container_left.grid(row=0, column=0, sticky="nsew")

        self.left_frame = HomeLeft(self.container_left, self)
        self.left_frame.pack(fill="both", expand=True)

    #_________IMPORTANT_____________#
    def get_current_right_frame(self):
        """Get the current right frame instance"""
        return self.right_frame
    #-------------------------------#

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
