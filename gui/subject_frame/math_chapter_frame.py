
# gui/subject_frame/math_chapter_frame.py
import tkinter as tk
import ttkbootstrap as ttk
from functools import partial

from logic.test import TestFunction as tst
from setting.settings import LBTN_WIDTH, MATH_CHAPTER_NAME
from logic.switch_logic import FrameSwitcher as swf

from gui.subject_frame import text_show_frame
from gui.subject_frame import reading_controll_frame


class MathChapterFrame(ttk.Frame):
    """
    📘 ReaderRightFrame
    Scrollable frame जिसमें हर row में एक Button ("Read") और उसके right side एक Label (chapter name) होता है।
    """

    def __init__(self, master, app):
        super().__init__(master, bootstyle="info")
        self.pack(expand=True, fill="both")

        self.app = app
        self.chapters = MATH_CHAPTER_NAME   # Labels list (जैसे ["Chapter 1", "Chapter 2", ...])

        # Create main container with proper weight distribution
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # 🔹 Create a frame to hold canvas and scrollbar
        container = ttk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        # 🔹 Canvas for scrollable content
        self.canvas = ttk.Canvas(container, background="white", highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        
        # 🔹 Scrollbar
        self.scrollbar = ttk.Scrollbar(
            container, orient="vertical", command=self.canvas.yview, bootstyle="round-success"
        )
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # 🔹 Frame inside canvas
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # 🔹 Add button + label rows
        for index, chapter in enumerate(self.chapters, start=1):
            self.create_row(index, chapter).pack(fill="x", pady=4, padx=10)

        # 🔹 Events
        self.scrollable_frame.bind("<Configure>", self.update_scrollregion)
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        self.canvas.bind("<Enter>", self.bind_mousewheel)
        self.canvas.bind("<Leave>", self.unbind_mousewheel)
        
        # Update initial scroll region
        self.update_idletasks()
        self.update_scrollregion(None)

    # ----------------------------------------------------------------------

    def update_scrollregion(self, event):
        """Resize scroll region automatically based on content"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def on_canvas_configure(self, event):
        """Update the inner frame's width to match canvas"""
        self.canvas.itemconfig(self.window, width=event.width)
        
    def bind_mousewheel(self, event):
        """Bind mousewheel only when cursor is over this canvas"""
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)
        
    def unbind_mousewheel(self, event):
        """Unbind mousewheel when cursor leaves this canvas"""
        self.canvas.unbind_all("<MouseWheel>")
        
    def on_mousewheel(self, event):
        """Enable mouse wheel scroll"""
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # ----------------------------------------------------------------------

    def create_row(self, index, chapter_name):
        """
        Row बनाता है जिसमें एक Button (Read) और एक Label (Chapter name) होता है।
        """
        row_frame = ttk.Frame(self.scrollable_frame, bootstyle="light")

        # grid layout: Button (col=0), Label (col=1)
        row_frame.columnconfigure(0, weight=0)   # Button fixed
        row_frame.columnconfigure(1, weight=1)   # Label expands

        # Button
        ttk.Button(
            row_frame,
            text="Read",
            width=LBTN_WIDTH,
            bootstyle="success",
            command=lambda i=index: self.button_action(i),
        ).grid(row=0, column=0, padx=(0, 10), sticky="w")

        # Label
        ttk.Label(
            row_frame,
            text=chapter_name,
            font=("Arial", 12),
            bootstyle="secondary"
        ).grid(row=0, column=1, sticky="w")

        return row_frame

    # ----------------------------------------------------------------------

    def button_action(self, index):
        """
        Button press पर action run करता है।
        """
        chapter_files = {
        1: r"data/chapter_one_notes.txt",
        2: r"data/vs_hortcut.txt",
        3: r"data/git_notes.txt",
        4: r"data/readmen.txt",
        5: r"data/symbols.txt",
        6: r"data/text.txt",
        7: r"data/virtual_env.txt",
    }
        if index in chapter_files:
            file_path = chapter_files[index]

            # ✅ partial ensures correct params
            left_factory = partial(reading_controll_frame.ReadingControllFrame, path=file_path)

            swf.switch_both_frames(
                self.app,
                left_factory,   # अब ये (master, app) के साथ call होगा और path भी pass करेगा
                text_show_frame.ShowText,
                page_name=f"Chapter: {index}"
            )

        # if index == 1:
        #     swf.switch_both_frames(self.app, 
        #                            reading_controll_frame.ReadingControllFrame, 
        #                            text_show_frame.ShowText)
        elif index == 9:  # Example: 9th button special
            test = tst()
            test.test_method()
        else:
            print(f"Read clicked for Chapter {index}")


    def sent_args_to_reading_controll_frame(self):
        self.file_pt = r"data/chapter_one_notes.txt"
        swf.switch_both_frames(self.app, 
                               self.file_pt,
                                   reading_controll_frame.ReadingControllFrame, 
                                   text_show_frame.ShowText, page_name="Chapter 2")