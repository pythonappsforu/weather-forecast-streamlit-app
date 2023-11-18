import os
import requests

from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API")

def get_data(place,days):
    URL = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(URL).json()
    print(response)
    if response['cod'] == '200':
        data_list = response['list']
        num_of_data_points = days * 8
        filtered_data = data_list[:num_of_data_points]
        status = "200"
        return filtered_data,status
    else:
        status = response['cod']
        return response['message'],status

if __name__ == "__main__":
    print(get_data("tokyo",5,"Temperature"))