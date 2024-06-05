from customtkinter import *
from PIL import Image
import requests
from datetime import datetime
api = '58ece528195235057712455ac755125d'
app = CTk()
app.geometry("300x400")
app._set_appearance_mode("dark")
app.resizable(False, False)
app.title("Погода")

def on_enter(event):
    search_button.configure(bg_color='#2D2726')

def on_leave(event):
    search_button.configure(bg_color='#242424')

def on_click(event):
    search_button.configure(bg_color='#242424')

class server_handling:
    def search_click():
        entered_city = search.get()
        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={entered_city}&units=imperial&APPID={api}")
        with open("history.txt", 'a') as file:
                file.write(f"{(search.get()).upper()}: \n")
        if weather_data.json()['cod'] == '404':
            result_label.configure(text="No city found")
            with open("history.txt", 'a') as file:
                file.write(f"No city found\n\n")
        else:
            weather = weather_data.json()['weather'][0]['main']
            temp = round((weather_data.json()['main']['temp']))
            temp_celsius = round(5/9 * (temp - 32), 1)
            temp_celsius = int(temp_celsius)
            result_text = f"{temp_celsius}°C"
            result_label.configure(text=result_text)
            weather_result = f"{weather}"
            weather_label.configure(text=weather_result)
            
            humidity = weather_data.json()['main']['humidity']
            humidity_result = f"Humidity: \n{humidity}%"
            humidity_label.configure(text=humidity_result)
            
            wind_speed = weather_data.json()['wind']['speed']
            wind_result = f"Wind Speed:\n{wind_speed} m/s"
            wind_label.configure(text=wind_result)
            with open("history.txt", 'a') as file:
                timemine = datetime.now()
                file.write(f"Time: {timemine.strftime('%H:%M:%S')}\nWeather: {weather}\nTemperature: {temp}\nHumidity: {humidity}\nWind Speed: {wind_speed}\n\n")

                

frame = CTkFrame(app)
frame.pack(pady=10, anchor='w', padx=10)

search = CTkEntry(frame, font=("Helvetica", 18), text_color='#FFFFFF', placeholder_text='SEARCH', corner_radius=15, width=250, height=30, fg_color='#242424', border_width=1, bg_color='#242424')
search.grid(row=0, column=0)
search_icon = CTkImage(light_image=Image.open("C:\JPTV23\Git\weather\search_icon.png"), dark_image=Image.open("C:\JPTV23\Git\weather\search_icon.png"))

search_button = CTkButton(frame, text='', image=search_icon, width=30, height=30, command=server_handling.search_click, corner_radius=5, fg_color='#242424', bg_color='#242424')
search_button.bind("<Enter>", on_enter)
search_button.bind("<Leave>", on_leave)
search_button.bind("<Button-1>", on_click)
search_button.grid(row=0, column=1)

result_label = CTkLabel(app, text="", font=("Bauhaus 93", 56), width=280, height=56, fg_color='#242424', bg_color='#242424', text_color='#FFFFFF', wraplength=200)
result_label.pack(pady=(100, 0), padx=10)

weather_label = CTkLabel(app, text="", font=("Montserrat", 18), width=280, height=24, justify="center", fg_color='#242424', bg_color='#242424', text_color='#FFFFFF')
weather_label.pack(pady=0)

humidity_label = CTkLabel(app, text="", font=("Montserrat", 18), width=60, height=60, justify="left", fg_color='#242424', bg_color='#242424', text_color='#FFFFFF')
humidity_label.place(x=20, y = 330)

wind_label = CTkLabel(app, text="", font=("Montserrat", 18), width=60, height=60, justify="right", fg_color='#242424', bg_color='#242424', text_color='#FFFFFF')
wind_label.place(x=175, y=330)

app.mainloop()