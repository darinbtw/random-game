import tkinter as tk
from tkinter import messagebox
import random

def check_guess():
    guess = int(guess_entry.get())
    if guess < secret_number:
        messagebox.showinfo("Результат", "Мое число больше, чем твое. Попробуй еще раз!")
    elif guess > secret_number:
        messagebox.showinfo("Результат", "Мое число меньше, чем твое. Попробуй еще раз!")
    else:
        messagebox.showinfo("Поздравляем!", f"Ты угадал число {secret_number} за {attempts} попыток!")
        window.quit()

def start_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    messagebox.showinfo("Игра началась!", "Привет! Я загадал число от 0 до 100. Попробуй угадать его!")
    guess_entry.delete(0, tk.END)

window = tk.Tk()
window.title("Угадай число")

secret_number = 0
attempts = 0

guess_label = tk.Label(window, text="Введи свою догадку:")
guess_label.pack()

guess_entry = tk.Entry(window)
guess_entry.pack()

check_button = tk.Button(window, text="Проверить", command=check_guess)
check_button.pack()

start_button = tk.Button(window, text="Начать игру", command=start_game)
start_button.pack()

window.mainloop()
