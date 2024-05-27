import tkinter as tk
import os

class FrameLevelSoal1(tk.Frame):
    def __init__(self, master, back_callback):
        super().__init__(master)
        self.back_callback = back_callback

        # Mendapatkan path ke direktori assets
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(script_dir, '..', '..'))
        questions_path = os.path.join(project_root, 'assets', 'level_soal1.txt')

        # Load questions from the specified file
        self.questions = self.load_questions(questions_path)
        self.question_index = 0
        self.score = 0

        self.create_widgets()

    def create_widgets(self):
        # Add title label
        self.title_label = tk.Label(self, text="Pilih Quiz", font=("Helvetica", 18), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        # Display question
        self.question_label = tk.Label(self, text="", font=("Helvetica", 14), wraplength=400, bg="#f0f0f0")
        self.question_label.pack(pady=20)

        # Frame for answer buttons
        self.answer_frame = tk.Frame(self, bg="#f0f0f0")
        self.answer_frame.pack(pady=10)

        # Answer buttons
        self.answer_buttons = []
        for i in range(4):
            button = tk.Button(self.answer_frame, text="", command=lambda i=i: self.check_answer(i), width=20, font=("Helvetica", 12), bg="#2196f3", fg="white")
            self.answer_buttons.append(button)
            button.grid(row=i//2, column=i%2, padx=5, pady=5)

        # Result label
        self.result_label = tk.Label(self, text="", font=("Helvetica", 12), bg="#f0f0f0")
        self.result_label.pack(pady=10)

        # Back button
        self.back_button = tk.Button(self, text="Kembali", command=self.back_callback, width=20, font=("Helvetica", 12), bg="#f44336", fg="white")
        self.back_button.pack(pady=10)

        self.show_question()

    def load_questions(self, filepath):
        with open(filepath, 'r') as file:
            lines = file.readlines()
        questions = [line.strip().split('|') for line in lines]
        return questions

    def show_question(self):
        if self.question_index < len(self.questions):
            self.question_label.config(text=f"Pertanyaan {self.question_index + 1}: {self.questions[self.question_index][0]}")
            for i, button in enumerate(self.answer_buttons):
                button.config(text=self.questions[self.question_index][i + 1])
            self.result_label.config(text="")
        else:
            self.question_label.config(text="Kuis selesai!")
            self.result_label.config(text=f"Skor Anda: {self.score}")

    def check_answer(self, selected_index):
        selected_answer = self.answer_buttons[selected_index].cget("text")
        correct_answer = self.questions[self.question_index][1]
        if selected_answer == correct_answer:
            self.score += 1
            self.result_label.config(text="Benar!", fg="green")
        else:
            self.result_label.config(text=f"Salah! Jawaban yang benar adalah {correct_answer}", fg="red")
        self.question_index += 1
        self.show_question()
