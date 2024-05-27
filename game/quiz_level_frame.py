import tkinter as tk

class QuizLevelFrame(tk.Frame):
    def __init__(self, master, show_soal_callback, show_main_menu_callback):
        super().__init__(master)
        self.show_soal_callback = show_soal_callback
        self.show_main_menu_callback = show_main_menu_callback

        # Configure background color
        self.configure(bg="#f0f0f0")

        # Add title label
        self.title_label = tk.Label(self, text="Pilih Quiz", font=("Helvetica", 18), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        # Create a frame to contain level selection buttons
        self.level_selection_frame = tk.Frame(self, bg="#f0f0f0")
        self.level_selection_frame.pack(fill='both', expand=True)

        # Add level buttons in a grid layout (2 rows and 3 columns)
        self.level_buttons = []
        for i in range(10):
            button = tk.Button(self.level_selection_frame, text=f"Kuis Level {i + 1}", command=lambda i=i: self.show_soal(i + 1), width=20, font=("Helvetica", 12), bg="#2196f3", fg="white")
            self.level_buttons.append(button)
            button.grid(row=i//3, column=i%3, padx=40, pady=10)

        # Add back button in the level selection frame with red color
        self.back_button = tk.Button(self.level_selection_frame, text="Kembali", command=self.show_main_menu, width=20, font=("Helvetica", 12), bg="#f44336", fg="white")
        self.back_button.grid(row=6, column=1, pady=20)  # Adjust the row and column as needed

    def show_soal(self, level):
        self.show_soal_callback(level)

    def show_main_menu(self):
        self.show_main_menu_callback()
