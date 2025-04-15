import requests

class StreetLib:
    #ricerco una località chiedendo il nome all'utente
    def search_location(self, tappa):
        #da street map ricerco la localita
        url = f"https://nominatim.openstreetmap.org/search?q={tappa}&format=json&addressdetails=1"
        #faccio la query
        response = requests.get(url)
        #casistiche del risultato
        #-200 = successo
        #-altrimenti errore
        if response.status_code == 200:
            return True
        else:
            print(f"Errore nella richiesta API: {response.status_code}")
            return False
    #visualizzo i risultati
    def display_results(self, locations):
        #per ogni location
        for location in locations:
            print(f"nome: {location['display_name']}")
            print(f"latitudine: {location['lat']}")
            print(f"longitudine: {location['lon']}")
            print(f"città: {location['address'].get('city', 'N/A')}")
            print(f"via: {location['address'].get('road', 'N/A')}")
            print(f"regione: {location['address'].get('state', 'N/A')}")
            print("-" * 50)

    #ottengo la latitudine della tappa
    def getLat(self, tappa):
        url = f"https://nominatim.openstreetmap.org/search?q={tappa}&format=json&addressdetails=1"
        #faccio la query
        response = requests.get(url)
        #casistiche del risultato
        #-200 = successo
        #-altrimenti errore
        if response.status_code == 200:
            locations = response.json()
            return locations[0]['lat']
        else:
            print(f"Errore nella richiesta API: {response.status_code}")
            return False
        
    #ottengo la longitudine della tappa
    def getLon(self, tappa):
        url = f"https://nominatim.openstreetmap.org/search?q={tappa}&format=json&addressdetails=1"
        #faccio la query
        response = requests.get(url)
        #casistiche del risultato
        #-200 = successo
        #-altrimenti errore
        if response.status_code == 200:
            locations = response.json()
            return locations[0]['lon']
        else:
            print(f"Errore nella richiesta API: {response.status_code}")
            return False