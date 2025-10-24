import requests

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.show_weather(data)
        else:
            print("Error fetching data. Please check the city name or your API key.")

    def show_weather(self, data):
        city = data['name']
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        print(f"\nWeather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather}")

    def my_UI(self):
        while True:
            city = input("\nEnter city name (or 'quit' to exit): ").strip()
            if city.lower() == 'quit':
                print("Goodbye!")
                break
            self.get_weather(city)


my_api_key = "8b349dd2fc1e4351d48a65e3da2d8e86"
app = WeatherApp(my_api_key)
app.my_UI()
