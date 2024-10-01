#youssef hussein mohamed
#212103168 
import requests, json

city_name = input("please enter name of city ")

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={"69a6badb36a747e811328b682c71095e"}'

R = requests.get(url)

if R.status_code == 200:
    data = json.loads(R.text)
    print("Country "+data["sys"]["country"])
    print("Name of city is "+city_name)
    print("Temperature:", data["main"]["temp"], "°C")
    print("Temperature feels like: ",data["main"]["feels_like"],"°C")
    print("Minimum Temperature ",data["main"]["temp_min"]," °C") 
    print("Maximum Temperature ",data["main"]["temp_max"]," °C")
    print("Weather Description: ",data["weather"][0]["description"])
    print("pressure ",data["main"]["pressure"]," hpa")
    print("Wind Speed ",data["wind"]["speed"],"M/S")


    
 
else:
    print(f"sorry {R.status_code}")