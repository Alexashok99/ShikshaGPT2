"""

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x300")

# ---- Left panel ----
left_canvas = tk.Canvas(root, background="lightblue")
left_canvas.pack(side="left", fill="both", expand=True)

left_frame = ttk.Frame(left_canvas)
left_window = left_canvas.create_window((0,0), window=left_frame, anchor="nw")

left_scroll = ttk.Scrollbar(root, orient="vertical", command=left_canvas.yview)
left_canvas.configure(yscrollcommand=left_scroll.set)
left_scroll.pack(side="left", fill="y")

# ---- Right panel ----
right_canvas = tk.Canvas(root, background="lightyellow")
right_canvas.pack(side="left", fill="both", expand=True)

right_frame = ttk.Frame(right_canvas)
right_window = right_canvas.create_window((0,0), window=right_frame, anchor="nw")

right_scroll = ttk.Scrollbar(root, orient="vertical", command=right_canvas.yview)
right_canvas.configure(yscrollcommand=right_scroll.set)
right_scroll.pack(side="right", fill="y")

# Add widgets to left frame
for i in range(60):
    ttk.Button(left_frame, text=f"Left Btn {i+1}").pack(pady=2)

# Add widgets to right frame
for i in range(60):
    ttk.Label(right_frame, text=f"Right Label {i+1}").pack(pady=2)

# Update scrollregions
def update_left(event):
    left_canvas.configure(scrollregion=left_canvas.bbox("all"))

def update_right(event):
    right_canvas.configure(scrollregion=right_canvas.bbox("all"))

left_frame.bind("<Configure>", update_left)
right_frame.bind("<Configure>", update_right)

# -------- Mouse Wheel Bind --------
def _on_mousewheel_left(event):
    left_canvas.yview_scroll(-int(event.delta / 60), "units")

def _on_mousewheel_right(event):
    right_canvas.yview_scroll(-int(event.delta / 60), "units")

# Bind when mouse enters each panel
left_canvas.bind("<Enter>", lambda e: root.bind_all("<MouseWheel>", _on_mousewheel_left))
right_canvas.bind("<Enter>", lambda e: root.bind_all("<MouseWheel>", _on_mousewheel_right))

# Unbind when mouse leaves
left_canvas.bind("<Leave>", lambda e: root.unbind_all("<MouseWheel>"))
right_canvas.bind("<Leave>", lambda e: root.unbind_all("<MouseWheel>"))

root.mainloop()

"""

# # gui/subject_left_frame.py
# import tkinter as tk
# import ttkbootstrap as ttk
# from logic.test import TestFunction as tst
# from setting.settings import LBTN_WIDTH, SUBJECT_NAME


# class ReaderLeftFrameS(ttk.Frame):
#     """
#     📘 ReaderLeftFrameS
#     यह class एक scrollable frame बनाती है जिसमें कई buttons होते हैं।  
#     - Left side panel (जैसे sidebar menu) के लिए इस्तेमाल किया जा सकता है।  
#     - Scrollbar + Mousewheel दोनों से scroll कर सकते हैं।  
#     - Buttons के नाम external setting `SUBJECT_NAME` से लिए जाते हैं।  
#     """

#     def __init__(self, master, app):
#         """
#         Constructor: Frame initialize करता है और अंदर scrollable canvas बनाता है।
        
#         Arguments:
#         master : parent widget (main window/container)
#         app    : main application का reference (future use)
#         """
#         super().__init__(master, bootstyle="info")
#         self.pack(expand=True, fill="both")

#         # 🔹 Settings / Data
#         self.item_height = 60                          # Approx height per item (used for scroll calculations)
#         self.text_data = SUBJECT_NAME         # Button labels list (from settings)
#         self.item_number = len(self.text_data)         # Total button count
#         self.list_height = self.item_number * self.item_height

#         # 🔹 Canvas for scrollable content
#         self.canvas = tk.Canvas(
#             self,
#             background="white",
#             scrollregion=(0, 0, self.winfo_width(), self.list_height),
#             highlightthickness=0,
#         )
#         self.canvas.pack(side="left", expand=True, fill="both")

#         # 🔹 Frame inside canvas (actual content here)
#         self.frame = ttk.Frame(self.canvas)

#         # 🔹 Add buttons to the frame
#         for index, item in enumerate(self.text_data):
#             self.create_item(index, item).pack(
#                 expand=True, fill="x", pady=4, padx=10
#             )

#         # 🔹 Vertical scrollbar
#         self.scrollbar = ttk.Scrollbar(
#             self, orient="vertical", command=self.canvas.yview, bootstyle="round-success"
#         )
#         self.canvas.configure(yscrollcommand=self.scrollbar.set)
#         self.scrollbar.pack(side="right", fill="y")

#         # 🔹 Events binding
#         self.canvas.bind_all(
#             "<MouseWheel>",
#             lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"),
#         )
#         self.bind("<Configure>", self.update_size)

#     # ----------------------------------------------------------------------

#     def update_size(self, event):
#         """
#         जब frame resize होता है, तब scroll region update करता है और scrollbar
#         दिखाता/छुपाता है।
#         """
#         if self.list_height >= self.winfo_height():
#             height = self.list_height
#             self.canvas.bind_all(
#                 "<MouseWheel>",
#                 lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"),
#             )
#             self.scrollbar.pack(side="right", fill="y")
#         else:
#             height = self.winfo_height()
#             self.canvas.unbind_all("<MouseWheel>")
#             self.scrollbar.pack_forget()

#         # Scrollable frame को canvas के अंदर draw करना
#         self.canvas.create_window(
#             (0, 0),
#             window=self.frame,
#             anchor="nw",
#             width=self.winfo_width(),
#             height=height,
#         )

#     # ----------------------------------------------------------------------

#     def create_item(self, index, item):
#         """
#         एक row बनाता है जिसमें एक button होता है।
        
#         Arguments:
#         index : button का index (0 से शुरू)
#         item  : button का text (string)
#         """
#         frame = ttk.Frame(self.frame, bootstyle="light")

#         frame.rowconfigure(0, weight=1)
#         frame.columnconfigure(0, weight=1, uniform="a")

#         ttk.Button(
#             frame,
#             text=f"{item}",
#             width=LBTN_WIDTH,
#             command=lambda n=index: self.button_action(n),
#             bootstyle="success",
#         ).grid(row=0, column=0)

#         return frame

#     # ----------------------------------------------------------------------

#     def button_action(self, n):
#         """
#         Button press पर action run करता है।
        
#         Arguments:
#         n : button का index (0 से शुरू)
#         """
#         if n == 9:  # Example: 10th button (index 9) special case
#             test = tst()
#             test.test_method()
#         else:
#             print(f"Button {n} clicked!")  # Default action



# # # gui/subject_left_frame.py
# # import tkinter as tk
# # import ttkbootstrap as ttk
# # from logic.test import TestFunction as tst
# # from setting.settings import LBTN_WIDTH, SUBJECT_NAME


# # class ReaderLeftFrameS(ttk.Frame):
# #     def __init__(self, master, app):
# #         super().__init__(master, bootstyle="info")
# #         self.pack(expand=True, fill="both")

# #         # Data
# #         self.text_data = SUBJECT_NAME

# #         # Canvas
# #         self.canvas = tk.Canvas(self, background="white", highlightthickness=0)
# #         self.canvas.pack(side="left", expand=True, fill="both")

# #         # Frame inside canvas
# #         self.frame = ttk.Frame(self.canvas)
# #         self.window = self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

# #         # Add items
# #         for index, item in enumerate(self.text_data):
# #             self.create_item(index, item).pack(expand=True, fill="x", pady=4, padx=10)

# #         # Scrollbar
# #         self.scrollbar = ttk.Scrollbar(
# #             self, orient="vertical", command=self.canvas.yview, bootstyle="round-success"
# #         )
# #         self.canvas.configure(yscrollcommand=self.scrollbar.set)
# #         self.scrollbar.pack(side="right", fill="y")

# #         # Events
# #         self.frame.bind("<Configure>", self.update_size)

# #         # Mousewheel bind
# #         self.canvas.bind("<Enter>", lambda e: self.bind_all("<MouseWheel>", self._on_mousewheel))
# #         self.canvas.bind("<Leave>", lambda e: self.unbind_all("<MouseWheel>"))

# #     def update_size(self, event):
# #         """Update scrollregion when frame resizes"""
# #         self.canvas.configure(scrollregion=self.canvas.bbox("all"))
# #         self.canvas.itemconfig(self.window, width=self.canvas.winfo_width())

