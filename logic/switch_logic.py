
# # # logic/switch_logic.py

# # class FrameSwitcher:

# #     def switch_right_frame_only(main_gui, right_class):
# #         """
# #         सिर्फ right frame को change करने के लिए
# #         """
# #         # Save history for back
# #         main_gui.history.append((main_gui.left_frame.__class__, main_gui.right_frame.__class__))

# #         # Destroy only right frame
# #         main_gui.right_frame.destroy()

# #         # Create new right frame
# #         main_gui.right_frame = right_class(main_gui.container_right, main_gui)
# #         main_gui.right_frame.pack(fill="both", expand=True)

# #     def switch_frame(main_gui, left_class, right_class):
# #         # Save history for back
# #         main_gui.history.append((main_gui.left_frame.__class__, main_gui.right_frame.__class__))

# #         # Destroy old frames
# #         main_gui.left_frame.destroy()
# #         main_gui.right_frame.destroy()

# #         # Create new frames
# #         main_gui.left_frame = left_class(main_gui.container_left, main_gui)
# #         main_gui.left_frame.pack(fill="both", expand=True)

# #         main_gui.right_frame = right_class(main_gui.container_right, main_gui)
# #         main_gui.right_frame.pack(fill="both", expand=True)

# #     # def go_back(main_gui):
# #     #     if main_gui.history:
# #     #         last_left, last_right = main_gui.history.pop()

# #     #         # Destroy current frames
# #     #         main_gui.left_frame.destroy()
# #     #         main_gui.right_frame.destroy()

# #     #         # Restore previous frames
# #     #         main_gui.left_frame = last_left(main_gui.container_left, main_gui)
# #     #         main_gui.left_frame.pack(fill="both", expand=True)

# #     #         main_gui.right_frame = last_right(main_gui.container_right, main_gui)
# #     #         main_gui.right_frame.pack(fill="both", expand=True)


# #     def go_back(main_gui):
# #         if main_gui.history:
# #             left_class, right_class = main_gui.history.pop()
# #             main_gui.forward_stack.append((type(main_gui.left_frame), type(main_gui.right_frame)))

# #             main_gui.left_frame.destroy()
# #             main_gui.right_frame.destroy()

# #             main_gui.left_frame = left_class(main_gui.container_left, main_gui)
# #             main_gui.left_frame.pack(fill="both", expand=True)

# #             main_gui.right_frame = right_class(main_gui.container_right, main_gui)
# #             main_gui.right_frame.pack(fill="both", expand=True)


# #     def go_forward(main_gui):
# #         if main_gui.forward_stack:
# #             left_class, right_class = main_gui.forward_stack.pop()
# #             main_gui.history.append((type(main_gui.left_frame), type(main_gui.right_frame)))

# #             main_gui.left_frame.destroy()
# #             main_gui.right_frame.destroy()

# #             main_gui.left_frame = left_class(main_gui.container_left, main_gui)
# #             main_gui.left_frame.pack(fill="both", expand=True)

# #             main_gui.right_frame = right_class(main_gui.container_right, main_gui)
# #             main_gui.right_frame.pack(fill="both", expand=True)



# #     # def switch_both_frames(main_gui, left_class, right_class):
# #     #     """
# #     #     नया method: दोनों frames को एक साथ switch करने के लिए + history maintain
# #     #     """
# #     #     # Save history for back
# #     #     main_gui.history.append((main_gui.left_frame.__class__, main_gui.right_frame.__class__))

# #     #     # Destroy old frames
# #     #     main_gui.left_frame.destroy()
# #     #     main_gui.right_frame.destroy()

# #     #     # Create new frames
# #     #     main_gui.left_frame = left_class(main_gui.container_left, main_gui)
# #     #     main_gui.left_frame.pack(fill="both", expand=True)

# #     #     main_gui.right_frame = right_class(main_gui.container_right, main_gui)
# #     #     main_gui.right_frame.pack(fill="both", expand=True)

# #     def switch_both_frames(main_gui, left_class, right_class):
# #         """
# #         नया method: दोनों frames को एक साथ switch करने के लिए + history maintain
# #         """
# #         main_gui.history.append((main_gui.left_frame.__class__, main_gui.right_frame.__class__))

# #         main_gui.left_frame.destroy()
# #         main_gui.right_frame.destroy()

# #         # ✅ अगर callable है तो call करो
# #         main_gui.left_frame = left_class(main_gui.container_left, main_gui) if callable(left_class) else left_class(main_gui.container_left, main_gui)
# #         main_gui.left_frame.pack(fill="both", expand=True)

# #         main_gui.right_frame = right_class(main_gui.container_right, main_gui) if callable(right_class) else right_class(main_gui.container_right, main_gui)
# #         main_gui.right_frame.pack(fill="both", expand=True)














