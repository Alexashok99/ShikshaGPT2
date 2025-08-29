

import tkinter as tk
from queue import Queue

import tkinter as tk
from queue import Queue

class TextShowAreaFrame(tk.Frame):
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

    def clear(self):
        """Remove all chat bubbles"""
        for widget in self.chat_frame.winfo_children():
            widget.destroy()
        self.update_idletasks()
        self.canvas.yview_moveto(0.0)




# class TextShowAreaFrame(tk.Frame):
#     """
#     Chat-like view that renders lines as chat bubbles with typing effect.
#     Uses an internal queue to receive lines from ReaderController thread.
#     """
#     def __init__(self, parent, on_file_done=None):
#         super().__init__(parent, bg="#ECECEC")
#         self.on_file_done = on_file_done

#         # Scrollable Canvas
#         self.canvas = tk.Canvas(self, bg="#ECECEC", highlightthickness=0)
#         self.scroll_y = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
#         self.chat_frame = tk.Frame(self.canvas, bg="#ECECEC")

#         self.canvas.create_window((0, 0), window=self.chat_frame, anchor="nw")
#         self.canvas.configure(yscrollcommand=self.scroll_y.set)

#         self.canvas.pack(side="left", fill="both", expand=True)
#         self.scroll_y.pack(side="right", fill="y")

#         self.chat_frame.bind("<Configure>", lambda e: self.canvas.configure(
#             scrollregion=self.canvas.bbox("all")
#         ))

#         # Queue for incoming lines
#         self._line_q = Queue()

#         # Start polling queue
#         self.after(50, self._poll_queue)

#     # Called by controller thread (thread-safe)
#     def enqueue_line(self, line: str):
#         self._line_q.put(line)

#     def _poll_queue(self):
#         try:
#             while True:
#                 line = self._line_q.get_nowait()
#                 self._add_bubble_with_typing(line)
#         except Exception:
#             pass
#         self.after(50, self._poll_queue)

#     def _add_bubble_with_typing(self, text):
#         bubble = tk.Label(
#             self.chat_frame,
#             text="",
#             bg="white",
#             fg="black",
#             wraplength=700,
#             justify="left",
#             anchor="w",
#             padx=14, pady=10,
#             font=("Nirmala UI", 12),
#             bd=0
#         )
#         bubble.pack(anchor="w", pady=6, padx=10, fill="x")

#         # Typing effect via after()
#         self._type_char(bubble, text, idx=0)

#     def _type_char(self, widget, full_text, idx):
#         if idx <= len(full_text):
#             widget.config(text=full_text[:idx])
#             # autoscroll
#             self.update_idletasks()
#             self.canvas.yview_moveto(1.0)
#             self.after(15, self._type_char, widget, full_text, idx + 1)
#         # else: finished typing this bubble

#     # Optionally, let app know when file finished (controller also calls app)
#     def file_done(self):
#         if callable(self.on_file_done):
#             self.on_file_done()


# import tkinter as tk
# from queue import Queue

class ShowText(tk.Frame):
    """
    Chat-like view that renders lines as chat bubbles with typing effect.
    Uses an internal queue to receive lines from ReaderController thread.
    """
    def __init__(self, parent, on_file_done=None):
        super().__init__(parent, bg="#ECECEC")
        self.on_file_done = on_file_done
        self.pack(expand=True, fill="both")

        # Create main container
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Create a frame to hold canvas and scrollbar
        container = tk.Frame(self, bg="#ECECEC")
        container.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        # Scrollable Canvas
        self.canvas = tk.Canvas(container, bg="#ECECEC", highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        
        # Scrollbar
        self.scroll_y = tk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
        self.scroll_y.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.scroll_y.set)

        # Chat frame inside canvas
        self.chat_frame = tk.Frame(self.canvas, bg="#ECECEC")
        self.window = self.canvas.create_window((0, 0), window=self.chat_frame, anchor="nw")

        # Events
        self.chat_frame.bind("<Configure>", self.update_scrollregion)
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        self.canvas.bind("<Enter>", self.bind_mousewheel)
        self.canvas.bind("<Leave>", self.unbind_mousewheel)

        # Queue for incoming lines
        self._line_q = Queue()

        # Start polling queue
        self.after(50, self._poll_queue)

        self._jobs = []  # store after() ids

    def update_scrollregion(self, event):
        """Update scroll region when chat frame changes size"""
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

        # Update scroll region after adding new bubble
        self.update_idletasks()
        self.update_scrollregion(None)
        
        # Typing effect via after()
        self._type_char(bubble, text, idx=0)

    # def _type_char(self, widget, full_text, idx):
    #     if idx <= len(full_text):
    #         widget.config(text=full_text[:idx])
    #         # Auto-scroll to bottom
    #         self.canvas.yview_moveto(1.0)
    #         self.after(15, self._type_char, widget, full_text, idx + 1)
    #     # else: finished typing this bubble

    def _type_char(self, widget, full_text, idx):
        if not widget.winfo_exists():
            return  # Widget destroy ho chuka hai, skip karo

        if idx <= len(full_text):
            widget.config(text=full_text[:idx])
            self.canvas.yview_moveto(1.0)
            job_id = self.after(15, self._type_char, widget, full_text, idx + 1)
            self._jobs.append(job_id)


    def file_done(self):
        """Called when file reading is complete"""
        if callable(self.on_file_done):
            self.on_file_done()
            
    def clear_text(self):
        """Clear all text bubbles"""
        for widget in self.chat_frame.winfo_children():
            widget.destroy()
        self.update_scrollregion(None)

    # def clear(self):
    #     """Remove all chat bubbles"""
    #     for widget in self.chat_frame.winfo_children():
    #         widget.destroy()
    #     self.update_idletasks()
    #     self.canvas.yview_moveto(0.0)

    def clear(self):
        """Remove all chat bubbles and cancel pending jobs"""
        # Cancel pending after jobs
        for job in self._jobs:
            try:
                self.after_cancel(job)
            except:
                pass
        self._jobs.clear()

        # Destroy chat bubbles
        for widget in self.chat_frame.winfo_children():
            widget.destroy()

        self.update_idletasks()
        self.canvas.yview_moveto(0.0)
