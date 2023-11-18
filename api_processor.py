import os
import requests

from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API")

def get_data(place,days,option):
    URL = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(URL).json()
    data_list = response['list']
    num_of_data_points = days * 8
    filtered_data = data_list[:num_of_data_points]
    if option == "Temperature":
        temp_list = [data['main']['temp'] for data in filtered_data]
        return temp_list
    elif option == "Sky":
        sky_list = [data['weather'][0]['main'] for data in filtered_data]
        return sky_list

if __name__ == "__main__":
    print(get_data("tokyo",5,"Temperature"))