# #     def create_item(self, index, item):
# #         """Create one row (button only)"""
# #         frame = ttk.Frame(self.frame, bootstyle="light")

# #         ttk.Button(
# #             frame,
# #             text=f"{item}",
# #             width=LBTN_WIDTH,
# #             command=lambda n=index: self.button_action(n),
# #             bootstyle="success",
# #         ).grid(row=0, column=0)

# #         return frame

# #     def button_action(self, n):
# #         """Button actions"""
# #         if n == 9:  # Example: 10th button special
# #             test = tst()
# #             test.test_method()
# #         else:
# #             print(f"Button {n} clicked!")

# #     def _on_mousewheel(self, event):
# #         """Mouse wheel scroll"""
# #         self.canvas.yview_scroll(-int(event.delta / 60), "units")






# # logic/switch_logic.py

# class FrameSwitcher:

#     def switch_frame(main_gui, left_class, right_class):
#         # Save history for back
#         main_gui.history.append((main_gui.left_frame.__class__, main_gui.right_frame.__class__))

#         # Destroy old frames
#         main_gui.left_frame.destroy()
#         main_gui.right_frame.destroy()

#         # Create new frames
#         main_gui.left_frame = left_class(main_gui.container_left, main_gui)
#         main_gui.left_frame.pack(fill="both", expand=True)

#         main_gui.right_frame = right_class(main_gui.container_right, main_gui)
#         main_gui.right_frame.pack(fill="both", expand=True)

#     def go_back(main_gui):
#         if main_gui.history:
#             last_left, last_right = main_gui.history.pop()

#             # Destroy current frames
#             main_gui.left_frame.destroy()
#             main_gui.right_frame.destroy()

#             # Restore previous frames
#             main_gui.left_frame = last_left(main_gui.container_left, main_gui)
#             main_gui.left_frame.pack(fill="both", expand=True)

#             main_gui.right_frame = last_right(main_gui.container_right, main_gui)
#             main_gui.right_frame.pack(fill="both", expand=True)

# gui/reader_right_frame
# import ttkbootstrap as ttk
# import time
# class ReaderRightFrame(ttk.Frame):
#     def __init__(self, master, app):
#         super().__init__(master, bootstyle="light")

#         # पहले label बनाओ, फिर pack() अलग से करो
#         self.heading = ttk.Label(self, text="📄 Notes Contents", font=("Arial", 16))
#         self.heading.pack(pady=20)

#         ttk.Button(self, text="Do Action 1", bootstyle="success-outline", command=lambda: self.change_text(1)).pack(pady=10)
#         ttk.Button(self, text="Do Action 2", bootstyle="warning-outline", command= lambda: self.change_text(2)).pack(pady=10)

#     def change_text(self, num):
#         if num == 1:
#             self.heading.config(text="✅ Action 1 Executed!")
#             self.update()
#             time.sleep(2)
#             self.heading.config(text="📄 Notes Contents")
#         elif num == 2:
#             self.heading.config(text="✅ Action 2 Executed!")
#             self.update()
#             time.sleep(2)
#             self.heading.config(text="📄 Notes Contents")






# # gui/reader_right_frame.py
# import tkinter as tk
# import ttkbootstrap as ttk
# from setting.settings import RBTN_WIDTH, SUBJECT_NAME


# class ReaderRightFrame(ttk.Frame):
#     def __init__(self, master, app):
#         super().__init__(master, bootstyle="secondary")
#         self.pack(expand=True, fill="both")

#         # Data
#         self.text_data = SUBJECT_NAME

#         # Canvas
#         self.canvas = tk.Canvas(self, background="white", highlightthickness=0)
#         self.canvas.pack(side="left", expand=True, fill="both")

#         # Frame inside canvas
#         self.frame = ttk.Frame(self.canvas)
#         self.window = self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

#         # Add items
#         for index, item in enumerate(self.text_data):
#             self.create_item(index, item).pack(expand=True, fill="x", pady=4, padx=10)

#         # Scrollbar
#         self.scrollbar = ttk.Scrollbar(
#             self, orient="vertical", command=self.canvas.yview, bootstyle="round-secondary"
#         )
#         self.canvas.configure(yscrollcommand=self.scrollbar.set)
#         self.scrollbar.pack(side="right", fill="y")

#         # Events
#         self.frame.bind("<Configure>", self.update_size)

#         # Mousewheel bind
#         self.canvas.bind("<Enter>", lambda e: self.bind_all("<MouseWheel>", self._on_mousewheel))
#         self.canvas.bind("<Leave>", lambda e: self.unbind_all("<MouseWheel>"))

#     def update_size(self, event):
#         """Update scrollregion when frame resizes"""
#         self.canvas.configure(scrollregion=self.canvas.bbox("all"))
#         self.canvas.itemconfig(self.window, width=self.canvas.winfo_width())

#     def create_item(self, index, item):
#         """Create one row (Button + Label)"""
#         frame = ttk.Frame(self.frame, bootstyle="light")

#         ttk.Button(frame, text="Read", width=RBTN_WIDTH, bootstyle="success").grid(row=0, column=0, padx=5)
#         ttk.Label(frame, text=f"{item}", anchor="w").grid(row=0, column=1, sticky="w")

#         return frame

#     def _on_mousewheel(self, event):
#         """Mouse wheel scroll"""
#         self.canvas.yview_scroll(-int(event.delta / 60), "units")








# import tkinter as tk
# import ttkbootstrap as ttk
# from logic.test import TestFunction as tst
# from setting.settings import LBTN_WIDTH, GEOGRAPHY_CHAPTER_NAME
# from logic.switch_logic import FrameSwitcher as swf

# from gui.subject_frame import text_show_frame
# from gui.subject_frame import reading_controll_frame


# class SubjectChapterFrame(ttk.Frame):
#     """
#     📘 ReaderRightFrame
#     Scrollable frame जिसमें हर row में एक Button ("Read") और उसके right side एक Label (chapter name) होता है।
#     """

#     def __init__(self, master, app):
#         super().__init__(master, bootstyle="info")
#         self.pack(expand=True, fill="both")

#         self.app = app
#         self.chapters = GEOGRAPHY_CHAPTER_NAME   # Labels list (जैसे ["Chapter 1", "Chapter 2", ...])

#         # Create main container with proper weight distribution
#         self.grid_rowconfigure(0, weight=1)
#         self.grid_columnconfigure(0, weight=1)
        
#         # 🔹 Create a frame to hold canvas and scrollbar
#         container = ttk.Frame(self)
#         container.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
        
#         # 🔹 Canvas for scrollable content
#         self.canvas = ttk.Canvas(container, background="white", highlightthickness=0)
#         self.canvas.grid(row=0, column=0, sticky="nsew")
        
#         # 🔹 Scrollbar
#         self.scrollbar = ttk.Scrollbar(
#             container, orient="vertical", command=self.canvas.yview, bootstyle="round-success"
#         )
#         self.scrollbar.grid(row=0, column=1, sticky="ns")
#         self.canvas.configure(yscrollcommand=self.scrollbar.set)

#         # 🔹 Frame inside canvas
#         self.scrollable_frame = ttk.Frame(self.canvas)
#         self.window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

#         # 🔹 Add button + label rows
#         for index, chapter in enumerate(self.chapters, start=1):
#             self.create_row(index, chapter).pack(fill="x", pady=4, padx=10)

#         # 🔹 Events
#         self.scrollable_frame.bind("<Configure>", self.update_scrollregion)
#         self.canvas.bind("<Configure>", self.on_canvas_configure)
#         self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)
        
#         # Update initial scroll region
#         self.update_idletasks()
#         self.update_scrollregion(None)

#     # ----------------------------------------------------------------------

#     def update_scrollregion(self, event):
#         """Resize scroll region automatically based on content"""
#         self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
#     def on_canvas_configure(self, event):
#         """Update the inner frame's width to match canvas"""
#         self.canvas.itemconfig(self.window, width=event.width)
        
#     def on_mousewheel(self, event):
#         """Enable mouse wheel scroll"""
#         self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

#     # ----------------------------------------------------------------------

#     def create_row(self, index, chapter_name):
#         """
#         Row बनाता है जिसमें एक Button (Read) और एक Label (Chapter name) होता है।
#         """
#         row_frame = ttk.Frame(self.scrollable_frame, bootstyle="light")

#         # grid layout: Button (col=0), Label (col=1)
#         row_frame.columnconfigure(0, weight=0)   # Button fixed
#         row_frame.columnconfigure(1, weight=1)   # Label expands

