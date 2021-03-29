from pycoingecko import CoinGeckoAPI
import cbpro

class CryptoCoin:
    sCoinName = "DEFAULT"
    sWalletAdress = "DEFAULT"
    bActive = False
    fMinSell = 0
    fMaxSell = 0

    def __init__(self, sCoinName, sWalletAdress, bActive, fMaxSell, fMinSell):
        self.sCoinName = sCoinName
        self.sWalletAdress = sWalletAdress
        self.bActive = bActive
        self.fMaxSell = fMaxSell
        self.fMinSell = fMinSell

        print("Coin added")
    
    def __del__():
        print("Coin deleted")

    def isWithinParameters(self, fCurrent):
        if self.fMaxSell < fCurrent or self.fMinSell > fCurrent:
            print("aaa")

    def bSell(self, bActivator):
        if bActivator == True:
            print("sell")

class Profile:
    def __init__(self, sName, sCardNumber, nCCV, sExpDate, sUserName, sPassword):
        self.sName = sName
        self.sCardNumber = sCardNumber
        self.nCCV = nCCV
        self.sExpDate = sExpDate
        self.sUserName = sUserName
        self.sPassword = sPassword

        print("Profile added")

    def __del__():
        print("Profile deleted")

def __main__():
    a = CryptoCoin("bitcoin", "mihai", True, 8.5, -5)
    a.isWithinParameters(9)
    a.bSell(True)

__main__()

