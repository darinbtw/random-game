import tkinter as tk
from tkinter import messagebox
import random
import json

# Загрузка конфигурационных данных
def load_config():
    try:
        with open("config.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"nickname": "Anonymous", "score": 0}

# Сохранение конфигурационных данных
def save_config(config):
    with open("config.json", "w") as file:
        json.dump(config, file)

def start_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    messagebox.showinfo("Игра началась!", "Привет! Я загадал число от 1 до 100. Попробуй угадать его!")
    guess_entry.delete(0, tk.END)

def check_guess(event=None):
    global attempts, score
    guess = guess_entry.get()
    if guess.isdigit():
        guess = int(guess)
        attempts += 1
        if guess < secret_number:
            messagebox.showinfo("Результат", "Мое число больше, чем твое. Попробуй еще раз!")
        elif guess > secret_number:
            messagebox.showinfo("Результат", "Мое число меньше, чем твое. Попробуй еще раз!")
        else:
            messagebox.showinfo("Поздравляем!", f"Ты угадал число {secret_number} за {attempts} попыток!")
            score += 6
            config["score"] = score
            save_config(config)  # Сохраняем только счет в конфигурационный файл
            update_score_label()
            start_game()  # Генерируем новое число после победы
    else:
        messagebox.showerror("Ошибка", "Пожалуйста, введите только число.")

def update_score_label():
    score_label.config(text=f"Счет: {config['score']}")

def buy_hint():
    global score
    if config['score'] >= 10:  # Устанавливаем стоимость подсказки в 10 баллов
        hint_range = (max(secret_number - 5, 1), min(secret_number + 5, 100))
        messagebox.showinfo("Подсказка", f"Число находится в диапазоне от {hint_range[0]} до {hint_range[1]}.")
        config['score'] -= 10
        score = config['score']
        update_score_label()
    else:
        messagebox.showinfo("Ошибка", "У вас недостаточно баллов для покупки подсказки.")

def open_shop_window():
    shop_window = tk.Toplevel(window)
    shop_window.title("Магазин")
    hint_button = tk.Button(shop_window, text="Купить подсказку", command=buy_hint)
    hint_button.pack()

# Окно
window = tk.Tk()
window.title("Угадай число")

# Загрузка конфигурации при запуске
config = load_config()
score = config['score']

secret_number = random.randint(1, 100)
attempts = 0

# Метка и поле для ввода числа
guess_label = tk.Label(window, text="Введи свою догадку:")
guess_label.pack()

guess_entry = tk.Entry(window)
guess_entry.pack()

# Связываем нажатие Enter с функцией check_guess()
guess_entry.bind('<Return>', check_guess)

# Кнопки
check_button = tk.Button(window, text="Проверить", command=check_guess)
check_button.pack()

start_button = tk.Button(window, text="Начать игру", command=start_game)
start_button.pack()

score_label = tk.Label(window, text=f"Счет: {config['score']}")
score_label.pack()

shop_button = tk.Button(window, text="Магазин", command=open_shop_window)
shop_button.pack()

window.mainloop()
