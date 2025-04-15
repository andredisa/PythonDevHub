from news import newsApi

def main():
    #crea un'istanza della classe StreetLib
    newsLibreria = newsApi()
    newsLibreria.getByArgumentDomain("crypto", "thenextweb.com")

if __name__ == "__main__":
    main()