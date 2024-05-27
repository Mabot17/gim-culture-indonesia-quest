import tkinter as tk
from game.quiz import QuizApp

class FrameLevelSoal1(tk.Frame):
    def __init__(self, master, back_callback):
        super().__init__(master)
        quiz_app = QuizApp(self, back_callback, 'level_soal1.txt', 'img/bg.jpg')
        quiz_app.pack(fill='both', expand=True)