#         # Button
#         ttk.Button(
#             row_frame,
#             text="Read",
#             width=LBTN_WIDTH,
#             bootstyle="success",
#             command=lambda i=index: self.button_action(i),
#         ).grid(row=0, column=0, padx=(0, 10), sticky="w")

#         # Label
#         ttk.Label(
#             row_frame,
#             text=chapter_name,
#             font=("Arial", 12),
#             bootstyle="secondary"
#         ).grid(row=0, column=1, sticky="w")

#         return row_frame

#     # ----------------------------------------------------------------------

#     def button_action(self, index):
#         """
#         Button press पर action run करता है।
#         """

#         if index == 1:
#             swf.switch_both_frames(self.app, 
#                                    reading_controll_frame.ReadingControllFrame, 
#                                    text_show_frame.TextShowAreaFrame)
#         elif index == 9:  # Example: 9th button special
#             test = tst()
#             test.test_method()
#         else:
#             print(f"Read clicked for Chapter {index}")





# # gui/subject_left_frame.py
# import tkinter as tk
# import ttkbootstrap as ttk
# from logic.test import TestFunction as tst
# from setting.settings import LBTN_WIDTH, SUBJECT_NAME
# from logic.switch_logic import FrameSwitcher as logic

# # नए frames import करो जो open होंगे button press पर
# from gui import quiz_left_frame, quiz_right_frame
# from gui import home_left_frame, home_right_frame
# from gui.subject_frame import subject_chapter_frame


# class ReaderLeftFrameS(ttk.Frame):
#     """
#     📘 ReaderLeftFrameS
#     यह class एक scrollable frame बनाती है जिसमें कई buttons होते हैं।  
#     - Left side panel (जैसे sidebar menu) के लिए इस्तेमाल किया जा सकता है।  
#     - Scrollbar + Mousewheel दोनों से scroll कर सकते हैं।  
#     - Buttons के नाम external setting `SUBJECT_NAME` से लिए जाते हैं।  
#     """

#     def __init__(self, master, app):
#         """
#         Constructor: Frame initialize करता है और अंदर scrollable canvas बनाता है.
        
#         Arguments:
#         master : parent widget (main window/container)
#         app    : main application का reference (future use)
#         """
#         super().__init__(master, bootstyle="info")
#         self.pack(expand=True, fill="both")
#         self.app = app  # 👈 app reference save karo

#         # 🔹 Settings / Data
#         self.item_height = 60                          # Approx height per item (used for scroll calculations)
#         self.text_data = SUBJECT_NAME         # Button labels list (from settings)
#         self.item_number = len(self.text_data)         # Total button count
#         self.list_height = self.item_number * self.item_height

#         # 🔹 Canvas for scrollable content
#         self.canvas = tk.Canvas(
#             self,
#             background="white",
#             scrollregion=(0, 0, self.winfo_width(), self.list_height),
#             highlightthickness=0,
#         )
#         self.canvas.pack(side="left", expand=True, fill="both")

#         # 🔹 Frame inside canvas (actual content here)
#         self.frame = ttk.Frame(self.canvas)

#         # 🔹 Add buttons to the frame
#         for index, item in enumerate(self.text_data):
#             self.create_item(index, item).pack(
#                 expand=True, fill="x", pady=4, padx=10
#             )

#         # 🔹 Vertical scrollbar
#         self.scrollbar = ttk.Scrollbar(
#             self, orient="vertical", command=self.canvas.yview, bootstyle="round-success"
#         )
#         self.canvas.configure(yscrollcommand=self.scrollbar.set)
#         self.scrollbar.pack(side="right", fill="y")

#         # 🔹 Events binding
#         self.canvas.bind_all(
#             "<MouseWheel>",
#             lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"),
#         )
#         self.bind("<Configure>", self.update_size)

#     # ----------------------------------------------------------------------

#     def update_size(self, event):
#         """
#         जब frame resize होता है, तब scroll region update करता है और scrollbar
#         दिखाता/छुपाता है.
#         """
#         if self.list_height >= self.winfo_height():
#             height = self.list_height
#             self.canvas.bind_all(
#                 "<MouseWheel>",
#                 lambda event: self.canvas.yview_scroll(-int(event.delta / 60), "units"),
#             )
#             self.scrollbar.pack(side="right", fill="y")
#         else:
#             height = self.winfo_height()
#             self.canvas.unbind_all("<MouseWheel>")
#             self.scrollbar.pack_forget()

#         # Scrollable frame को canvas के अंदर draw करना
#         self.canvas.create_window(
#             (0, 0),
#             window=self.frame,
#             anchor="nw",
#             width=self.winfo_width(),
#             height=height,
#         )

#     # ----------------------------------------------------------------------

#     def create_item(self, index, item):
#         """
#         एक row बनाता है जिसमें एक button होता है.
        
#         Arguments:
#         index : button का index (0 से शुरू)
#         item  : button का text (string)
#         """
#         frame = ttk.Frame(self.frame, bootstyle="light")

#         frame.rowconfigure(0, weight=1)
#         frame.columnconfigure(0, weight=1, uniform="a")

#         ttk.Button(
#             frame,
#             text=f"{item}",
#             width=LBTN_WIDTH,
#             command=lambda n=index: self.button_action(n, item),
#             bootstyle="success",
#         ).grid(row=0, column=0)

#         return frame

#     # ----------------------------------------------------------------------

#     def button_action(self, n, button_text):
#         """
#         Button press पर action run करता है.
        
#         Arguments:
#         n : button का index (0 से शुरू)
#         button_text : button का text
#         """
#         print(f"Button {n} clicked: {button_text}")
        
#         # अलग-अलग buttons के लिए अलग-अलग frames open करो
#         if n == 0:  # Mathematics button
#             # logic.switch_both_frames(self.app, 
#             #                        quiz_left_frame.QuizLeftFrame, 
#             #                        quiz_right_frame.QuizRightFrame)
#             logic.switch_right_frame_only(self.app, quiz_right_frame.QuizRightFrame)
        
#         elif n == 1:  # Reasoning button  
#             logic.switch_right_frame_only(self.app, subject_chapter_frame.SubjectChapterFrame)
        
#         elif n == 2:  # English button
#             # यहाँ आप कोई और frames set कर सकते हो
#             print("English button clicked - add your frames here")
            
#         elif n == 9:  # Example: 10th button special case
#             test = tst()
#             test.test_method()
        
#         else:
#             # Default action for other buttons
#             print(f"Button {n} ({button_text}) clicked!")






# # app.py

# import tkinter as tk
# import ttkbootstrap as ttk

# from gui import home_left_frame, home_right_frame
# from logic.switch_logic import FrameSwitcher as logic

# from setting.settings import *


# class MainApp(ttk.Window):
#     def __init__(self):
#         super().__init__(themename=THEME2)
#         self.title(TITLE)
#         self.geometry(f"{WSIZE[0]}x{WSIZE[1]}+{POS[0]}+{POS[1]}")
#         self.iconbitmap(ICON)
#         self.minsize(WSIZE[0], WSIZE[1])

#         # Back history stack
#         self.history = []
        
#         # Initialize chat_frame as None (will be set when needed)
#         self.chat_frame = None
        
#         self.top_bar_frame()

#         # Main container
#         self.container = ttk.Frame(self)
#         self.container.pack(fill="both", expand=True)

#         self.container.grid_columnconfigure(0, weight=1, uniform="group1")
#         self.container.grid_columnconfigure(1, weight=4, uniform="group1")
#         self.container.grid_rowconfigure(0, weight=1)

#         self.left_frame_container()
#         self.rigt_frame_container()

#     def top_bar_frame(self):
#         # Topbar
#         topbar = ttk.Frame(self, bootstyle="secondary")
#         topbar.pack(side="top", fill="x")

#         back_btn = ttk.Button(topbar, text="⬅ Back", bootstyle="info-outline",
#                               command=lambda: logic.go_back(self))
#         back_btn.pack(side="left", padx=10, pady=5)

#         self.search_btn = ttk.Button(topbar, text="🔍 Search", bootstyle="info-outline")
#         self.search_btn.pack(side="right", padx=10, pady=5)

#         self.search_entry = ttk.Entry(topbar)
#         self.search_entry.pack(side="right", padx=10, pady=5)

#     def rigt_frame_container(self):
#         # Left + Right containers
#         self.container_right = ttk.Frame(self.container, bootstyle="light")
#         self.container_right.grid(row=0, column=1, sticky="nsew")

#         self.right_frame = home_right_frame.HomeRight(self.container_right, self)
#         self.right_frame.pack(fill="both", expand=True)

