# gui/home_left_frame.py

import ttkbootstrap as ttk

from logic.switch_logic import FrameSwitcher as logic

from gui import subject_left_frame, reader_right_frame
from gui import quiz_left_frame, quiz_right_frame

from setting.settings import WIDTH

class HomeLeft(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master, bootstyle="secondary")

        ttk.Button(self, text="Read Notes", 
                   bootstyle="primary",
                   width=WIDTH,
                   command=lambda: logic.switch_frame(app, subject_left_frame.ReaderLeftFrameS, reader_right_frame.ReaderRightFrame, page_name="Notes")
                   ).pack(pady=10)

        ttk.Button(self, text="Quiz Time", 
                   bootstyle="success",
                   width=WIDTH,
                   command=lambda: logic.switch_frame(app, quiz_left_frame.QuizLeftFrame, quiz_right_frame.QuizRightFrame, page_name="Quizes")
                   ).pack(pady=10)

        ttk.Button(self, text="Switch Whole App", 
                   bootstyle="warning",
                   width=WIDTH,
                   command=lambda: logic.switch_frame(app, quiz_left_frame.QuizLeftFrame, reader_right_frame.ReaderRightFrame)
                   ).pack(pady=10)
        
        ttk.Button(self, text="Quit", 
                   bootstyle="danger",
                   width=WIDTH,
                   command=app.destroy
                   ).pack(pady=10)
