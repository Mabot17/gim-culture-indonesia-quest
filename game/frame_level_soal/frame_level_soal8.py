import tkinter as tk
from game.quiz import QuizApp

class FrameLevelSoal8(tk.Frame):
    def __init__(self, master, back_callback):
        super().__init__(master)
        quiz_app = QuizApp(self, back_callback, 'level_soal8.txt')
        quiz_app.pack(fill='both', expand=True)