#     def left_frame_container(self):
#         # Start with Home Screen
#         self.container_left = ttk.Frame(self.container, bootstyle="dark")
#         self.container_left.grid(row=0, column=0, sticky="nsew")

#         self.left_frame = home_left_frame.HomeLeft(self.container_left, self)
#         self.left_frame.pack(fill="both", expand=True)





# import tkinter as tk
# import ttkbootstrap as ttk
# from logic.test import TestFunction as tst
# from setting.settings import LBTN_WIDTH, MATH_CHAPTER_NAME
# from logic.switch_logic import FrameSwitcher as swf

# from gui.subject_frame import text_show_frame
# from gui.subject_frame import reading_controll_frame


# class MathChapterFrame(ttk.Frame):
#     """
#     📘 ReaderRightFrame
#     Scrollable frame जिसमें हर row में एक Button ("Read") और उसके right side एक Label (chapter name) होता है।
#     """

#     def __init__(self, master, app):
#         super().__init__(master, bootstyle="info")
#         self.pack(expand=True, fill="both")

#         self.app = app
#         self.chapters = MATH_CHAPTER_NAME   # Labels list (जैसे ["Chapter 1", "Chapter 2", ...])

#         # 🔹 Canvas for scrollable content
#         self.canvas = ttk.Canvas(self, background="white", highlightthickness=0)
#         self.canvas.pack(side="left", expand=True, fill="both")

#         # 🔹 Frame inside canvas
#         self.scrollable_frame = ttk.Frame(self.canvas)
#         self.window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

#         # 🔹 Add button + label rows
#         for index, chapter in enumerate(self.chapters, start=1):
#             self.create_row(index, chapter).pack(fill="x", pady=4, padx=10)

#         # 🔹 Scrollbar
#         self.scrollbar = ttk.Scrollbar(
#             self, orient="vertical", command=self.canvas.yview, bootstyle="round-success"
#         )
#         self.canvas.configure(yscrollcommand=self.scrollbar.set)
#         self.scrollbar.pack(side="right", fill="y")

#         # 🔹 Events
#         self.scrollable_frame.bind("<Configure>", self.update_scrollregion)
#         self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

#     # ----------------------------------------------------------------------

#     def update_scrollregion(self, event):
#         """Resize scroll region automatically based on content"""
#         self.canvas.configure(scrollregion=self.canvas.bbox("all"))
#         self.canvas.itemconfig(self.window, width=self.canvas.winfo_width())

#     def on_mousewheel(self, event):
#         """Enable mouse wheel scroll"""
#         self.canvas.yview_scroll(-int(event.delta / 60), "units")

#     # ----------------------------------------------------------------------

#     def create_row(self, index, chapter_name):
#         """
#         Row बनाता है जिसमें एक Button (Read) और एक Label (Chapter name) होता है।
#         """
#         row_frame = ttk.Frame(self.scrollable_frame, bootstyle="light")

#         # grid layout: Button (col=0), Label (col=1)
#         row_frame.columnconfigure(0, weight=0)   # Button fixed
#         row_frame.columnconfigure(1, weight=1)   # Label expands

#         # Button
#         ttk.Button(
#             row_frame,
#             text="Read",
#             width=LBTN_WIDTH,
#             bootstyle="success",
#             command=lambda i=index: self.button_action(i),
#         ).grid(row=0, column=0, padx=(0, 10), sticky="w")

#         # Label
#         ttk.Label(
#             row_frame,
#             text=chapter_name,
#             font=("Arial", 12),
#             bootstyle="secondary"
#         ).grid(row=0, column=1, sticky="w")

#         return row_frame

#     # ----------------------------------------------------------------------

#     def button_action(self, index):
#         """
#         Button press पर action run करता है।
#         """

#         if index == 0:
#             swf.switch_both_frames(self.app, 
#                                    reading_controll_frame.ReadingControllFrame, 
#                                    text_show_frame.TextShowAreaFrame)
#         elif index == 9:  # Example: 9th button special
#             test = tst()
#             test.test_method()
#         else:
#             print(f"Read clicked for Chapter {index}")






# # gui/math_chapter_frame.py
# import tkinter as tk
# import ttkbootstrap as ttk
# from logic.text_reader import TextReader


# class MathChapterFrame(ttk.Frame):
#     """
#     📘 MathChapterFrame
#     - Scrollable Text box बनाता है (chatGPT जैसा look).
#     - TextReader से file read करके show करता है।
#     """

#     def __init__(self, master, app, filepath=r"data/chapter_one_notes.txt"):
#         super().__init__(master, bootstyle="light")
#         self.app = app
#         self.filepath = filepath

#         # Reader instance
#         self.reader = TextReader(filepath)

#         # 🔹 Scrollable Text widget
#         self.text_area = tk.Text(
#             self,
#             wrap="word",
#             font=("Consolas", 12),
#             bg="white",
#             fg="black",
#             padx=10,
#             pady=10,
#         )
#         self.text_area.pack(expand=True, fill="both", side="left")

#         # 🔹 Scrollbar
#         self.scrollbar = ttk.Scrollbar(
#             self, orient="vertical", command=self.text_area.yview
#         )
#         self.scrollbar.pack(side="right", fill="y")
#         self.text_area.configure(yscrollcommand=self.scrollbar.set)

#         # 🔹 Load text
#         self.load_text()

#         # 🔹 Buttons (bottom panel)
#         button_frame = ttk.Frame(self)
#         button_frame.pack(fill="x", pady=5)

#         ttk.Button(button_frame, text="🔄 Refresh", command=self.load_text).pack(
#             side="left", padx=5
#         )
#         ttk.Button(button_frame, text="🔊 Speak", command=self.speak_text).pack(
#             side="left", padx=5
#         )

#     def load_text(self):
#         """File से text पढ़ो और text box में show करो"""
#         content = self.reader.read_text()
#         self.text_area.delete("1.0", tk.END)
#         self.text_area.insert(tk.END, content)

#     def speak_text(self):
#         """(Future) Text-to-Speech trigger"""
#         text = self.text_area.get("1.0", tk.END)
#         self.reader.text_to_speech(text)









# # gui/home_left_frame.py

# # gui/home_left_frame.py
# import ttkbootstrap as ttk
# from logic.switch_logic import FrameSwitcher as logic
# from gui import subject_left_frame, reader_right_frame
# from setting.settings import WIDTH
# from logic.reader_controller import ReaderController

# class ReadingControllFrame(ttk.Frame):
#     def __init__(self, master, app, show_text_widget):
#         super().__init__(master, bootstyle="secondary")
#         self.app = app
#         self.show_text = show_text_widget
#         self.file_path = r"data/chapter_one_notes.txt"
#         self.controller = ReaderController(self.file_path, self.show_text, self.show_text.file_done)

#         ttk.Button(self, text="Load File", bootstyle="danger", width=WIDTH,
#                    command=self.controller.load_file).pack(pady=10)

#         ttk.Button(self, text="Play", bootstyle="primary", width=WIDTH,
#                    command=self.controller.start).pack(pady=10)

#         ttk.Button(self, text="Pause", bootstyle="warning", width=WIDTH,
#                    command=self.controller.pause).pack(pady=10)

#         ttk.Button(self, text="Resume", bootstyle="danger", width=WIDTH,
#                    command=self.controller.resume).pack(pady=10)

#         ttk.Button(self, text="Restart", bootstyle="primary", width=WIDTH,
#                    command=self.controller.restart).pack(pady=10)

#         ttk.Button(self, text="Back", bootstyle="warning", width=WIDTH,
#                    command=lambda: logic.switch_frame(app, subject_left_frame.ReaderLeftFrameS,
#                                                       reader_right_frame.ReaderRightFrame)).pack(pady=10)

#         ttk.Button(self, text="Quit", bootstyle="danger", width=WIDTH,
#                    command=app.destroy).pack(pady=10)






# # import ttkbootstrap as ttk

# # from logic.switch_logic import FrameSwitcher as logic

# # from gui import subject_left_frame, reader_right_frame
# # from gui import quiz_left_frame, quiz_right_frame

# # from setting.settings import WIDTH

# # class ReadingControllFrame(ttk.Frame):
# #     def __init__(self, master, app):
# #         super().__init__(master, bootstyle="secondary")

# #         ttk.Button(self, text="Load File", 
# #                    bootstyle="danger",
# #                    width=WIDTH,
# #                    command=lambda: print("Load File Button")
# #                    ).pack(pady=10)

# #         ttk.Button(self, text="Play", 
# #                    bootstyle="primary",
# #                    width=WIDTH,
# #                    command=lambda: print("Play Button")
# #                    ).pack(pady=10)

