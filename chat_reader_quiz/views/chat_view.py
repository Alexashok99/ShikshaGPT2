import tkinter as tk
from queue import Queue

class ChatView(tk.Frame):
    """
    Chat-like view that renders lines as chat bubbles with typing effect.
    Uses an internal queue to receive lines from ReaderController thread.
    """
    def __init__(self, parent, on_file_done=None):
        super().__init__(parent, bg="#ECECEC")
        self.on_file_done = on_file_done

        # Scrollable Canvas
        self.canvas = tk.Canvas(self, bg="#ECECEC", highlightthickness=0)
        self.scroll_y = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.chat_frame = tk.Frame(self.canvas, bg="#ECECEC")

        self.canvas.create_window((0, 0), window=self.chat_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scroll_y.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scroll_y.pack(side="right", fill="y")

        self.chat_frame.bind("<Configure>", lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
        ))

        # Queue for incoming lines
        self._line_q = Queue()

        # Start polling queue
        self.after(50, self._poll_queue)

    # Called by controller thread (thread-safe)
    def enqueue_line(self, line: str):
        self._line_q.put(line)

    def _poll_queue(self):
        try:
            while True:
                line = self._line_q.get_nowait()
                self._add_bubble_with_typing(line)
        except Exception:
            pass
        self.after(50, self._poll_queue)

    def _add_bubble_with_typing(self, text):
        bubble = tk.Label(
            self.chat_frame,
            text="",
            bg="white",
            fg="black",
            wraplength=700,
            justify="left",
            anchor="w",
            padx=14, pady=10,
            font=("Nirmala UI", 12),
            bd=0
        )
        bubble.pack(anchor="w", pady=6, padx=10, fill="x")

        # Typing effect via after()
        self._type_char(bubble, text, idx=0)

    def _type_char(self, widget, full_text, idx):
        if idx <= len(full_text):
            widget.config(text=full_text[:idx])
            # autoscroll
            self.update_idletasks()
            self.canvas.yview_moveto(1.0)
            self.after(15, self._type_char, widget, full_text, idx + 1)
        # else: finished typing this bubble

    # Optionally, let app know when file finished (controller also calls app)
    def file_done(self):
        if callable(self.on_file_done):
            self.on_file_done()