# # logic/switch_logic.py

# class FrameSwitcher:

#     def switch_right_frame_only(main_gui, right_class):
#         """
#         सिर्फ right frame को change करने के लिए
#         """
#         main_gui.history.append((main_gui.left_frame.__class__, main_gui.right_frame.__class__))

#         # ❌ नया navigation → forward stack clear
#         main_gui.forward_stack.clear()

#         main_gui.right_frame.destroy()

#         main_gui.right_frame = right_class(main_gui.container_right, main_gui)

#     def switch_both_frames(main_gui, left_class, right_class):
#         """
#         दोनों frames को एक साथ switch करने के लिए + history maintain
#         """
#         main_gui.history.append((main_gui.left_frame.__class__, main_gui.right_frame.__class__))

#         # ❌ नया navigation → forward stack clear
#         main_gui.forward_stack.clear()

#         main_gui.left_frame.destroy()
#         main_gui.right_frame.destroy()

#         main_gui.left_frame = left_class(main_gui.container_left, main_gui)
#         main_gui.left_frame.pack(fill="both", expand=True)

#         main_gui.right_frame = right_class(main_gui.container_right, main_gui)
#         main_gui.right_frame.pack(fill="both", expand=True)
#         main_gui.right_frame.pack(fill="both", expand=True)

#     # def switch_frame(main_gui, left_class, right_class):
#     #     main_gui.history.append((main_gui.left_frame.__class__, main_gui.right_frame.__class__))

#     #     # ❌ नया navigation → forward stack clear
#     #     main_gui.forward_stack.clear()

#     #     main_gui.left_frame.destroy()
#     #     main_gui.right_frame.destroy()

#     #     main_gui.left_frame = left_class(main_gui.container_left, main_gui)
#     #     main_gui.left_frame.pack(fill="both", expand=True)

#     #     main_gui.right_frame = right_class(main_gui.container_right, main_gui)
#     #     main_gui.right_frame.pack(fill="both", expand=True)



#     def switch_frame(main_gui, left_class, right_class, page_name=""):
#         """Main function to switch frames like browser navigation"""
        
#         # Agar koi current frame hai to usko history me bhej do
#         if hasattr(main_gui, "left_frame") and hasattr(main_gui, "right_frame"):
#             main_gui.history.append((
#                 main_gui.left_frame.__class__,
#                 main_gui.right_frame.__class__,
#                 main_gui.page_label.cget("text")  # save current page name
#             ))

#         # Forward history clear kar do (browser जैसा)
#         main_gui.forward_history.clear()

#         # Destroy current frames
#         if hasattr(main_gui, "left_frame"):
#             main_gui.left_frame.destroy()
#         if hasattr(main_gui, "right_frame"):
#             main_gui.right_frame.destroy()

#         # Load new frames
#         main_gui.left_frame = left_class(main_gui.container_left, main_gui)
#         main_gui.left_frame.pack(fill="both", expand=True)

#         main_gui.right_frame = right_class(main_gui.container_right, main_gui)
#         main_gui.right_frame.pack(fill="both", expand=True)

#         # Update label
#         main_gui.page_label.config(text=page_name if page_name else left_class.__name__)


#     # def go_back(main_gui):
#     #     if main_gui.history:
#     #         left_class, right_class = main_gui.history.pop()
#     #         # ✅ Current ko forward_stack me save karo
#     #         main_gui.forward_stack.append((type(main_gui.left_frame), type(main_gui.right_frame)))

#     #         main_gui.left_frame.destroy()
#     #         main_gui.right_frame.destroy()

#     #         main_gui.left_frame = left_class(main_gui.container_left, main_gui)
#     #         main_gui.left_frame.pack(fill="both", expand=True)

#     #         main_gui.right_frame = right_class(main_gui.container_right, main_gui)
#     #         main_gui.right_frame.pack(fill="both", expand=True)

#     # def go_forward(main_gui):
#     #     if main_gui.forward_stack:
#     #         left_class, right_class = main_gui.forward_stack.pop()
#     #         # ✅ Current ko history me save karo
#     #         main_gui.history.append((type(main_gui.left_frame), type(main_gui.right_frame)))

#     #         main_gui.left_frame.destroy()
#     #         main_gui.right_frame.destroy()

#     #         main_gui.left_frame = left_class(main_gui.container_left, main_gui)
#     #         main_gui.left_frame.pack(fill="both", expand=True)

#     #         main_gui.right_frame = right_class(main_gui.container_right, main_gui)
#     #         main_gui.right_frame.pack(fill="both", expand=True)

#     # def go_home(main_gui):
#     #     # Clear history & forward stack
#     #     main_gui.history.clear()
#     #     main_gui.forward_stack.clear()