# #         ttk.Button(self, text="Pause", 
# #                    bootstyle="warning",
# #                    width=WIDTH,
# #                    command=lambda: print("Pause")
# #                    ).pack(pady=10)
        
# #         ttk.Button(self, text="Resume", 
# #                    bootstyle="danger",
# #                    width=WIDTH,
# #                    command=lambda: print("Resume")
# #                    ).pack(pady=10)
        
# #         ttk.Button(self, text="Restart", 
# #                    bootstyle="primary",
# #                    width=WIDTH,
# #                    command=lambda: print("Restart")
# #                    ).pack(pady=10)

# #         ttk.Button(self, text="Back", 
# #                    bootstyle="warning",
# #                    width=WIDTH,
# #                    command=lambda: logic.switch_frame(app, subject_left_frame.ReaderLeftFrameS, reader_right_frame.ReaderRightFrame)
# #                    ).pack(pady=10)
        
# #         ttk.Button(self, text="Quit", 
# #                    bootstyle="danger",
# #                    width=WIDTH,
# #                    command=app.destroy
# #                    ).pack(pady=10)


# # # # # gui/reading_controll_frame.py

# # # # import ttkbootstrap as ttk
# # # # from logic.switch_logic import FrameSwitcher as logic
# # # # from gui import subject_left_frame, reader_right_frame
# # # # from gui import quiz_left_frame, quiz_right_frame
# # # # from setting.settings import WIDTH
# # # # from logic.text_reader import TextReader

# # # # class ReadingControllFrame(ttk.Frame):
# # # #     def __init__(self, master, app):
# # # #         super().__init__(master, bootstyle="secondary")
# # # #         self.app = app  # Store app reference
# # # #         self.reader = None  # TextReader instance
# # # #         self.current_file = None  # Current file path
        
# # # #         # Control buttons
# # # #         ttk.Button(self, text="Play", 
# # # #                    bootstyle="primary",
# # # #                    width=WIDTH,
# # # #                    command=self.play_file
# # # #                    ).pack(pady=10)

# # # #         ttk.Button(self, text="Pause", 
# # # #                    bootstyle="warning",
# # # #                    width=WIDTH,
# # # #                    command=self.pause_reading
# # # #                    ).pack(pady=10)
        
# # # #         ttk.Button(self, text="Resume", 
# # # #                    bootstyle="success",
# # # #                    width=WIDTH,
# # # #                    command=self.resume_reading
# # # #                    ).pack(pady=10)
        
# # # #         ttk.Button(self, text="Restart", 
# # # #                    bootstyle="info",
# # # #                    width=WIDTH,
# # # #                    command=self.restart_reading
# # # #                    ).pack(pady=10)

# # # #         ttk.Button(self, text="Load File", 
# # # #                    bootstyle="secondary",
# # # #                    width=WIDTH,
# # # #                    command=self.load_file
# # # #                    ).pack(pady=10)

# # # #         ttk.Button(self, text="Back", 
# # # #                    bootstyle="warning",
# # # #                    width=WIDTH,
# # # #                    command=lambda: logic.switch_frame(app, subject_left_frame.ReaderLeftFrameS, reader_right_frame.ReaderRightFrame)
# # # #                    ).pack(pady=10)
        
# # # #         ttk.Button(self, text="Quit", 
# # # #                    bootstyle="danger",
# # # #                    width=WIDTH,
# # # #                    command=app.destroy
# # # #                    ).pack(pady=10)
    
# # # #     def load_file(self):
# # # #         """Load a text file for reading"""
# # # #         # For demo purposes, using a hardcoded file path
# # # #         # In real app, you'd use filedialog.askopenfilename()
# # # #         file_path = "data/subject_chapter_frame_chapter.txt"
# # # #         self.current_file = file_path
        
# # # #         # Create new reader instance
# # # #         self.reader = TextReader(
# # # #             file_path=file_path,
# # # #             on_line=self.app.chat_frame.enqueue_line,
# # # #             on_done=self.on_reading_done,
# # # #             line_delay_ms=100  # Adjust typing speed
# # # #         )
        
# # # #         # Clear previous content
# # # #         self.clear_chat()
        
# # # #         print(f"Loaded file: {file_path}")
    
# # # #     def play_file(self):
# # # #         """Start reading the loaded file"""
# # # #         if self.reader and self.current_file:
# # # #             self.reader.start_stream()
# # # #             print("Started reading...")
# # # #         else:
# # # #             print("Please load a file first!")
    
# # # #     def pause_reading(self):
# # # #         """Pause the current reading"""
# # # #         if self.reader:
# # # #             self.reader.stop()
# # # #             print("Reading paused")
    
# # # #     def resume_reading(self):
# # # #         """Resume reading from where it was paused"""
# # # #         if self.reader and self.current_file:
# # # #             # For simplicity, we'll restart from beginning
# # # #             # In a real implementation, you'd need to track position
# # # #             self.restart_reading()
# # # #             print("Resumed reading")
    
# # # #     def restart_reading(self):
# # # #         """Restart reading from the beginning"""
# # # #         if self.current_file:
# # # #             self.clear_chat()
# # # #             self.load_file()  # Reload the file
# # # #             self.play_file()  # Start reading
# # # #             print("Restarted reading")
    
# # # #     def clear_chat(self):
# # # #         """Clear the chat display"""
# # # #         if hasattr(self.app, 'chat_frame'):
# # # #             for widget in self.app.chat_frame.chat_frame.winfo_children():
# # # #                 widget.destroy()
    
# # # #     def on_reading_done(self):
# # # #         """Callback when reading is completed"""
# # # #         print("Reading completed")
# # # #         if hasattr(self.app, 'chat_frame'):
# # # #             self.app.chat_frame.file_done()


# # # # gui/reading_controll_frame.py

# # # import ttkbootstrap as ttk
# # # from tkinter import filedialog, messagebox
# # # from logic.switch_logic import FrameSwitcher as logic
# # # from gui import subject_left_frame, reader_right_frame
# # # from gui import quiz_left_frame, quiz_right_frame
# # # from setting.settings import WIDTH
# # # from logic.text_reader import TextReader

# # # class ReadingControllFrame(ttk.Frame):
# # #     def __init__(self, master, app):
# # #         super().__init__(master, bootstyle="secondary")
# # #         self.app = app
# # #         self.reader = None
# # #         self.current_file = None
# # #         self.is_playing = False
# # #         self.is_paused = False
        
# # #         # Create button frame for better organization
# # #         button_frame = ttk.Frame(self)
# # #         button_frame.pack(pady=20, padx=10, fill="x")
        
# # #         # Control buttons
# # #         self.play_btn = ttk.Button(button_frame, text="Play", 
# # #                    bootstyle="primary",
# # #                    width=WIDTH,
# # #                    command=self.play_file
# # #                    )
# # #         self.play_btn.pack(pady=5)
        
# # #         self.pause_btn = ttk.Button(button_frame, text="Pause", 
# # #                    bootstyle="warning",
# # #                    width=WIDTH,
# # #                    command=self.pause_reading,
# # #                    state="disabled"
# # #                    )
# # #         self.pause_btn.pack(pady=5)
        
# # #         self.resume_btn = ttk.Button(button_frame, text="Resume", 
# # #                    bootstyle="success",
# # #                    width=WIDTH,
# # #                    command=self.resume_reading,
# # #                    state="disabled"
# # #                    )
# # #         self.resume_btn.pack(pady=5)
        
# # #         self.restart_btn = ttk.Button(button_frame, text="Restart", 
# # #                    bootstyle="info",
# # #                    width=WIDTH,
# # #                    command=self.restart_reading,
# # #                    state="disabled"
# # #                    )
# # #         self.restart_btn.pack(pady=5)

# # #         self.load_btn = ttk.Button(button_frame, text="Load File", 
# # #                    bootstyle="secondary",
# # #                    width=WIDTH,
# # #                    command=self.load_file
# # #                    )
# # #         self.load_btn.pack(pady=5)

# # #         ttk.Button(button_frame, text="Back", 
# # #                    bootstyle="warning",
# # #                    width=WIDTH,
# # #                    command=lambda: logic.switch_frame(app, subject_left_frame.ReaderLeftFrameS, reader_right_frame.ReaderRightFrame)
# # #                    ).pack(pady=5)
        
# # #         ttk.Button(button_frame, text="Quit", 
# # #                    bootstyle="danger",
# # #                    width=WIDTH,
# # #                    command=app.destroy
# # #                    ).pack(pady=5)
        
