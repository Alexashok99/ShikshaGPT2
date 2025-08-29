import csv
import random
from models import Question

class QuizController:
    """
    Loads questions from CSV and manages quiz state.
    CSV Format (UTF-8, header included):
    question, option_a, option_b, option_c, option_d, answer
    answer must be A/B/C/D
    """
    def __init__(self, csv_path):
        self.questions = self._load_csv(csv_path)
        random.shuffle(self.questions)
        self.index = 0
        self.score = 0

    def _load_csv(self, path):
        out = []
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                q = row["question"].strip()
                opts = [row["option_a"].strip(), row["option_b"].strip(),
                        row["option_c"].strip(), row["option_d"].strip()]
                ans_letter = row["answer"].strip().upper()
                ans_idx = {"A":0, "B":1, "C":2, "D":3}.get(ans_letter, 0)
                out.append(Question(q, opts, ans_idx))
        return out

    def has_next(self):
        return self.index < len(self.questions)

    def current(self):
        if not self.has_next():
            return None
        return self.questions[self.index]

    def submit(self, selected_index):
        """Update score, advance index; returns (correct: bool, correct_index: int)"""
        q = self.current()
        correct = (selected_index == q.answer_index)
        if correct:
            self.score += 1
        self.index += 1
        return correct, q.answer_index

    def result(self):
        return self.score, len(self.questions)
