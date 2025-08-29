import ttkbootstrap as ttk

class QuizRightFrame(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master, bootstyle="light")

        self.quiz_heading = ttk.Label(self, text="📑 Quiz Content", font=("Arial", 16))
        self.quiz_heading.pack(pady=20)
        ttk.Button(self, text="Another Action", bootstyle="success").pack(pady=10)
