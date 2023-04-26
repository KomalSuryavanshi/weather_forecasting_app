import requests

API_KEY = "06486787f1cb5505bfa4c3d1855c6b3e"


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()

    # filtering data according to forecast days
    filtered_content = content["list"]
    no_of_values = 8 * forecast_days  # 8 because 8 observations are seen in 24 hours so 8 * no of forecast days
    filtered_content = filtered_content[:no_of_values]
    return filtered_content


if __name__ == "__main__":
    print(get_data(place="London",forecast_days=3))
