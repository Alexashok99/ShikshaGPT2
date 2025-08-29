import tkinter as tk
from views.chat_view import ChatView
from views.quiz_view import QuizView
from controllers.reader import ReaderController
from controllers.quiz import QuizController

class ChatReaderQuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ChatGPT-Style Hindi Reader + MCQ")
        self.geometry("900x700")
        self.configure(bg="#ECECEC")

        # Frames container
        self.container = tk.Frame(self, bg="#ECECEC")
        self.container.pack(fill="both", expand=True)

        # Init Views
        self.chat_view = ChatView(self.container, on_file_done=self.on_read_finish)
        self.chat_view.pack(fill="both", expand=True)

        self.quiz_view = None  # later

        # Controllers
        self.reader = ReaderController(
            file_path= r"data/solar_system.txt",
            on_line=self.chat_view.enqueue_line,
            on_done=self.on_read_finish
        )
        # Start reading immediately
        self.reader.start_stream()

    def on_read_finish(self):
        """Switch to quiz after reading ends"""
        if self.quiz_view is None:
            quiz_controller = QuizController(csv_path=r"data/questions.csv")
            self.quiz_view = QuizView(self.container, quiz_controller, on_quit=self.quit_to_close)
        self.chat_view.pack_forget()
        self.quiz_view.pack(fill="both", expand=True)

    def quit_to_close(self):
        self.destroy()
