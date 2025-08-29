import tkinter as tk
from tkinter import messagebox

class QuizView(tk.Frame):
    """
    Simple MCQ UI: shows one question at a time with 4 options.
    """
    def __init__(self, parent, controller, on_quit=None):
        super().__init__(parent, bg="#F7F7F7")
        self.controller = controller
        self.on_quit = on_quit

        self.title = tk.Label(self, text="📝 MCQ Quiz", font=("Nirmala UI", 18, "bold"), bg="#F7F7F7")
        self.title.pack(pady=(20,10))

        self.q_label = tk.Label(self, text="", font=("Nirmala UI", 14), bg="#FFFFFF", anchor="w", justify="left",
                                wraplength=800, padx=14, pady=12, bd=0, relief="solid")
        self.q_label.pack(padx=20, pady=10, fill="x")

        self.var = tk.IntVar(value=-1)
        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self, text="", variable=self.var, value=i,
                                font=("Nirmala UI", 12), anchor="w", justify="left",
                                bg="#F7F7F7")
            rb.pack(padx=30, pady=6, fill="x")
            self.option_buttons.append(rb)

        btn_frame = tk.Frame(self, bg="#F7F7F7")
        btn_frame.pack(pady=20)

        self.submit_btn = tk.Button(btn_frame, text="Submit", command=self.on_submit, font=("Nirmala UI", 12))
        self.submit_btn.grid(row=0, column=0, padx=10)

        self.next_btn = tk.Button(btn_frame, text="Next ▶", command=self.next_question, state="disabled", font=("Nirmala UI", 12))
        self.next_btn.grid(row=0, column=1, padx=10)

        self.status = tk.Label(self, text="", font=("Nirmala UI", 12), bg="#F7F7F7")
        self.status.pack()

        self.quit_btn = tk.Button(self, text="Quit", command=self._quit, font=("Nirmala UI", 11))
        self.quit_btn.pack(pady=(10, 20))

        self.load_question()

    def load_question(self):
        q = self.controller.current()
        if q is None:
            score, total = self.controller.result()
            messagebox.showinfo("Result", f"आपका स्कोर: {score}/{total}")
            self._quit()
            return

        self.q_label.config(text=q.text)
        for i, opt in enumerate(q.options):
            self.option_buttons[i].config(text=f"{chr(65+i)}. {opt}")
        self.var.set(-1)
        self.status.config(text="")
        self.submit_btn.config(state="normal")
        self.next_btn.config(state="disabled")

    def on_submit(self):
        sel = self.var.get()
        if sel == -1:
            self.status.config(text="कृपया एक विकल्प चुनें।")
            return
        correct, correct_idx = self.controller.submit(sel)
        if correct:
            self.status.config(text="✅ सही उत्तर!")
        else:
            self.status.config(text=f"❌ गलत। सही उत्तर: {chr(65+correct_idx)}")
        self.submit_btn.config(state="disabled")
        self.next_btn.config(state="normal")

    def next_question(self):
        self.load_question()

    def _quit(self):
        if callable(self.on_quit):
            self.on_quit()