# # #         # Status label
# # #         self.status_var = ttk.StringVar(value="No file loaded")
# # #         ttk.Label(button_frame, textvariable=self.status_var, 
# # #                  bootstyle="inverse-secondary", anchor="center").pack(pady=10, fill="x")
    
# # #     def update_button_states(self):
# # #         """Update button states based on current reading state"""
# # #         has_file = self.current_file is not None
# # #         self.play_btn.config(state="normal" if has_file else "disabled")
# # #         self.pause_btn.config(state="normal" if self.is_playing else "disabled")
# # #         self.resume_btn.config(state="normal" if self.is_paused else "disabled")
# # #         self.restart_btn.config(state="normal" if has_file else "disabled")
    
# # #     def load_file(self):
# # #         """Load a text file for reading using file dialog"""
# # #         file_path = filedialog.askopenfilename(
# # #             title="Select Geography Text File",
# # #             filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
# # #         )
        
# # #         if not file_path:
# # #             return
            
# # #         try:
# # #             self.current_file = file_path
            
# # #             # Create new reader instance
# # #             self.reader = TextReader(
# # #                 file_path=file_path,
# # #                 on_line=self.app.chat_frame.enqueue_line,
# # #                 on_done=self.on_reading_done,
# # #                 line_delay_ms=100
# # #             )
            
# # #             # Clear previous content
# # #             self.clear_chat()
            
# # #             self.status_var.set(f"Loaded: {file_path.split('/')[-1]}")
# # #             self.update_button_states()
            
# # #         except Exception as e:
# # #             messagebox.showerror("Error", f"Failed to load file: {str(e)}")
# # #             self.status_var.set("Error loading file")
    
# # #     def play_file(self):
# # #         """Start reading the loaded file"""
# # #         try:
# # #             if not self.reader and self.current_file:
# # #                 self.load_file()  # Reload if needed
                
# # #             if self.reader:
# # #                 self.reader.start_stream()
# # #                 self.is_playing = True
# # #                 self.is_paused = False
# # #                 self.status_var.set("Playing...")
# # #                 self.update_button_states()
# # #         except Exception as e:
# # #             messagebox.showerror("Error", f"Playback error: {str(e)}")
    
# # #     def pause_reading(self):
# # #         """Pause the current reading"""
# # #         if self.reader:
# # #             self.reader.stop()
# # #             self.is_playing = False
# # #             self.is_paused = True
# # #             self.status_var.set("Paused")
# # #             self.update_button_states()
    
# # #     def resume_reading(self):
# # #         """Resume reading from where it was paused"""
# # #         if self.reader and self.is_paused:
# # #             # This assumes your TextReader has resume capability
# # #             # If not, you may need to modify TextReader to support this
# # #             try:
# # #                 self.reader.resume()  # You might need to implement this method
# # #                 self.is_playing = True
# # #                 self.is_paused = False
# # #                 self.status_var.set("Playing...")
# # #                 self.update_button_states()
# # #             except:
# # #                 # Fallback to restart if resume not supported
# # #                 self.restart_reading()
    
# # #     def restart_reading(self):
# # #         """Restart reading from the beginning"""
# # #         if self.current_file:
# # #             self.clear_chat()
# # #             self.load_file()  # Reload the file
# # #             self.play_file()  # Start reading
    
# # #     def clear_chat(self):
# # #         """Clear the chat display"""
# # #         if hasattr(self.app, 'chat_frame'):
# # #             for widget in self.app.chat_frame.chat_frame.winfo_children():
# # #                 widget.destroy()
    
# # #     def on_reading_done(self):
# # #         """Callback when reading is completed"""
# # #         self.is_playing = False
# # #         self.is_paused = False
# # #         self.status_var.set("Playback completed")
# # #         self.update_button_states()
        
# # #         if hasattr(self.app, 'chat_frame'):
# # #             self.app.chat_frame.file_done()



# # # gui/reading_controll_frame.py

# # import ttkbootstrap as ttk
# # from tkinter import filedialog, messagebox
# # from logic.switch_logic import FrameSwitcher as logic
# # from gui import subject_left_frame, reader_right_frame
# # from setting.settings import WIDTH
# # from logic.text_reader import TextReader

# # class ReadingControllFrame(ttk.Frame):
# #     def __init__(self, master, app):
# #         super().__init__(master, bootstyle="secondary")
# #         self.app = app
# #         self.reader = None
# #         self.current_file = None
# #         self.is_playing = False
# #         self.is_paused = False
        
# #         # Create button frame for better organization
# #         button_frame = ttk.Frame(self)
# #         button_frame.pack(pady=20, padx=10, fill="x")
        
# #         # Control buttons
# #         self.play_btn = ttk.Button(button_frame, text="Play", 
# #                    bootstyle="primary",
# #                    width=WIDTH,
# #                    command=self.play_file
# #                    )
# #         self.play_btn.pack(pady=5)
        
# #         self.pause_btn = ttk.Button(button_frame, text="Pause", 
# #                    bootstyle="warning",
# #                    width=WIDTH,
# #                    command=self.pause_reading,
# #                    state="disabled"
# #                    )
# #         self.pause_btn.pack(pady=5)
        
# #         self.resume_btn = ttk.Button(button_frame, text="Resume", 
# #                    bootstyle="success",
# #                    width=WIDTH,
# #                    command=self.resume_reading,
# #                    state="disabled"
# #                    )
# #         self.resume_btn.pack(pady=5)
        
# #         self.restart_btn = ttk.Button(button_frame, text="Restart", 
# #                    bootstyle="info",
# #                    width=WIDTH,
# #                    command=self.restart_reading,
# #                    state="disabled"
# #                    )
# #         self.restart_btn.pack(pady=5)

# #         self.load_btn = ttk.Button(button_frame, text="Load File", 
# #                    bootstyle="secondary",
# #                    width=WIDTH,
# #                    command=self.load_file
# #                    )
# #         self.load_btn.pack(pady=5)

# #         ttk.Button(button_frame, text="Back", 
# #                    bootstyle="warning",
# #                    width=WIDTH,
# #                    command=lambda: logic.switch_frame(app, subject_left_frame.ReaderLeftFrameS, reader_right_frame.ReaderRightFrame)
# #                    ).pack(pady=5)
        
# #         ttk.Button(button_frame, text="Quit", 
# #                    bootstyle="danger",
# #                    width=WIDTH,
# #                    command=app.destroy
# #                    ).pack(pady=5)
        
# #         # Status label
# #         self.status_var = ttk.StringVar(value="No file loaded")
# #         ttk.Label(button_frame, textvariable=self.status_var, 
# #                  bootstyle="inverse-secondary", anchor="center").pack(pady=10, fill="x")
    
# #     def update_button_states(self):
# #         """Update button states based on current reading state"""
# #         has_file = self.current_file is not None
# #         self.play_btn.config(state="normal" if has_file else "disabled")
# #         self.pause_btn.config(state="normal" if self.is_playing else "disabled")
# #         self.resume_btn.config(state="normal" if self.is_paused else "disabled")
# #         self.restart_btn.config(state="normal" if has_file else "disabled")
    
# #     def load_file(self):
# #         """Load a text file for reading using file dialog"""
# #         file_path = filedialog.askopenfilename(
# #             title="Select Geography Text File",
# #             filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
# #         )
        
# #         if not file_path:
# #             return
            
# #         try:
# #             self.current_file = file_path
            
# #             # Create new reader instance
# #             self.reader = TextReader(
# #                 file_path=file_path,
# #                 on_line=self.app.chat_frame.enqueue_line,  # Fixed: chat_frame (not chat_fram)
# #                 on_done=self.on_reading_done,
# #                 line_delay_ms=100
# #             )
            
# #             # Clear previous content
# #             self.clear_chat()
            
# #             self.status_var.set(f"Loaded: {file_path.split('/')[-1]}")
# #             self.update_button_states()
            
# #         except Exception as e:
# #             messagebox.showerror("Error", f"Failed to load file: {str(e)}")
# #             self.status_var.set("Error loading file")
    
# #     def play_file(self):
# #         """Start reading the loaded file"""
# #         try:
# #             if not self.reader and self.current_file:
# #                 self.load_file()  # Reload if needed
                
# #             if self.reader:
# #                 self.reader.start_stream()
# #                 self.is_playing = True
# #                 self.is_paused = False
# #                 self.status_var.set("Playing...")
# #                 self.update_button_states()
# #         except Exception as e:
# #             messagebox.showerror("Error", f"Playback error: {str(e)}")
    
