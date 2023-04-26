import requests

API_KEY = "06486787f1cb5505bfa4c3d1855c6b3e"


def get_data(place, forecast_days=None, type_of_weather=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    return content


if __name__ == "__main__":
    print(get_data(place="London"))
