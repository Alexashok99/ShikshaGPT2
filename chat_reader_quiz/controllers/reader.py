import threading
import time
import queue

class ReaderController:
    """
    Reads a UTF-8 text file line-by-line in a background thread and
    notifies UI via callbacks.
    """
    def __init__(self, file_path, on_line, on_done, line_delay_ms=500):
        self.file_path = file_path
        self.on_line = on_line
        self.on_done = on_done
        self.line_delay = line_delay_ms / 1000.0
        self._thread = None
        self._stop = False

    def start_stream(self):
        if self._thread and self._thread.is_alive():
            return
        self._stop = False
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def stop(self):
        self._stop = True

    def _run(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                for raw in f:
                    if self._stop:
                        break
                    line = raw.strip()
                    if line:
                        # push line to UI queue
                        self.on_line(line)
                        time.sleep(self.line_delay)
        finally:
            # inform UI that we are done
            self.on_done()
