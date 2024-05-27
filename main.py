import tkinter as tk
from game.quiz_level_frame import QuizLevelFrame
from game.frame_level_soal.frame_level_soal1 import FrameLevelSoal1
from game.frame_level_soal.frame_level_soal2 import FrameLevelSoal2
from game.frame_level_soal.frame_level_soal3 import FrameLevelSoal3
from game.frame_level_soal.frame_level_soal4 import FrameLevelSoal4
from game.frame_level_soal.frame_level_soal5 import FrameLevelSoal5
from game.frame_level_soal.frame_level_soal6 import FrameLevelSoal6
from game.frame_level_soal.frame_level_soal7 import FrameLevelSoal7
from game.frame_level_soal.frame_level_soal8 import FrameLevelSoal8
from game.frame_level_soal.frame_level_soal9 import FrameLevelSoal9
from game.frame_level_soal.frame_level_soal10 import FrameLevelSoal10

class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Indonesia Culture Quiz")
        self.master.geometry("800x500")

        # Create a container frame
        self.container = tk.Frame(master)
        self.container.pack(fill='both', expand=True)

        # Create the main menu frame
        self.main_menu_frame = tk.Frame(self.container)
        self.main_menu_frame.pack(fill='both', expand=True)

        # Add welcome label
        self.welcome_label = tk.Label(self.main_menu_frame, text="Selamat datang di gim kombinasi", font=("Helvetica", 16))
        self.welcome_label.pack(pady=20)

        # Configure the buttons with larger width and centered alignment
        self.start_button = tk.Button(self.main_menu_frame, text="Mulai", command=self.show_quiz_levels, width=20)
        self.start_button.pack(pady=10)

        self.exit_button = tk.Button(self.main_menu_frame, text="Keluar", command=self.master.quit, width=20)
        self.exit_button.pack(pady=10)

        # Create frames for each quiz level
        self.level_selection_frame = QuizLevelFrame(self.container, self.show_soal, self.show_main_menu)

        # Create frames for each quiz level (assuming there are 10 levels)
        self.soal_frames = [
            FrameLevelSoal1(self.container, self.show_quiz_levels),
            FrameLevelSoal2(self.container, self.show_quiz_levels),
            FrameLevelSoal3(self.container, self.show_quiz_levels),
            FrameLevelSoal4(self.container, self.show_quiz_levels),
            FrameLevelSoal5(self.container, self.show_quiz_levels),
            FrameLevelSoal6(self.container, self.show_quiz_levels),
            FrameLevelSoal7(self.container, self.show_quiz_levels),
            FrameLevelSoal8(self.container, self.show_quiz_levels),
            FrameLevelSoal9(self.container, self.show_quiz_levels),
            FrameLevelSoal10(self.container, self.show_quiz_levels)
        ]

    def show_quiz_levels(self):
        self.hide_all_frames()
        self.level_selection_frame.pack(fill='both', expand=True)

    def show_soal(self, level):
        self.hide_all_frames()
        self.soal_frames[level - 1].pack(fill='both', expand=True)

    def show_main_menu(self):
        self.hide_all_frames()
        self.main_menu_frame.pack(fill='both', expand=True)

    def hide_all_frames(self):
        self.main_menu_frame.pack_forget()
        self.level_selection_frame.pack_forget()
        for frame in self.soal_frames:
            frame.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