# #     def pause_reading(self):
# #         """Pause the current reading"""
# #         if self.reader:
# #             self.reader.stop()
# #             self.is_playing = False
# #             self.is_paused = True
# #             self.status_var.set("Paused")
# #             self.update_button_states()
    
# #     def resume_reading(self):
# #         """Resume reading from where it was paused"""
# #         if self.reader and self.is_paused:
# #             # This assumes your TextReader has resume capability
# #             # If not, you may need to modify TextReader to support this
# #             try:
# #                 # Check if TextReader has a resume method
# #                 if hasattr(self.reader, 'resume'):
# #                     self.reader.resume()
# #                 else:
# #                     # Fallback to restart if resume not supported
# #                     self.restart_reading()
                
# #                 self.is_playing = True
# #                 self.is_paused = False
# #                 self.status_var.set("Playing...")
# #                 self.update_button_states()
# #             except Exception as e:
# #                 messagebox.showerror("Error", f"Resume error: {str(e)}")
# #                 # Fallback to restart if resume fails
# #                 self.restart_reading()
    
# #     def restart_reading(self):
# #         """Restart reading from the beginning"""
# #         if self.current_file:
# #             self.clear_chat()
# #             # Create a new reader instance
# #             self.reader = TextReader(
# #                 file_path=self.current_file,
# #                 on_line=self.app.chat_frame.enqueue_line,  # Fixed: chat_frame (not chat_fram)
# #                 on_done=self.on_reading_done,
# #                 line_delay_ms=100
# #             )
# #             self.play_file()  # Start reading
    
# #     def clear_chat(self):
# #         """Clear the chat display"""
# #         # Fixed: chat_frame (not chat_fram)
# #         if hasattr(self.app, 'chat_frame') and hasattr(self.app.chat_frame, 'chat_frame'):
# #             for widget in self.app.chat_frame.chat_frame.winfo_children():
# #                 widget.destroy()
    
# #     def on_reading_done(self):
# #         """Callback when reading is completed"""
# #         self.is_playing = False
# #         self.is_paused = False
# #         self.status_var.set("Playback completed")
# #         self.update_button_states()
        
# #         # Fixed: chat_frame (not chat_fram)
# #         if hasattr(self.app, 'chat_frame') and hasattr(self.app.chat_frame, 'file_done'):
# #             self.app.chat_frame.file_done()




# # # gui/reading_controll_frame.py

# # import ttkbootstrap as ttk
# # from tkinter import filedialog, messagebox
# # from logic.switch_logic import FrameSwitcher as logic
# # from gui import subject_left_frame, reader_right_frame
# # from setting.settings import WIDTH
# # from logic.text_reader import TextReader

# # class ReadingControllFrame(ttk.Frame):
# #     def __init__(self, master, app):
# #         super().__init__(master, bootstyle="secondary")
# #         self.app = app
# #         self.reader = None
# #         self.current_file = None
# #         self.is_playing = False
# #         self.is_paused = False
        
# #         # Create button frame for better organization
# #         button_frame = ttk.Frame(self)
# #         button_frame.pack(pady=20, padx=10, fill="x")
        
# #         # Control buttons
# #         self.play_btn = ttk.Button(button_frame, text="Play", 
# #                    bootstyle="primary",
# #                    width=WIDTH,
# #                    command=self.play_file
# #                    )
# #         self.play_btn.pack(pady=5)
        
# #         self.pause_btn = ttk.Button(button_frame, text="Pause", 
# #                    bootstyle="warning",
# #                    width=WIDTH,
# #                    command=self.pause_reading,
# #                    state="disabled"
# #                    )
# #         self.pause_btn.pack(pady=5)
        
# #         self.resume_btn = ttk.Button(button_frame, text="Resume", 
# #                    bootstyle="success",
# #                    width=WIDTH,
# #                    command=self.resume_reading,
# #                    state="disabled"
# #                    )
# #         self.resume_btn.pack(pady=5)
        
# #         self.restart_btn = ttk.Button(button_frame, text="Restart", 
# #                    bootstyle="info",
# #                    width=WIDTH,
# #                    command=self.restart_reading,
# #                    state="disabled"
# #                    )
# #         self.restart_btn.pack(pady=5)

# #         self.load_btn = ttk.Button(button_frame, text="Load File", 
# #                    bootstyle="secondary",
# #                    width=WIDTH,
# #                    command=self.load_file
# #                    )
# #         self.load_btn.pack(pady=5)

# #         ttk.Button(button_frame, text="Back", 
# #                    bootstyle="warning",
# #                    width=WIDTH,
# #                    command=lambda: logic.switch_frame(app, subject_left_frame.ReaderLeftFrameS, reader_right_frame.ReaderRightFrame)
# #                    ).pack(pady=5)
        
# #         ttk.Button(button_frame, text="Quit", 
# #                    bootstyle="danger",
# #                    width=WIDTH,
# #                    command=app.destroy
# #                    ).pack(pady=5)
        
# #         # Status label
# #         self.status_var = ttk.StringVar(value="No file loaded")
# #         ttk.Label(button_frame, textvariable=self.status_var, 
# #                  bootstyle="inverse-secondary", anchor="center").pack(pady=10, fill="x")
    
# #     def update_button_states(self):
# #         """Update button states based on current reading state"""
# #         has_file = self.current_file is not None
# #         self.play_btn.config(state="normal" if has_file else "disabled")
# #         self.pause_btn.config(state="normal" if self.is_playing else "disabled")
# #         self.resume_btn.config(state="normal" if self.is_paused else "disabled")
# #         self.restart_btn.config(state="normal" if has_file else "disabled")
    
# #     def load_file(self):
# #         """Load a text file for reading using file dialog"""
# #         file_path = filedialog.askopenfilename(
# #             title="Select Geography Text File",
# #             filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
# #         )
        
# #         if not file_path:
# #             return
            
# #         try:
# #             self.current_file = file_path
            
# #             # Create new reader instance only if chat_frame exists
# #             if hasattr(self.app, 'chat_frame') and self.app.chat_frame is not None:
# #                 self.reader = TextReader(
# #                     file_path=file_path,
# #                     on_line=self.app.chat_frame.enqueue_line,
# #                     on_done=self.on_reading_done,
# #                     line_delay_ms=100
# #                 )
                
# #                 # Clear previous content
# #                 self.clear_chat()
                
# #                 self.status_var.set(f"Loaded: {file_path.split('/')[-1]}")
# #             else:
# #                 self.status_var.set("Chat frame not available")
                
# #             self.update_button_states()
            
# #         except Exception as e:
# #             messagebox.showerror("Error", f"Failed to load file: {str(e)}")
# #             self.status_var.set("Error loading file")
    
# #     def play_file(self):
# #         """Start reading the loaded file"""
# #         try:
# #             if not self.reader and self.current_file:
# #                 self.load_file()  # Reload if needed
                
# #             if self.reader:
# #                 self.reader.start_stream()
# #                 self.is_playing = True
# #                 self.is_paused = False
# #                 self.status_var.set("Playing...")
# #                 self.update_button_states()
# #         except Exception as e:
# #             messagebox.showerror("Error", f"Playback error: {str(e)}")
    
# #     def pause_reading(self):
# #         """Pause the current reading"""
# #         if self.reader:
# #             self.reader.stop()
# #             self.is_playing = False
# #             self.is_paused = True
# #             self.status_var.set("Paused")
# #             self.update_button_states()
    
# #     def resume_reading(self):
# #         """Resume reading from where it was paused"""
# #         if self.reader and self.is_paused:
# #             # This assumes your TextReader has resume capability
# #             # If not, you may need to modify TextReader to support this
# #             try:
# #                 # Check if TextReader has a resume method
# #                 if hasattr(self.reader, 'resume'):
# #                     self.reader.resume()
# #                 else:
# #                     # Fallback to restart if resume not supported
# #                     self.restart_reading()
                
# #                 self.is_playing = True
# #                 self.is_paused = False
# #                 self.status_var.set("Playing...")
# #                 self.update_button_states()
# #             except Exception as e:
# #                 messagebox.showerror("Error", f"Resume error: {str(e)}")
# #                 # Fallback to restart if resume fails
# #                 self.restart_reading()
    
# #     def restart_reading(self):
# #         """Restart reading from the beginning"""
# #         if self.current_file:
# #             self.clear_chat()
# #             # Create a new reader instance if chat_frame exists
# #             if hasattr(self.app, 'chat_frame') and self.app.chat_frame is not None:
# #                 self.reader = TextReader(
# #                     file_path=self.current_file,
# #                     on_line=self.app.chat_frame.enqueue_line,
# #                     on_done=self.on_reading_done,
# #                     line_delay_ms=100
# #                 )
# #                 self.play_file()  # Start reading
    