#     #     # Destroy current frames
#     #     main_gui.left_frame.destroy()
#     #     main_gui.right_frame.destroy()

#     #     # Load home frames (jaise pehle start hota hai)
#     #     from gui.home_left_frame import HomeLeft
#     #     from gui.home_right_frame import HomeRight
#     #     main_gui.left_frame = HomeLeft(main_gui.container_left, main_gui)
#     #     main_gui.left_frame.pack(fill="both", expand=True)

#     #     main_gui.right_frame = HomeRight(main_gui.container_right, main_gui)
#     #     main_gui.right_frame.pack(fill="both", expand=True)

#     def go_back(main_gui):
#         if main_gui.history:
#             # Current ko forward history me bhej do
#             main_gui.forward_history.append((
#                 main_gui.left_frame.__class__,
#                 main_gui.right_frame.__class__,
#                 main_gui.page_label.cget("text")
#             ))

#             last_left, last_right, last_name = main_gui.history.pop()

#             # Destroy current
#             main_gui.left_frame.destroy()
#             main_gui.right_frame.destroy()

#             # Restore last frames
#             main_gui.left_frame = last_left(main_gui.container_left, main_gui)
#             main_gui.left_frame.pack(fill="both", expand=True)

#             main_gui.right_frame = last_right(main_gui.container_right, main_gui)
#             main_gui.right_frame.pack(fill="both", expand=True)

#             # Update label
#             main_gui.page_label.config(text=last_name)


#     def go_forward(main_gui):
#         if main_gui.forward_history:
#             # Current ko history me bhej do
#             main_gui.history.append((
#                 main_gui.left_frame.__class__,
#                 main_gui.right_frame.__class__,
#                 main_gui.page_label.cget("text")
#             ))

#             next_left, next_right, next_name = main_gui.forward_history.pop()

#             # Destroy current
#             main_gui.left_frame.destroy()
#             main_gui.right_frame.destroy()

#             # Load next frames
#             main_gui.left_frame = next_left(main_gui.container_left, main_gui)
#             main_gui.left_frame.pack(fill="both", expand=True)

#             main_gui.right_frame = next_right(main_gui.container_right, main_gui)
#             main_gui.right_frame.pack(fill="both", expand=True)

#             # Update label
#             main_gui.page_label.config(text=next_name)


#     def go_home(main_gui):
#         # Clear histories
#         main_gui.history.clear()
#         main_gui.forward_history.clear()

#         # Destroy current
#         if hasattr(main_gui, "left_frame"):
#             main_gui.left_frame.destroy()
#         if hasattr(main_gui, "right_frame"):
#             main_gui.right_frame.destroy()

#         # Load default home frames
#         # apna import path lagana
#         # Load home frames (jaise pehle start hota hai)
#         from gui.home_left_frame import HomeLeft
#         from gui.home_right_frame import HomeRight

#         main_gui.left_frame = HomeLeft(main_gui.container_left, main_gui)
#         main_gui.left_frame.pack(fill="both", expand=True)

#         main_gui.right_frame = HomeRight(main_gui.container_right, main_gui)
#         main_gui.right_frame.pack(fill="both", expand=True)

#         # Update label
#         main_gui.page_label.config(text="Home")



# logic/switch_logic.py

