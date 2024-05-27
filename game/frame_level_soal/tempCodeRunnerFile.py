import tkinter as tk
from ..quiz import QuizApp

class FrameLevelSoal1(tk.Frame):
    def __init__(self, master, back_callback):
        super().__init__(master)
        quiz_app = QuizApp(self, back_callback, 'assets/level_soal1.txt')
        quiz_app.pack(fill='both', expand=True)