# #     def clear_chat(self):
# #         """Clear the chat display"""
# #         # Check if chat_frame exists and has the chat_frame attribute
# #         if (hasattr(self.app, 'chat_frame') and 
# #             self.app.chat_frame is not None and 
# #             hasattr(self.app.chat_frame, 'chat_frame')):
# #             for widget in self.app.chat_frame.chat_frame.winfo_children():
# #                 widget.destroy()
    
# #     def on_reading_done(self):
# #         """Callback when reading is completed"""
# #         self.is_playing = False
# #         self.is_paused = False
# #         self.status_var.set("Playback completed")
# #         self.update_button_states()
        
# #         # Check if chat_frame exists and has file_done method
# #         if (hasattr(self.app, 'chat_frame') and 
# #             self.app.chat_frame is not None and 
# #             hasattr(self.app.chat_frame, 'file_done')):
# #             self.app.chat_frame.file_done()






# # gui/text_show_frame.py
# import tkinter as tk
# from queue import Queue

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

# class ShowText(tk.Frame):
#     """
#     Chat-like view that renders lines as chat bubbles with typing effect.
#     Uses an internal queue to receive lines from ReaderController thread.
#     """
#     def __init__(self, parent, on_file_done=None):
#         super().__init__(parent, bg="#ECECEC")
#         self.on_file_done = on_file_done
#         self.pack(expand=True, fill="both")

#         # Create main container
#         self.grid_rowconfigure(0, weight=1)
#         self.grid_columnconfigure(0, weight=1)
        
#         # Create a frame to hold canvas and scrollbar
#         container = tk.Frame(self, bg="#ECECEC")
#         container.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
        
#         # Scrollable Canvas
#         self.canvas = tk.Canvas(container, bg="#ECECEC", highlightthickness=0)
#         self.canvas.grid(row=0, column=0, sticky="nsew")
        
#         # Scrollbar
#         self.scroll_y = tk.Scrollbar(container, orient="vertical", command=self.canvas.yview)
#         self.scroll_y.grid(row=0, column=1, sticky="ns")
#         self.canvas.configure(yscrollcommand=self.scroll_y.set)

#         # Chat frame inside canvas
#         self.chat_frame = tk.Frame(self.canvas, bg="#ECECEC")
#         self.window = self.canvas.create_window((0, 0), window=self.chat_frame, anchor="nw")

#         # Events
#         self.chat_frame.bind("<Configure>", self.update_scrollregion)
#         self.canvas.bind("<Configure>", self.on_canvas_configure)
#         self.canvas.bind("<Enter>", self.bind_mousewheel)
#         self.canvas.bind("<Leave>", self.unbind_mousewheel)

#         # Queue for incoming lines
#         self._line_q = Queue()

#         # Start polling queue
#         self.after(50, self._poll_queue)

#     def update_scrollregion(self, event):
#         """Update scroll region when chat frame changes size"""
#         self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
#     def on_canvas_configure(self, event):
#         """Update the inner frame's width to match canvas"""
#         self.canvas.itemconfig(self.window, width=event.width)
        
#     def bind_mousewheel(self, event):
#         """Bind mousewheel only when cursor is over this canvas"""
#         self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)
        
#     def unbind_mousewheel(self, event):
#         """Unbind mousewheel when cursor leaves this canvas"""
#         self.canvas.unbind_all("<MouseWheel>")
        
#     def on_mousewheel(self, event):
#         """Enable mouse wheel scroll"""
#         self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

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

#         # Update scroll region after adding new bubble
#         self.update_idletasks()
#         self.update_scrollregion(None)
        
#         # Typing effect via after()
#         self._type_char(bubble, text, idx=0)

#     def _type_char(self, widget, full_text, idx):
#         if idx <= len(full_text):
#             widget.config(text=full_text[:idx])
#             # Auto-scroll to bottom
#             self.canvas.yview_moveto(1.0)
#             self.after(15, self._type_char, widget, full_text, idx + 1)
#         # else: finished typing this bubble

#     # Optionally, let app know when file finished (controller also calls app)
#         def file_done(self):
#             if callable(self.on_file_done):
#                 self.on_file_done()
#             # Bubble me bhi message dikhado
#             done_label = tk.Label(
#                 self.chat_frame, text="✅ File Completed!",
#                 bg="#ECECEC", fg="green", font=("Nirmala UI", 12, "bold"),
#                 pady=10
#             )
#             done_label.pack(anchor="center", pady=6)
#             self.canvas.yview_moveto(1.0)





# # logic/reader_controller.py
# import threading
# import time

# class ReaderController:
#     def __init__(self, filepath, show_text_widget, on_done=None):
#         self.filepath = filepath
#         self.show_text = show_text_widget
#         self.on_done = on_done

#         self._lines = []
#         self._thread = None
#         self._running = False
#         self._paused = False
#         self._pos = 0   # current line index

#     def load_file(self):
#         """Load file into memory"""
#         with open(self.filepath, "r", encoding="utf-8") as f:
#             self._lines = [line.strip() for line in f if line.strip()]
#         self._pos = 0

#     def start(self):
#         """Start reading in background thread"""
#         if not self._lines:
#             self.load_file()
#         self._running = True
#         self._paused = False
#         self._thread = threading.Thread(target=self._run, daemon=True)
#         self._thread.start()

#     def _run(self):
#         while self._running and self._pos < len(self._lines):
#             if self._paused:
#                 time.sleep(0.1)
#                 continue
#             line = self._lines[self._pos]
#             self.show_text.enqueue_line(line)
#             self._pos += 1
#             time.sleep(0.5)  # delay between lines

#         if self._pos >= len(self._lines):
#             self._running = False
#             if self.on_done:
#                 self.on_done()

#     def pause(self):
#         self._paused = True

#     def resume(self):
#         self._paused = False

#     def restart(self):
#         self.stop()
#         self._pos = 0
#         self.start()

#     def stop(self):
#         self._running = False


# def file_path(f_path):
#     return f_path


# ptr=file_path("aghuag")

# print(ptr)






    # def top_bar_frame(self):
    #     # Topbar
    #     topbar = ttk.Frame(self, bootstyle="secondary")
    #     topbar.pack(side="top", fill="x")

    #     back_btn = ttk.Button(topbar, text="⬅ Back", bootstyle="info-outline",
    #                           command=lambda: logic.go_back(self))
    #     back_btn.pack(side="left", padx=10, pady=5)
    #     back_btn = ttk.Button(topbar, text="⬅Forward", bootstyle="info-outline",
    #                           command=lambda: logic.go_forward(self))
    #     back_btn.pack(side="left", padx=10, pady=5)

    #     self.search_btn = ttk.Button(topbar, text="🔍 Search", bootstyle="info-outline")
    #     self.search_btn.pack(side="right", padx=10, pady=5)

    #     self.search_entry = ttk.Entry(topbar)
    #     self.search_entry.pack(side="right", padx=10, pady=5)


    # def top_bar_frame(self):
    #     # Topbar Frame
    #     topbar = ttk.Frame(self, bootstyle="dark")   # darker topbar for contrast
    #     topbar.pack(side="top", fill="x")

    #     # Navigation Buttons (Left Side)
    #     nav_frame = ttk.Frame(topbar)
    #     nav_frame.pack(side="left", padx=10, pady=5)

    #     back_btn = ttk.Button(nav_frame, text="⬅ Back", bootstyle="info-outline",
    #                         command=lambda: logic.go_back(self))
    #     back_btn.pack(side="left", padx=5)

    #     forward_btn = ttk.Button(nav_frame, text="➡ Forward", bootstyle="info-outline",
    #                             command=lambda: logic.go_forward(self))
    #     forward_btn.pack(side="left", padx=5)

    #     home_btn = ttk.Button(nav_frame, text="🏠 Home", bootstyle="success-outline",
    #                         command=lambda: logic.go_home(self))   # 👈 New Home Button
    #     home_btn.pack(side="left", padx=5)

    #     # Search Section (Right Side)
    #     search_frame = ttk.Frame(topbar)
    #     search_frame.pack(side="right", padx=10, pady=5)

    #     self.search_entry = ttk.Entry(search_frame, width=25)
    #     self.search_entry.pack(side="right", padx=5)

    #     self.search_btn = ttk.Button(search_frame, text="🔍 Search", bootstyle="info-outline")
    #     self.search_btn.pack(side="right", padx=5)