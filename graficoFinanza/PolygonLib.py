import requests

class PolygonLib:
    #costruttore
    def __init__(self, key, stock, month, year) -> None:
        self.apiKey = key
        self.stock = stock
        self.month = month
        self.year = year
        self.openPrices = {}
        self.closePrices = {}
        self.req = requests.Session()

    def getPrice(self):
        last = 0

        if self.month == "02":
            last = 28
        elif self.month in ["04", "06", "09", "11"]:
            last = 30
        else:
            last = 31

        url = f"https://api.polygon.io/v2/aggs/ticker/{self.stock}/range/1/day/{self.year}-{self.month}-01/{self.year}-{self.month}-{last}?adjusted=true&sort=asc&limit=120&apiKey={self.apiKey}"
        r = self.req.get(url)
        response_json = r.json()

        for day in response_json["results"]:
            self.openPrices[day["t"]] = day["o"]
            self.closePrices[day["t"]] = day["c"]

        return self.openPrices, self.closePrices
        
        