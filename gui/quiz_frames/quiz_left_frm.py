


import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class QuizAttemptFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, bootstyle="light")

        # Grid Layout
        self.grid_columnconfigure(0, weight=1, uniform="group1")
        self.grid_rowconfigure(0, weight=3, uniform="group2")
        self.grid_rowconfigure(1, weight=3, uniform="group2")
        self.grid_rowconfigure(2, weight=26, uniform="group2")
        self.grid_rowconfigure(3, weight=3, uniform="group2")
        self.grid_propagate(NO)

        self.tob_view_area()
        self.second_tob_view_area()
        self.question_options_view_area()
        self.bottom_view_area()


    def tob_view_area(self):
        self.top_area_frame = ttk.Frame(self, bootstyle="light")
        self.top_area_frame.grid(row=0, column=0, sticky=NSEW)

        q_lbl = ttk.Label(self.top_area_frame, text="SECTIONS", anchor="w", bootstyle= "secondary" ,font=("Helvetica", 11, "bold"))
        q_lbl.pack(side=LEFT, padx=10, pady=5)

        time_lbl = ttk.Label(self.top_area_frame, text="Test", anchor="e", 
                             bootstyle="inverse-primary", font=("Helvetica", 11, "bold"))
        time_lbl.pack(side=LEFT, padx=10, pady=5)

        time_lbl = ttk.Label(self.top_area_frame, text="Time Left: 00:05:53", anchor="e", 
                             bootstyle="danger", font=("Helvetica", 11, "bold"))
        time_lbl.pack(side=RIGHT, padx=10, pady=5)



    def second_tob_view_area(self):
        self.top_second_area_frame = ttk.Frame(self, bootstyle="light")
        self.top_second_area_frame.grid(row=1, column=0, sticky=NSEW)


        q_lbl = ttk.Label(self.top_second_area_frame, text="Question No. 5", anchor="w", font=("Helvetica", 11, "bold"))
        q_lbl.pack(side=LEFT, padx=10, pady=5)

        time_lbl = ttk.Label(self.top_second_area_frame, text="Time: 00:53", anchor="e", 
                             bootstyle="info", font=("Helvetica", 11, "bold"))
        time_lbl.pack(side=LEFT, padx=40, pady=5)

        self.btn_pause_quiz = ttk.Button(self.top_second_area_frame, text="Pause", bootstyle = "danger-outline" )
        self.btn_pause_quiz.pack(side=RIGHT, padx=10, pady=5)



    # ---------- Question + Options with Scrollbar ----------
    def question_options_view_area(self):
        frame = ttk.Frame(self, bootstyle="light")
        frame.grid(row=2, column=0, sticky=NSEW)

        # Create canvas + scrollbar
        canvas = tk.Canvas(frame, highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scroll_frame = ttk.Frame(canvas)

        # Configure canvas window
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Make scrollregion update
        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        scroll_frame.bind("<Configure>", on_configure)

        # -------- Add Question --------
        question = "1/2 of 16/5 + 1/8 of 24/9 × 18/12 - 5/8 का मान क्या होगा?"
        q_lbl = ttk.Label(scroll_frame, text=question, wraplength=700, font=("Helvetica", 12))
        q_lbl.pack(anchor="w", padx=15, pady=10)

        # # -------- Add Options --------
        # self.answer_var = tk.StringVar()
        # options = ["51/40", "68/39", "59/40", "61/50"]

        # for opt in options:
        #     r = ttk.Radiobutton(scroll_frame, text=opt, value=opt,
        #                         variable=self.answer_var, bootstyle="info-toolbutton")
        #     r.pack(anchor="w", padx=30, pady=3)

        # -------- Add Options --------
        self.answer_var = tk.StringVar()
        options = ["51/40", "68/39", "59/40", "61/50"]

        for opt in options:
            r = ttk.Radiobutton(scroll_frame, text=opt, value=opt, 
                                variable=self.answer_var)
            r.pack(anchor="w", padx=30, pady=3)

    # ---------- Bottom Bar (Buttons) ----------
    def bottom_view_area(self):
        frame = ttk.Frame(self, bootstyle="light")
        frame.grid(row=3, column=0, sticky=NSEW)

        btn1 = ttk.Button(frame, text="Mark for Review & Next", bootstyle="secondary-outline")
        btn2 = ttk.Button(frame, text="Clear Response", bootstyle="danger-outline")
        btn3 = ttk.Button(frame, text="Save & Next", bootstyle="success")

        btn1.pack(side=LEFT, padx=10, pady=5)
        btn2.pack(side=LEFT, padx=10, pady=5)
        btn3.pack(side=RIGHT, padx=10, pady=5)


if __name__ == "__main__":
    app = ttk.Window(themename="flatly")
    app.title("QUIZ APP")
    app.geometry("800x500")

    quiz = QuizAttemptFrame(app)
    quiz.pack(fill="both", expand=True, padx=10, pady=10)
    app.mainloop()
