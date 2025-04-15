# 🌍 Route Planner with Weather and Distance Information

A Python command-line project that allows users to plan a trip by entering a sequence of locations. The program uses **OpenStreetMap**, **OpenRouteService**, and **OpenWeatherMap** APIs to retrieve and display:

- 🧭 Route distances and travel times  
- 🌤️ Real-time weather conditions for each stop  

This is ideal for learning about API integration, JSON parsing, and user interaction via terminal.

---

## ✨ Features

- 📌 Add multiple waypoints for your trip
- ✅ Location validation using OpenStreetMap
- 🚗 Calculates distance and duration between consecutive stops using OpenRouteService
- 🌦️ Displays current weather at each location using OpenWeatherMap
- 🔁 Ensures at least two locations are provided to build a route

---

## 🧰 Technologies & APIs Used

- [OpenStreetMap (Nominatim)](https://nominatim.openstreetmap.org/)
- [OpenRouteService](https://openrouteservice.org/)
- [OpenWeatherMap](https://openweathermap.org/)
- Python standard libraries + `requests`

---

## 🛠️ Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/)

Install the required package:

```bash
pip install requests

🔐 API Key Setup
You will need:

An OpenRouteService API key

An OpenWeatherMap API key

Replace the placeholder keys in the following files:

OpenRouteLib.py → token_api = "your_openrouteservice_api_key"

weatherLib.py → key = "your_openweathermap_api_key"

⚠️ Do not share or upload these keys to public repositories.

🚀 How to Use
Run the main script:

bash
Copia
Modifica
python main.py
You will be prompted to:

Enter a location name

The script checks if the location is valid via OpenStreetMap

Repeat until at least two valid locations are entered

The program then:

Shows the weather for each location

Calculates the distance and travel time between each leg of the trip

Prints total travel distance and estimated time

📌 Example Output
yaml
Copia
Modifica
inserisci una località: Milan
continuare? s/n
s
inserisci una località: Rome
continuare? s/n
n

-------------------------------------------------------
METEO:
Condizione meteo di Milan: scattered clouds
Condizione meteo di Rome: clear sky

-------------------------------------------------------
DISTANZE:
distanza tra Milan e Rome = 571.2 km, tempo di percorrenza: 352.4 minuti

-------------------------------------------------------
TOTALI:
distanza totale = 571.2 km
tempo di percorrenza totale = 352.4 minuti
💡 Possible Enhancements
🗺️ Display the route visually on a map

💾 Save trip data to a file

🧭 Add walking or cycling mode

🌐 Add a GUI using Flask or Tkinter

📉 Include weather forecasts and alerts

📚 Educational Objectives
This project is great for practicing:

REST API integration

JSON response parsing

Modular Python structure with multiple classes

Handling real-world data from multiple APIs

CLI interaction and input validation

⚠️ Disclaimer
This is an educational project. The data may not be fully up-to-date or suitable for critical decisions like real-time navigation or travel planning.

👨‍💻 Happy coding and enjoy building your own trip planner!