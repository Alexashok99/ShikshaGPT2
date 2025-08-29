import ttkbootstrap as ttk
from setting.settings import WIDTH
from logic.switch_logic import FrameSwitcher as logic

class QuizLeftFrame(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master, bootstyle="info")

        # 👇 app ko save kar lo instance variable me
        self.app = app

        # Functions की list
        actions = [
            self.chapter_quiz,
            self.subject_quiz,
            self.all_quiz,
            self.refresh_reader,
            self.search_text,
            self.change_quiz_heading,
            self.export_data,
            lambda: logic.go_back(self.app),   # 👈 Back Button,
            self.exit_app
        ]

        btn_name = [
            "Chapter Quiz",
            "Subject Quiz",
            "Section Quiz",
            "All Quiz",
            "Search Text",
            "Change Heading",
            "Export Data",
            "⬅ Back",
            "Exit"
        ]

        # Buttons बनाओ
        for i, (func, nm) in enumerate(zip(actions, btn_name), start=1):
            ttk.Button(
                self,
                text=f"{nm}",     # यहां आप चाहो तो सिर्फ nm रख सकते हो
                bootstyle="success",
                width=WIDTH,
                command=func
            ).pack(pady=5)

    # Example actions
    def chapter_quiz(self): print("Open Reader")
    def subject_quiz(self): print("Save Reader")
    def all_quiz(self): print("Close Reader")
    def refresh_reader(self): print("Refresh Reader")
    def search_text(self): print("Search Text")

    def change_quiz_heading(self):
        """Left button click → Right frame ke label ka text change karo"""
        if hasattr(self.app.right_frame, "quiz_heading"):  # check if exists
            self.app.right_frame.quiz_heading.config(text="✅ Heading Changed from Left Frame!")
        else:
            print("Right Frame me 'quiz_heading' label nahi mila.")

    def export_data(self): print("Export Data")
    def import_data(self): print("Import Data")
    def exit_app(self):
        self.app.destroy()