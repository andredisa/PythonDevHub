from PolygonLib import PolygonLib
import matplotlib.pyplot as plt

from configFinanza import POLYGON_TOKEN

def main():
    mese = ""
    while (not mese.isdigit()) or int(mese) < 1 or int(mese) > 12:
        mese = input("Inserire il mese (1-12): ")
    if(int(mese) < 10):
        mese = "0"+mese

    anno = ""
    while (not anno.isdigit()) or int(anno) < 2000 or int(anno) > 2024:
        anno = input("Inserire l'anno (2000-2024): ")

    stock = None
    while stock == None or stock == "":
        stock = input("Inserire lo stock: ")

    polygon = PolygonLib(POLYGON_TOKEN, stock, mese, anno)
    openPrices, closePrices = polygon.getPrice()

    plt.plot(openPrices.keys(), openPrices.values(), label="Open")
    plt.plot(closePrices.keys(), closePrices.values(), label="Close")
    plt.legend()
    plt.show()

    
if __name__ == "__main__":
    main()