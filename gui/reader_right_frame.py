

# import tkinter as tk
# import ttkbootstrap as ttk
# from logic.test import TestFunction as tst
# from setting.settings import LBTN_WIDTH, GEOGRAPHY_CHAPTER_NAME


# class ReaderRightFrame(ttk.Frame):
#     """
#     📘 ReaderRightFrame
#     Scrollable frame जिसमें हर row में एक Button ("Read") और उसके right side एक Label (chapter name) होता है।
#     """

#     def __init__(self, master, app):
#         super().__init__(master, bootstyle="info")
#         self.pack(expand=True, fill="both")

#         self.app = app
#         self.chapters = GEOGRAPHY_CHAPTER_NAME   # Labels list (जैसे ["Chapter 1", "Chapter 2", ...])

#         # 🔹 Canvas for scrollable content
#         self.canvas = ttk.Canvas(self, background="white", highlightthickness=0)
#         self.canvas.pack(side="left", expand=True, fill="both")

#         # 🔹 Frame inside canvas
#         self.scrollable_frame = ttk.Frame(self.canvas)
#         self.window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

#         # 🔹 Add button + label rows
#         for index, chapter in enumerate(self.chapters, start=1):
#             self.create_row(index, chapter).pack(fill="x", pady=4, padx=10)

#         # 🔹 Scrollbar
#         self.scrollbar = ttk.Scrollbar(
#             self, orient="vertical", command=self.canvas.yview, bootstyle="round-success"
#         )
#         self.canvas.configure(yscrollcommand=self.scrollbar.set)
#         self.scrollbar.pack(side="right", fill="y")

#         # 🔹 Events
#         self.scrollable_frame.bind("<Configure>", self.update_scrollregion)
#         self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

#     # ----------------------------------------------------------------------

#     def update_scrollregion(self, event):
#         """Resize scroll region automatically based on content"""
#         self.canvas.configure(scrollregion=self.canvas.bbox("all"))
#         self.canvas.itemconfig(self.window, width=self.canvas.winfo_width())

#     def on_mousewheel(self, event):
#         """Enable mouse wheel scroll"""
#         self.canvas.yview_scroll(-int(event.delta / 60), "units")

#     # ----------------------------------------------------------------------

#     def create_row(self, index, chapter_name):
#         """
#         Row बनाता है जिसमें एक Button (Read) और एक Label (Chapter name) होता है।
#         """
#         row_frame = ttk.Frame(self.scrollable_frame, bootstyle="light")

#         # grid layout: Button (col=0), Label (col=1)
#         row_frame.columnconfigure(0, weight=0)   # Button fixed
#         row_frame.columnconfigure(1, weight=1)   # Label expands

#         # Button
#         ttk.Button(
#             row_frame,
#             text="Read",
#             width=LBTN_WIDTH,
#             bootstyle="success",
#             command=lambda i=index: self.button_action(i),
#         ).grid(row=0, column=0, padx=(0, 10), sticky="w")

#         # Label
#         ttk.Label(
#             row_frame,
#             text=chapter_name,
#             font=("Arial", 12),
#             bootstyle="secondary"
#         ).grid(row=0, column=1, sticky="w")

#         return row_frame

#     # ----------------------------------------------------------------------

#     def button_action(self, index):
#         """
#         Button press पर action run करता है।
#         """
#         if index == 9:  # Example: 9th button special
#             test = tst()
#             test.test_method()
#         else:
#             print(f"Read clicked for Chapter {index}")


# gui/home_right_frame.py

import ttkbootstrap as ttk

from logic.test import TestFunction as test

class ReaderRightFrame(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master, bootstyle="light")

        ttk.Label(self, text="🏠 Home Right Frame", font=("Arial", 16)).pack(pady=20)
        ttk.Button(self, text="Dummy Action", bootstyle="secondary-outline", command= lambda: test.test_method(app)).pack(pady=10)

