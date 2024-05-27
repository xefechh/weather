import requests
from bs4 import BeautifulSoup
from main import WeatherApp

def get_current_temperature(city):
    url = f"https://www.weather-forecast.com/locations/{city}/forecasts/latest"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        temperature = soup.find(class_='temp').text.strip()
        # Преобразовываем температуру в целое число (если она представлена в виде строки)
        temperature = str(temperature)
        # Создаем экземпляр класса WeatherApp и передаем температуру в качестве аргумента для метода mainloop()
        return str(temperature)
    else:
        print("Error: Failed to retrieve weather data.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    a = get_current_temperature(city)
#   Tallinn
#   London


app = WeatherApp()
app.setup_ui(a)
app.mainloop()