class FrameSwitcher:
    # ---------- internal helpers ----------
    def _ensure(main_gui):
        if not hasattr(main_gui, "history"):
            main_gui.history = []
        if not hasattr(main_gui, "forward_stack"):
            main_gui.forward_stack = []
        if not hasattr(main_gui, "current_page_name"):
            main_gui.current_page_name = "Home"

    def _get_page_name(main_gui):
        # Only uses an internal attribute; no UI dependency
        return getattr(main_gui, "current_page_name", "Home")

    def _set_page_name(main_gui, name: str):
        # Always keep an internal source of truth
        main_gui.current_page_name = name
        # Best-effort update UI if present (label or topbar StringVar)
        if hasattr(main_gui, "page_label"):
            try:
                main_gui.page_label.config(text=name)
            except Exception:
                pass
        if hasattr(main_gui, "topbar") and hasattr(main_gui.topbar, "frame_name_var"):
            try:
                main_gui.topbar.frame_name_var.set(name)
            except Exception:
                pass

    def _destroy_current(main_gui):
        if hasattr(main_gui, "left_frame"):
            try:
                main_gui.left_frame.destroy()
            except Exception:
                pass
        if hasattr(main_gui, "right_frame"):
            try:
                main_gui.right_frame.destroy()
            except Exception:
                pass

    def _create(main_gui, left_class, right_class):
        main_gui.left_frame = left_class(main_gui.container_left, main_gui)
        main_gui.left_frame.pack(fill="both", expand=True)

        main_gui.right_frame = right_class(main_gui.container_right, main_gui)
        main_gui.right_frame.pack(fill="both", expand=True)

    # ---------- public API ----------
    def switch_right_frame_only(main_gui, right_class, page_name: str = None):
        """
        Sirf right frame change karo, history maintain + forward clear (browser-like)
        """
        FrameSwitcher._ensure(main_gui)

        # Save current state for Back (left & right class + page name)
        if hasattr(main_gui, "left_frame") and hasattr(main_gui, "right_frame"):
            main_gui.history.append((
                type(main_gui.left_frame),
                type(main_gui.right_frame),
                FrameSwitcher._get_page_name(main_gui),
            ))

        # New navigation => forward cleared
        main_gui.forward_stack.clear()

        # Replace only right frame
        if hasattr(main_gui, "right_frame"):
            try:
                main_gui.right_frame.destroy()
            except Exception:
                pass

        main_gui.right_frame = right_class(main_gui.container_right, main_gui)
        main_gui.right_frame.pack(fill="both", expand=True)

        # Optional page title update
        if page_name:
            FrameSwitcher._set_page_name(main_gui, page_name)

    def switch_frame(main_gui, left_class, right_class, page_name: str = None):
        """
        Dono frames switch karo (browser-like). Forward cleared on new nav.
        """
        FrameSwitcher._ensure(main_gui)

        # Save current to history if any
        if hasattr(main_gui, "left_frame") and hasattr(main_gui, "right_frame"):
            main_gui.history.append((
                type(main_gui.left_frame),
                type(main_gui.right_frame),
                FrameSwitcher._get_page_name(main_gui),
            ))

        # New navigation => forward cleared
        main_gui.forward_stack.clear()

        # Switch
        FrameSwitcher._destroy_current(main_gui)
        FrameSwitcher._create(main_gui, left_class, right_class)

        # Title
        title = page_name or getattr(left_class, "__name__", "Page")
        FrameSwitcher._set_page_name(main_gui, title)

    # Kept for naming parity; same as switch_frame
    def switch_both_frames(main_gui, left_class, right_class, page_name: str = None):
        FrameSwitcher.switch_frame(main_gui, left_class, right_class, page_name)

    def go_back(main_gui):
        """
        One step back: push current to forward, pop from history, restore.
        """
        FrameSwitcher._ensure(main_gui)
        if not main_gui.history:
            return

        # Push current to forward
        if hasattr(main_gui, "left_frame") and hasattr(main_gui, "right_frame"):
            main_gui.forward_stack.append((
                type(main_gui.left_frame),
                type(main_gui.right_frame),
                FrameSwitcher._get_page_name(main_gui),
            ))

        # Pop from history and restore
        left_class, right_class, page_name = main_gui.history.pop()

        FrameSwitcher._destroy_current(main_gui)
        FrameSwitcher._create(main_gui, left_class, right_class)
        FrameSwitcher._set_page_name(main_gui, page_name)

    def go_forward(main_gui):
        """
        One step forward: push current to history, pop from forward, restore.
        """
        FrameSwitcher._ensure(main_gui)
        if not main_gui.forward_stack:
            return

        # Push current to history
        if hasattr(main_gui, "left_frame") and hasattr(main_gui, "right_frame"):
            main_gui.history.append((
                type(main_gui.left_frame),
                type(main_gui.right_frame),
                FrameSwitcher._get_page_name(main_gui),
            ))

        # Pop from forward and restore
        left_class, right_class, page_name = main_gui.forward_stack.pop()

        FrameSwitcher._destroy_current(main_gui)
        FrameSwitcher._create(main_gui, left_class, right_class)
        FrameSwitcher._set_page_name(main_gui, page_name)

    def go_home(main_gui, left_home_class=None, right_home_class=None, title: str = "Home"):
        """
        Go to Home. You can:
        - Pass classes here, OR
        - Pre-set on main_gui: main_gui.home_left_class / main_gui.home_right_class
        """
        FrameSwitcher._ensure(main_gui)

        # Resolve home classes
        if left_home_class is None:
            left_home_class = getattr(main_gui, "home_left_class", None)
        if right_home_class is None:
            right_home_class = getattr(main_gui, "home_right_class", None)
        if not (left_home_class and right_home_class):
            print("go_home: home classes not configured. "
                  "Pass them to go_home(...) or set main_gui.home_left_class / home_right_class.")
            return

        # Reset stacks (true Home)
        main_gui.history.clear()
        main_gui.forward_stack.clear()

        FrameSwitcher._destroy_current(main_gui)
        FrameSwitcher._create(main_gui, left_home_class, right_home_class)
        FrameSwitcher._set_page_name(main_gui, title)
