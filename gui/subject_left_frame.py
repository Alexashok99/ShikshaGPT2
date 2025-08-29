

# gui/subject_left_frame.py
import tkinter as tk
import ttkbootstrap as ttk
from logic.test import TestFunction as tst
from setting.settings import LBTN_WIDTH, SUBJECT_NAME
from logic.switch_logic import FrameSwitcher as logic

# नए frames import करो जो open होंगे button press पर
from gui.subject_frame import subject_chapter_frame
from gui.subject_frame import math_chapter_frame


class ReaderLeftFrameS(ttk.Frame):
    """
    📘 ReaderLeftFrameS
    यह class एक scrollable frame बनाती है जिसमें कई buttons होते हैं।  
    - Left side panel (जैसे sidebar menu) के लिए इस्तेमाल किया जा सकता है।  
    - Scrollbar + Mousewheel दोनों से scroll कर सकते हैं।  
    - Buttons के नाम external setting `SUBJECT_NAME` से लिए जाते हैं।  
    """

    def __init__(self, master, app):
        """
        Constructor: Frame initialize करता है और अंदर scrollable canvas बनाता है.
        
        Arguments:
        master : parent widget (main window/container)
        app    : main application का reference (future use)
        """
        super().__init__(master, bootstyle="info")
        self.pack(expand=True, fill="both")
        self.app = app  # 👈 app reference save karo

        # 🔹 Settings / Data
        self.text_data = SUBJECT_NAME  # Button labels list (from settings)

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

        # 🔹 Frame inside canvas (actual content here)
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # 🔹 Add buttons to the frame
        for index, item in enumerate(self.text_data):
            self.create_item(index, item).pack(expand=True, fill="x", pady=4, padx=10)

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

    def create_item(self, index, item):
        """
        एक row बनाता है जिसमें एक button होता है.
        
        Arguments:
        index : button का index (0 से शुरू)
        item  : button का text (string)
        """
        frame = ttk.Frame(self.scrollable_frame, bootstyle="light")

        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1, uniform="a")

        ttk.Button(
            frame,
            text=f"{item}",
            width=LBTN_WIDTH,
            command=lambda n=index: self.button_action(n, item),
            bootstyle="success",
        ).grid(row=0, column=0)

        return frame

    # ----------------------------------------------------------------------

    def button_action(self, n, button_text):
        """
        Button press पर action run करता है.
        
        Arguments:
        n : button का index (0 से शुरू)
        button_text : button का text
        """
        print(f"Button {n} clicked: {button_text}")
        
        # अलग-अलग buttons के लिए अलग-अलग frames open करो
        if n == 0:  # Mathematics button
            # logic.switch_both_frames(self.app, 
            #                        quiz_left_frame.QuizLeftFrame, 
            #                        quiz_right_frame.QuizRightFrame)
            logic.switch_right_frame_only(self.app, math_chapter_frame.MathChapterFrame, page_name="Math")
        
        elif n == 1:  # Reasoning button  
            logic.switch_right_frame_only(self.app, subject_chapter_frame.SubjectChapterFrame, page_name="Reasoning")
        
        elif n == 2:  # English button
            # यहाँ आप कोई और frames set कर सकते हो
            print("English button clicked - add your frames here")
            
        elif n == 9:  # Example: 10th button special case
            test = tst()
            test.test_method()
        
        else:
            # Default action for other buttons
            print(f"Button {n} ({button_text}) clicked!")