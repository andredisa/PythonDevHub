import requests
from configNews import key_api

class newsApi:
    def __init__(self):
        self.key_api

    #prendo il titolo delle news principali in un certo paese
    def getHeadlines(self, country):
        #url base della richiesta
        base_url = "https://newsapi.org/v2/top-headlines"
        #effettua la richiesta GET utilizzando requests
        params = {
            "country": country,
            "apiKey": self.key_api
        }
        #specifico l'url di base e i parametri che passerei normalmente nell'url
        response = requests.get(base_url, params=params)
        responseJson = response.json()
        #prendo tutti gli articoli
        articoli = responseJson["articles"]
        #scorro articolo per articolo
        for articolo in articoli:
            print("\n" + articolo['title'] + " data di pubblicazione: " + articolo["publishedAt"] + "\n")
    
    #prendo il titolo delle news principali, in una certa lingua
    def getHeadlinesLenguage(self, lenguage):
        #url base della richiesta
        base_url = "https://newsapi.org/v2/top-headlines"
        #effettua la richiesta GET utilizzando requests
        params = {
            "language": lenguage,
            "apiKey": self.key_api
        }
        #specifico l'url di base e i parametri che passerei normalmente nell'url
        response = requests.get(base_url, params=params)
        responseJson = response.json()
        #prendo tutti gli articoli
        articoli = responseJson["articles"]
        #scorro articolo per articolo
        for articolo in articoli:
            print("\n" + articolo['title'] + " data di pubblicazione: " + articolo["publishedAt"] + "\n")

    #prendo gli articoli in base all'argomento
    def getByArgument(self, argument):
        #url base della richiesta
        base_url = "https://newsapi.org/v2/everything"
        #effettua la richiesta GET utilizzando requests
        params = {
            "q": argument,
            "apiKey": self.key_api
        }
        #specifico l'url di base e i parametri che passerei normalmente nell'url
        response = requests.get(base_url, params=params)
        responseJson = response.json()
        articoli = responseJson["articles"]
        for articolo in articoli:
            print("\n" + articolo['title'] + " data di pubblicazione: " + articolo["publishedAt"] + "\n")

    #prendo gli articoli in base all'argomento in una certa data
    def getByDate(self, argument, dateStart, dateEnd):
        #url base della richiesta
        base_url = "https://newsapi.org/v2/everything"
        #effettua la richiesta GET utilizzando requests
        params = {
            "q": argument,
            "from": dateStart,
            "to": dateEnd,
            "apiKey": self.key_api
        }
        #specifico l'url di base e i parametri che passerei normalmente nell'url
        response = requests.get(base_url, params=params)
        responseJson = response.json()
        articoli = responseJson["articles"]
        for articolo in articoli:
            print("\n" + articolo['title'] + " data di pubblicazione: " + articolo["publishedAt"] + "\n")

    #prendo l'articolo/i più popolare, in una certa lingua
    def getMostPopularLenguage(self, lenguage, selezione):
        #selezione:
            #0 = tutti
            #1 = solo il più popolare
        #url base della richiesta
        base_url = "https://newsapi.org/v2/top-headlines"
        #effettua la richiesta GET utilizzando requests
        params = {
            "SortBy": "popularity",
            "language": lenguage,
            "apiKey": self.key_api
        }
        #specifico l'url di base e i parametri che passerei normalmente nell'url
        response = requests.get(base_url, params=params)
        responseJson = response.json()
        articoli = responseJson["articles"]
        if(selezione == 0):
            for articolo in articoli:
                print("\n" + articolo['title'] + " data di pubblicazione: " + articolo["publishedAt"] + "\n")
        else:
            print("\n" + articoli[0]['title'] + " data di pubblicazione: " + articoli[0]["publishedAt"] + "\n")
    
    #prendo gli articoli pubblicati da un certo editore su un certo argomento
    def getByArgumentDomain(self, argument, domain):
        #url base della richiesta
        base_url = "https://newsapi.org/v2/everything"
        #effettua la richiesta GET utilizzando requests
        params = {
            "q": argument,
            "apiKey": self.key_api,
            "domain": domain
        }
        #specifico l'url di base e i parametri che passerei normalmente nell'url
        response = requests.get(base_url, params=params)
        responseJson = response.json()
        articoli = responseJson["articles"]
        for articolo in articoli:
            print("\n" + articolo['title'] + " data di pubblicazione: " + articolo["publishedAt"] + "\n")
            print(articolo['url'])
            
    #prendo il primo articolo (il più popolare) per intero in base al titolo
    def getByArgumentComplete(self, argument, lenguage):
        #url base della richiesta
        base_url = "https://newsapi.org/v2/everything"
        #effettua la richiesta GET utilizzando requests
        params = {
            "SortBy": "popularity",
            "language": lenguage,
            "q": argument,
            "apiKey": self.key_api
        }
        #specifico l'url di base e i parametri che passerei normalmente nell'url
        response = requests.get(base_url, params=params)
        responseJson = response.json()
        articoli = responseJson["articles"]
        articolo = articoli[0]
        print("\n" + articolo['title'] + " data di pubblicazione: " + articolo["publishedAt"] + "\n")
        print("contenuto:" + articolo['content'])
        print(articolo['url'])

    