from dotenv import dotenv_values
import pandas as pd
import requests

variables = dotenv_values(".env")

API_KEY = variables["API_KEY"]
LAT = "-23.5505"  # Latitude (exemplo: São Paulo)
LON = "-46.6333"  # Longitude (exemplo: São Paulo)
URL = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={LAT}&lon={LON}&appid={API_KEY}"

response = requests.get(URL)
data = response.json()
print(data)
air_quality = data["list"][0]["components"]
df = pd.DataFrame(air_quality, index=[0])

# Exibir os dados
print("\nDados brutos:")
print(df)

df.to_csv("../data/qualidade_ar.csv", index=False)
print("\nDados salvos em ../data/qualidade_ar.csv")
