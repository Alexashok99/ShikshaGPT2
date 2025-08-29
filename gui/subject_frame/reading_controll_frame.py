
# gui/home_left_frame.py

import ttkbootstrap as ttk
from logic.switch_logic import FrameSwitcher as logic
from logic.reader_controller import ReaderController
from gui import subject_left_frame, reader_right_frame
from gui import quiz_left_frame, quiz_right_frame
from setting.settings import WIDTH


def file_path(f_path):
    return f_path

class ReadingControllFrame(ttk.Frame):
    def __init__(self, master, app, path=None):
        super().__init__(master, bootstyle="secondary")
        self.app = app
        self.reader_controller = None
        # self.file_path = r"data/chapter_one_notes.txt"
        self.file_path = path
        
        # Create buttons
        ttk.Button(self, text="Load File", 
                   bootstyle="danger",
                   width=WIDTH,
                   command=self.load_file
                   ).pack(pady=10)

        ttk.Button(self, text="Play", 
                   bootstyle="primary",
                   width=WIDTH,
                   command=self.play
                   ).pack(pady=10)

        ttk.Button(self, text="Pause", 
                   bootstyle="warning",
                   width=WIDTH,
                   command=self.pause
                   ).pack(pady=10)
        
        ttk.Button(self, text="Resume", 
                   bootstyle="danger",
                   width=WIDTH,
                   command=self.resume
                   ).pack(pady=10)
        
        ttk.Button(self, text="Restart", 
                   bootstyle="primary",
                   width=WIDTH,
                   command=self.restart
                   ).pack(pady=10)

        ttk.Button(self, text="Back", 
                   bootstyle="warning",
                   width=WIDTH,
                   command=self.go_back
                   ).pack(pady=10)
        
        ttk.Button(self, text="Quit", 
                   bootstyle="danger",
                   width=WIDTH,
                   command=app.destroy
                   ).pack(pady=10)

    def load_file(self):
        """Load the text file and initialize the reader controller"""
        try:
            # Get the text display frame from the app
            text_frame = self.app.get_current_right_frame()
            
            if hasattr(text_frame, 'enqueue_line'):
                # Initialize reader controller
                self.reader_controller = ReaderController(
                    file_path=self.file_path,
                    display_callback=text_frame.enqueue_line,
                    completion_callback=text_frame.file_done if hasattr(text_frame, 'file_done') else None
                )
                print("File loaded successfully")
            else:
                print("Error: Current frame doesn't support text display")
                
        except Exception as e:
            print(f"Error loading file: {e}")

    def play(self):
        """Start reading the file"""
        if self.reader_controller:
            self.reader_controller.start_reading()
        else:
            print("Please load a file first")

    def pause(self):
        """Pause reading"""
        if self.reader_controller:
            self.reader_controller.pause_reading()
        else:
            print("No active reading session")

    def resume(self):
        """Resume reading"""
        if self.reader_controller:
            self.reader_controller.resume_reading()
        else:
            print("No active reading session")

    def restart(self):
        """Restart reading from beginning"""
        if self.reader_controller:
            self.reader_controller.restart_reading()
        else:
            print("Please load a file first")

    def go_back(self):
        """Go back to previous screen"""
        if self.reader_controller:
            self.reader_controller.stop_reading()
        logic.switch_frame(self.app, subject_left_frame.ReaderLeftFrameS, reader_right_frame.ReaderRightFrame)
