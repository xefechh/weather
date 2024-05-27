# Authors: Artem Kii, Gaabriel Ponomarjov

# Imports
from customtkinter import *

class WeatherApp(CTk):
    def __init__(self):
        super().__init__()

    def setup_ui(self, a):
        self.title("Weather APP")

        set_appearance_mode("Dark")

        # Создаем холст с заданными размерами
        self.canvas = CTkCanvas(self, width=1000, height=600 , bg = "#000000", highlightthickness=0)
        self.canvas.pack()

        # Отрисовка всех квадратов
        self.draw_square(30, 60, 240, 250, text=a)
        self.draw_square(30, 306, 240, 576, text="5 days forecast")
        self.draw_square(270, 60, 970, 440)
        
        # Отрисовка временных слотов
        time_slots = [
            (270, 476, 348.75, 576),
            (358.75, 476, 437.5, 576),
            (447.5, 476, 526.25, 576),
            (536.25, 476, 615, 576),
            (625, 476, 703.75, 576),
            (713.75, 476, 792.5, 576),
            (802.5, 476, 881.25, 576),
            (891.25, 476, 970, 576),
        ]
        for x1, y1, x2, y2 in time_slots:
            self.draw_square(x1, y1, x2, y2)

    def draw_square(self, x1, y1, x2, y2, text=""):
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="#333333")
        if text:
            # Добавляем текст в центр квадрата
            x_center = (x1 + x2) / 2
            y_center = (y1 + y2) / 2
            self.canvas.create_text(x_center, y_center, text=text, fill="white", font=("Arial", 16, "bold"))

