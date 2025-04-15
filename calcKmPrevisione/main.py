from StreetLib import StreetLib
from OpenRouteLib import OpenRouteLib
from weatherLIb import weatherLIb
#chiedo le tappe del viaggio all'utente
def chiediTappe(streetLib, routeLib, weatherLib):
    continua = True
    tappe = []
    #creo un contatore per controllare se l'utente inserisce almeno 2 località
    countLocal = 0
    while continua == True:
        tappa = input("inserisci una località: ")
        #controllo se esiste la località indicata
        if streetLib.search_location(tappa) == False:
            print('località non esistente!')
        else:
            tappe.append(tappa)
            countLocal+=1
        #chiedo all'utente se vuole continuare
        inputContinua = input("continuare? s/n\n")
        if inputContinua == 'n' and countLocal>=2:
            routeLib.find_distances(streetLib, tappe, weatherLib)
            continua = False
        else:
            print('inserire almeno 2 località!')

def main():
    #crea un'istanza della classe StreetLib
    streetLib = StreetLib()
    routeLib = OpenRouteLib()
    weatherLib = weatherLIb()
    chiediTappe(streetLib, routeLib, weatherLib)

if __name__ == "__main__":
    main()