from customtkinter import *
from PIL import Image
import requests

api = '58ece528195235057712455ac755125d'
app = CTk()
app.geometry("300x400")
app._set_appearance_mode("dark")

def search_click():
    entered_city = search.get()
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={entered_city}&units=imperial&APPID={api}")
    if weather_data.json()['cod'] == '404':
        result_label.configure(text="No city found")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        temp_celsius = round(5/9 * (temp - 32), 2)

        result_text = f"{temp_celsius}°C"
        result_label.configure(text=result_text)

# Create a frame to contain the search box and the icon
frame = CTkFrame(app)
frame.pack(pady=10, anchor='w', padx=10)

# Create the search entry
search = CTkEntry(frame, font=("Helvetica", 18), placeholder_text='SEARCH', width=250, height=30)
search.grid(row=0, column=0)

# Load the search icon
search_icon = CTkImage(light_image=Image.open("search_icon.png"), dark_image=Image.open("search_icon.png"))

# Create a button for the icon and place it to the right of the search entry
search_button = CTkButton(frame, text='', image=search_icon, width=30, height=30, command=search_click, corner_radius=0)
search_button.grid(row=0, column=1)

# Create a label to display the weather information
result_label = CTkLabel(app, text="", font=("Bauhaus 93", 56), width=280, height=220, wraplength=280, justify="center")
result_label.pack(pady=20, padx=10)

app.mainloop()
