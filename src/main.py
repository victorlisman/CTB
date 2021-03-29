from pycoingecko import CoinGeckoAPI
import cbpro

class CryptoCoin(CoinGeckoAPI):
    def __init__(self, sCoinName, sWalletAdress, bActive, fMaxSell, fMinSell):
        self.sCoinName = sCoinName
        self.sWalletAdress = sWalletAdress
        self.bActive = bActive
        self.fMaxSell = fMaxSell
        self.fMinSell = fMinSell

        print("Coin added")
    
    def __del__(self):
        print("Coin deleted")

    def getCurrentPrice(self):
        price = CoinGeckoAPI().get_price('ethereum', 'usd')
        res = []

        for key in price.keys():
            res.append(price[key])
        
        return res[0]['usd']

    def isWithinParameters(self):
        fCurrent = self.getCurrentPrice()

        if self.fMaxSell < fCurrent or self.fMinSell > fCurrent:
            print(fCurrent)

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

    def __del__(self):
        print("Profile deleted")

def __main__():
    pyegay = CryptoCoin('ethereum', 'mata', True, 1750, 1700)
    pyegay.isWithinParameters()
    pass


if __name__ == '__main__':
    __main__()

