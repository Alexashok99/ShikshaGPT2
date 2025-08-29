# gui/home_right_frame.py

import ttkbootstrap as ttk

from logic.test import TestFunction as test

class HomeRight(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master, bootstyle="light")

        ttk.Label(self, text="🏠 Home Right Frame", font=("Arial", 16)).pack(pady=20)
        ttk.Button(self, text="Dummy Action", bootstyle="secondary-outline", command= lambda: test.test_method(app)).pack(pady=10)
