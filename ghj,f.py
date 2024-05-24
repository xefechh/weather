from customtkinter import *

class SquareApp(CTk):
    def __init__(self):
        super().__init__()
        self.von()  # Вызов метода для инициализации окна
    
    def von(self):
        self.title("Weather APP")

        # Создаем холст с заданными размерами
        self.canvas = CTkCanvas(self, width=1000, height=600)
        self.canvas.pack()

        set_appearance_mode("Dark")

    def fig(self, x1, y1, x2, y2):
        # Указываем координаты для квадрата
        self.x1, self.y1 = x1, y1  # Верхний левый угол
        self.x2, self.y2 = x2, y2  # Нижний правый угол

        self.draw_square(x1, y1, x2, y2)

    def draw_square(self, x1, y1, x2, y2):
        self.canvas.create_rectangle(x1, y1, x2, y2, corner_radius=10, fill="#333333")

app = SquareApp()
app.fig(30,60,240,250)
app.fig(30,306,240,576)
app.fig(270,60,970,440)
app.fig(270,476,348.75,576)
app.fig(358.75,476,437.5,576)
app.fig(447.5,476,526.25,576)
app.fig(536.25,476,615,576)
app.fig(625,476,703.75,576)
app.fig(713.75,476,792.5,576)
app.fig(802.5,476,881.25,576)
app.fig(891.25,476,970,576)
app.mainloop()





