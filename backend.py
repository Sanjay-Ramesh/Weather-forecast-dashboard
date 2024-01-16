import requests

API_KEY = "1a9b7b3703ece8140d7c35c82d034d52"


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    print(data)
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]   
    return filtered_data

if __name__ == "__main__":
    print(get_data(place = "Tokyo",forecast_days=3))