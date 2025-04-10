import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import app
 
# Mock genre list
genres = ["Math", "Science", "History", "Geography", "Sports"]

def show_settings_screen():
    window = tk.Tk()
    window.title("Quiz Settings")
    window.geometry("900x500")
    window.configure(bg='white')

    # Delay Input (in minutes)
    tk.Label(window, text="Quiz Inteverals (minutes):", font=("Arial", 12), bg='white').pack(pady=5)
    delay_entry = tk.Entry(window, font=("Arial", 12))
    # delay_entry.insert(0, "1")  # Default: 1 minute
    delay_entry.pack(pady=5)

    # Duration Input (in minutes)
    tk.Label(window, text="Quiz Duration (minutes):", font=("Arial", 12), bg='white').pack(pady=5)
    duration_entry = tk.Entry(window, font=("Arial", 12))
    # duration_entry.insert(0, "5")  # Default: 5 minutes
    duration_entry.pack(pady=5)
 
    # Genre Dropdown
    tk.Label(window, text="Select Subject:", font=("Arial", 12), bg='white').pack(pady=5)
    genre_var = tk.StringVar()
    genre_var.set(genres[0])
    genre_menu = tk.OptionMenu(window, genre_var, *genres)
    genre_menu.config(font=("Arial", 12))
    genre_menu.pack(pady=5)

    # Function to start the quiz
    def start_quiz():
        delay = delay_entry.get()
        duration = duration_entry.get()

        genre = genre_var.get()

        try:
            delay_minutes = float(delay)
            duration_minutes = float(duration)

            delay_seconds = delay_minutes * 60
            duration_seconds = duration_minutes * 60

            # Close the settings window
            window.destroy()

            # Execute app.py with the collected inputs
            app.start_quiz_loop(genre, delay_seconds, duration_seconds)

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for delay and duration.")

    # Start Quiz Button
    tk.Button(window, text="Start Quiz", font=("Arial", 12), command=start_quiz).pack(pady=20)

    window.mainloop()

# Run the settings screen
show_settings_screen()
  
