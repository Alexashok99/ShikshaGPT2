
# # logic/reader_controller.py

# import threading
# import time
# from queue import Queue

# class ReaderController:
#     def __init__(self, file_path, display_callback, completion_callback=None):
#         self.file_path = file_path
#         self.display_callback = display_callback
#         self.completion_callback = completion_callback
#         self._is_reading = False
#         self._is_paused = False
#         self._stop_requested = False
#         self.reading_thread = None
#         self.current_position = 0
#         self.lines = []
        
#         # Load file content
#         self.load_file()

#     def load_file(self):
#         """Load the file content into memory"""
#         try:
#             with open(self.file_path, 'r', encoding='utf-8') as file:
#                 self.lines = file.readlines()
#             print(f"Loaded {len(self.lines)} lines from {self.file_path}")
#         except Exception as e:
#             print(f"Error loading file: {e}")
#             self.lines = []

#     def start_reading(self):
#         """Start reading the file"""
#         if not self._is_reading and self.lines:
#             self._is_reading = True
#             self._is_paused = False
#             self._stop_requested = False
#             self.reading_thread = threading.Thread(target=self._read_file)
#             self.reading_thread.daemon = True
#             self.reading_thread.start()

#     def pause_reading(self):
#         """Pause the reading"""
#         self._is_paused = True

#     def resume_reading(self):
#         """Resume the reading"""
#         self._is_paused = False

#     def restart_reading(self):
#         """Restart reading from the beginning"""
#         self.stop_reading()
#         self.current_position = 0
#         time.sleep(0.1)  # Brief pause to ensure clean restart
#         self.start_reading()

#     def stop_reading(self):
#         """Stop reading completely"""
#         self._stop_requested = True
#         self._is_reading = False
#         self._is_paused = False
#         if self.reading_thread and self.reading_thread.is_alive():
#             self.reading_thread.join(timeout=1.0)

#     def _read_file(self):
#         """Main reading loop (runs in separate thread)"""
#         reading_speed = 0.05  # Adjust this value to control reading speed
        
#         while self.current_position < len(self.lines) and not self._stop_requested:
#             if not self._is_paused:
#                 line = self.lines[self.current_position].strip()
#                 if line:  # Only process non-empty lines
#                     self.display_callback(line)
                
#                 self.current_position += 1
#                 time.sleep(reading_speed)
#             else:
#                 time.sleep(0.1)  # Small sleep when paused
        
#         # Reading completed
#         self._is_reading = False
#         if self.current_position >= len(self.lines) and self.completion_callback:
#             self.completion_callback()





# logic/reader_controller.py

import threading
import time

class ReaderController:
    def __init__(self, file_path, display_callback, completion_callback=None):
        """
        :param file_path: Path of file to read
        :param display_callback: Function to call for each line (e.g. ShowText.enqueue_line)
        :param completion_callback: Function to call when file reading completes
        """
        self.file_path = file_path
        self.display_callback = display_callback
        self.completion_callback = completion_callback

        self._is_reading = False
        self._is_paused = False
        self._stop_requested = False
        self.reading_thread = None
        self.current_position = 0
        self.lines = []
        
        # Load file content
        self.load_file()

    def load_file(self):
        """Load the file content into memory"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.lines = [line.strip() for line in file if line.strip()]
            print(f"✅ Loaded {len(self.lines)} lines from {self.file_path}")
        except Exception as e:
            print(f"❌ Error loading file: {e}")
            self.lines = []

    def start_reading(self):
        """Start reading the file (like Play button)"""
        if not self._is_reading and self.lines:
            self._is_reading = True
            self._is_paused = False
            self._stop_requested = False
            self.reading_thread = threading.Thread(target=self._read_file, daemon=True)
            self.reading_thread.start()

    def pause_reading(self):
        """Pause the reading"""
        if self._is_reading:
            self._is_paused = True

    def resume_reading(self):
        """Resume the reading"""
        if self._is_reading:
            self._is_paused = False

    # def restart_reading(self):
    #     """Restart reading from the beginning"""
    #     self.stop_reading()
    #     self.current_position = 0
    #     time.sleep(0.1)  # Brief pause to ensure clean restart
    #     self.start_reading()

    def restart_reading(self):
        """Restart reading from the beginning"""
        self.stop_reading()
        self.current_position = 0
        
        # Clear previous chat bubbles (if display is ShowText)
        if hasattr(self.display_callback, "__self__"):  
            widget = self.display_callback.__self__
            if hasattr(widget, "clear"):
                widget.clear()
        
        time.sleep(0.1)  # Brief pause to ensure clean restart
        self.start_reading()


    def stop_reading(self):
        """Stop reading completely"""
        self._stop_requested = True
        self._is_reading = False
        self._is_paused = False

    def _read_file(self):
        """Main reading loop (runs in separate thread)"""
        delay_between_lines = 0.4  # time gap between two chat bubbles (in seconds)
        
        while self.current_position < len(self.lines) and not self._stop_requested:
            if not self._is_paused:
                line = self.lines[self.current_position]
                self.display_callback(line)   # <-- ShowText.enqueue_line()
                self.current_position += 1
                time.sleep(delay_between_lines)
            else:
                time.sleep(0.1)  # Small sleep when paused
        
        # Reading completed
        self._is_reading = False
        if self.current_position >= len(self.lines) and not self._stop_requested:
            if callable(self.completion_callback):
                self.completion_callback()   # <-- ShowText.file_done()
