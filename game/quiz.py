import tkinter as tk
from PIL import Image, ImageTk
import os

class QuizApp(tk.Frame):
    def __init__(self, master, back_callback, questions_file, background_image_path=None):
        super().__init__(master)
        self.back_callback = back_callback

        # Load questions from the specified file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(script_dir, '..'))
        questions_path = os.path.join(project_root, 'assets', questions_file)

        self.questions = self.load_questions(questions_path)
        self.current_question = None
        self.score = 0
        self.question_index = 0

        # Configure the main frame
        self.configure(bg="#f0f0f0")

        # Add background image if provided
        if background_image_path:
            background_image_full_path = os.path.join(project_root, 'assets', background_image_path)
            self.background_image = Image.open(background_image_full_path)
            self.background_photo = ImageTk.PhotoImage(self.background_image)
            self.background_label = tk.Label(self, image=self.background_photo)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Add a header label
        self.header_label = tk.Label(self, text="Kuis Level", font=("Helvetica", 18, "bold"), bg="#4caf50", fg="white")
        self.header_label.pack(fill="x")

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

        self.next_question()

    def load_questions(self, filepath):
        with open(filepath, 'r') as file:
            lines = file.readlines()
        questions = [line.strip().split('|') for line in lines]
        return questions

    def next_question(self):
        if self.question_index < len(self.questions):
            self.current_question = self.questions[self.question_index]
            self.question_label.config(text=f"Pertanyaan {self.question_index + 1}: {self.current_question[0]}")
            # Assume the question format is: "Question|Correct Answer|Option A|Option B|Option C|Option D"
            options = self.current_question[2:6]
            for i, button in enumerate(self.answer_buttons):
                button.config(text=options[i])
            self.result_label.config(text="")
        else:
            self.question_label.config(text="Kuis selesai!")
            self.result_label.config(text=f"Skor Anda: {self.score}")

    def check_answer(self, selected_index):
        selected_answer = self.answer_buttons[selected_index].cget("text")
        if selected_answer == self.current_question[1]:
            self.score += 1
            self.result_label.config(text="Benar!", fg="green")
        else:
            self.result_label.config(text=f"Salah! Jawaban yang benar adalah {self.current_question[1]}", fg="red")
        self.question_index += 1
        self.next_question()
