import requests
from bs4 import BeautifulSoup

def get_next_five_days_temperatures(city):
    url = f"https://www.weather-forecast.com/locations/{city}/forecasts/latest"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        temperature_elements = soup.find_all(class_='temp')
        temperatures = [temp.text.strip() for temp in temperature_elements[:5]]  # Получаем температуры на следующие 5 дней
        print(f"Temperatures in {city} for the next five days:")
        for temp in temperatures:
            print(temp)
    else:
        print("Error: Failed to retrieve weather data.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_next_five_days_temperatures(city)


