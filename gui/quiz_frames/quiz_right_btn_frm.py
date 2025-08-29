

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class RightPanelFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Frame layout
        self.grid_rowconfigure(1, weight=1)   # middle area expandable
        self.grid_columnconfigure(0, weight=1)

        self.status_area()
        self.section_area()   # scrollable section
        self.bottom_buttons_area()

    # ---------- Status area ----------
    def status_area(self):
        frame = ttk.Frame(self)
        frame.grid(row=0, column=0, sticky=EW, pady=5)
        
        # Center the status area content
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(6, weight=1)

        status_data = [
            ("Answered", "success", 0),
            ("Marked", "secondary", 0),
            ("Not Visited", "info", 6),
            ("Marked and answered", "purple", 0),
            ("Not Answered", "danger", 4)
        ]

        for i, (text, style, count) in enumerate(status_data):
            row = ttk.Frame(frame)
            row.grid(row=i, column=1, sticky=W, pady=2)

            lbl_count = ttk.Label(row, text=str(count), bootstyle=f"{style}-inverse")
            lbl_count.pack(side=LEFT, padx=5)

            lbl_text = ttk.Label(row, text=text, font=("Helvetica", 10))
            lbl_text.pack(side=LEFT, padx=5)

    # ---------- Section & Questions (scrollable) ----------
    def section_area(self):
        outer_frame = ttk.Frame(self)
        outer_frame.grid(row=1, column=0, sticky=NSEW, pady=5, padx=2)
        # outer_frame.grid_rowconfigure(0, weight=1)
        outer_frame.grid_columnconfigure(0, weight=1) # Center the content

        section_lbl = ttk.Label(
            outer_frame, text="SECTION : टेस्ट",
            font=("Helvetica", 10, "bold"), bootstyle="inverse-info"
        )
        section_lbl.grid(row=0, column=0, sticky=EW, pady=2)

        # Canvas + Scrollbar
        canvas_frame = ttk.Frame(outer_frame)
        canvas_frame.grid(row=1, column=0, sticky=NSEW)
        canvas_frame.grid_rowconfigure(0, weight=1)
        canvas_frame.grid_columnconfigure(0, weight=1)

        self.canvas = tk.Canvas(canvas_frame, borderwidth=0, highlightthickness=0)
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=self.canvas.yview)
        self.scroll_frame = ttk.Frame(self.canvas)  # inner frame

        self.scroll_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.grid(row=0, column=0, sticky=NSEW)
        scrollbar.grid(row=0, column=1, sticky=NS)
        self.canvas.grid(row=0, column=0, sticky=NSEW)
        scrollbar.grid(row=0, column=1, sticky=NS)

        # MouseWheel binding (only on canvas area)
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)     # Windows
        self.canvas.bind("<Button-4>", self._on_mousewheel)       # Linux
        self.canvas.bind("<Button-5>", self._on_mousewheel)

        # Add question buttons in scrollable frame
        self.q_buttons = []
        for i in range(1, 51):  # ज्यादा number for testing
            style = "secondary-outline"
            if i in [1, 2, 3, 4]:
                style = "danger"  # red filled
            elif i == 5:
                style = "secondary-outline"

            btn = ttk.Button(self.scroll_frame, text=str(i), width=3, bootstyle=style)
            btn.grid(row=(i-1)//5, column=(i-1)%5, padx=5, pady=5)
            self.q_buttons.append(btn)

    def _on_mousewheel(self, event):
        """ Mousewheel scrolling fix (cross-platform) """
        if event.num == 4:      # Linux scroll up
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:    # Linux scroll down
            self.canvas.yview_scroll(1, "units")
        else:                   # Windows / Mac
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    # # ---------- Bottom Buttons ----------
    def bottom_buttons_area(self):
        frame = ttk.Frame(self)
        frame.grid(row=2, column=0, sticky=EW, pady=5)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(4, weight=1)

        btn_container = ttk.Frame(frame)
        btn_container.grid(row=0, column=1, columnspan=3, sticky=NSEW)

        # btn1 = ttk.Button(btn_container, text="Question Paper", bootstyle="info-outline")
        btn2 = ttk.Button(btn_container, text="Instructions", bootstyle="info-outline")
        btn3 = ttk.Button(btn_container, text="Submit Test", bootstyle="success")

        # btn1.pack(side=LEFT, expand=True, padx=5, pady=5)
        btn2.pack(side=LEFT, expand=True, padx=5, pady=5)
        btn3.pack(side=LEFT, expand=True, padx=5, pady=5)


if __name__ == "__main__":
    app = ttk.Window(themename="flatly")
    app.title("QUIZ APP")
    app.geometry("300x600")

    quiz = RightPanelFrame(app)
    quiz.pack(fill="both", expand=True, padx=10, pady=10)
    app.mainloop()
