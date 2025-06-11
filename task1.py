import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

API_KEY = '31014d0af6170b91a00991e746410e76'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

cities = ['Delhi', 'Mumbai', 'Chennai', 'Bengaluru', 'Hyderabad', 'Kolkata', 'Ahmedabad', 'Pune']

weather_data = []

for city in cities:
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        city_data = {
            'City': city,
            'Temperature (°C)': data['main']['temp'],
            'Humidity (%)': data['main']['humidity']
        }
        weather_data.append(city_data)
    else:
        print(f"Failed to fetch data for {city}")

df = pd.DataFrame(weather_data)

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.barplot(x='City', y='Temperature (°C)', hue='City', data=df, palette='coolwarm', legend=False)

plt.title('Current Temperature in Indian Cities')
plt.ylabel('Temperature (°C)')
plt.xlabel('City')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(x='City', y='Humidity (%)', data=df, marker='o', color='green')
plt.title('Current Humidity in Indian Cities')
plt.ylabel('Humidity (%)')
plt.xlabel('City')
plt.tight_layout()
plt.show()
