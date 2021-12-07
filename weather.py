import requests


def get_weather_desc_and_temp():
    api_key = ""
    city = "Lehi"

    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"
    # api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=

    response = requests.get(url)
    json = response.json()

    description = json.get("weather")[0].get("description")

    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {
        'description': description,
        'temp_min': temp_min,
        'temp_max': temp_max
    }

def main():
    weather_dict = get_weather_desc_and_temp()
    print("Today's forecast is", weather_dict['description'])
    print("The minimum temp is", weather_dict['temp_min'])
    print("The maximum temp is", weather_dict['temp_max'])
main()