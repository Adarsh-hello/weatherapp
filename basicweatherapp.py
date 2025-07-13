import tkinter as tk
from tkinter import messagebox
import requests


API_KEY = "fed34111cabc49c98ce53418250407"

def get_weather():
    city = city_input.get().strip()
    
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    # API URL for WeatherAPI
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"



    try:
        response = requests.get(url)
        data = response.json()

        if "error" in data:
            messagebox.showerror("Error", data["error"]["message"])
            return

        city_name = data["location"]["name"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        wind_kph = data["current"]["wind_kph"]

        result = f"""
Weather in {city_name}, {country}
Condition: {condition}
Temperature: {temp_c}°C
Humidity: {humidity}%
Wind Speed: {wind_kph} km/h
"""
        messagebox.showinfo(f"Weather in {city_name}", result)

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong!\n{e}")

# GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("350x250")
root.config(bg="#2c3e50")

tk.Label(root, text="Weather App", font=("Arial", 20, "bold"), fg="white", bg="#2c3e50").pack(pady=10)

city_input = tk.Entry(root, font=("Arial", 14), justify="center")
city_input.pack(pady=10)

tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather, bg="#3498db", fg="white").pack(pady=10)

root.mainloop()
