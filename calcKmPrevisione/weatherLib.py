import requests
from configKMP import key

class weatherLIb:
    #stampo le condizioni meteo di una location
    def find_meteo_location(self, nomeTappa):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={nomeTappa}&appid={key}&units=metric"
        response = requests.get(url)
        responseJson = response.json()
        #!analizza sempre la risposta json usando il link nel browser!
        print(f"Condizione meteo di {nomeTappa}: {responseJson['weather'][0]['description']}")