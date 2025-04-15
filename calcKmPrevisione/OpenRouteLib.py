import requests
from StreetLib import StreetLib
from weatherLIb import weatherLIb

from configKMP import token_api
class OpenRouteLib:
    #trovo tutte le distanze
    def find_distances(self, streetLib, tappeArray, weatherLib):
        distanzaTotale = 0
        tempoTotale = 0
        #trovo il meteo di ogni località
        print("-------------------------------------------------------\nMETEO:")
        for i in range(len(tappeArray)):
            weatherLib.find_meteo_location(tappeArray[i])
        print("-------------------------------------------------------\nDISTANZE:")
        #ottengo la distanza tra una tappa e la successiva
        for i in range(len(tappeArray)-1): 
            #ottengo latitudine e longitudine della prima tappa
            lat1 = streetLib.getLat(tappeArray[i])
            lon1 = streetLib.getLon(tappeArray[i])
            #ottengo lat e lon della tappa successiva
            lat2 = streetLib.getLat(tappeArray[i+1])
            lon2 = streetLib.getLon(tappeArray[i+1])
            #trovo la distanza tra le due tappe
            risCSV = self.find_distance(tappeArray[i], tappeArray[i+1], lat1, lon1, lat2, lon2)
            ris = risCSV.split(';')
            distanzaTotale += float(ris[0])
            tempoTotale += float(ris[1])
            i = i+1
        #stampo i risultati finali, con distanza e tempo di percorrenza totali
        print("-------------------------------------------------------\nTOTALI:")
        print(f"distanza totale = {distanzaTotale} km")
        print(f"tempo di percorrenza totale = {tempoTotale} minuti")

    #ottengo la distanza tra due tappe
    def find_distance(self, nomeTappa1, nomeTappa2, lat1, lon1, lat2, lon2):
        #dal sito di open route prendo il comando
        #metto la mia key e le latitudini e longitudini ottenute tramite streetmap
        url = f"https://api.openrouteservice.org/v2/directions/driving-car?api_key={token_api}&start={lon1},{lat1}&end={lon2},{lat2}"
        #faccio la query
        response = requests.get(url)
        #ottengo la risposta in json
        responseJson = response.json()
        #ottengo la distanza in metri dal json ottenuto
        distanza_metri = (responseJson['features'][0]['properties']['summary']['distance'])/1000
        tempo_percorrenza = (responseJson['features'][0]['properties']['summary']['duration'])/60
        print(f"distanza tra {nomeTappa1} e {nomeTappa2} = {distanza_metri} km, tempo di percorrenza: {tempo_percorrenza} minuti")
        return str(distanza_metri) + ";" + str(tempo_percorrenza)
        