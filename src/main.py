from pycoingecko import CoinGeckoAPI
import cbpro

class CryptoCoin():
    def __init__(self, sCoinName, bActive, fMaxSell, fMinSell):
        self.__sCoinName = sCoinName
        self.__bActive = bActive
        self.__fMaxSell = fMaxSell
        self.__fMinSell = fMinSell

        print("Coin added")
    
    def __del__(self):
        print("Coin deleted")

    def getCurrentPrice(self):
        price = CoinGeckoAPI().get_price(self.__sCoinName, 'usd')
        res = []

        for key in price.keys():
            res.append(price[key])
        
        return res[0]['usd']

    def isWithinParameters(self):
        fCurrent = self.getCurrentPrice()

        if self.__fMaxSell < fCurrent or self.__fMinSell > fCurrent:
            print(fCurrent)

    def bSell(self, bActivator):
        if bActivator == True:
            print("sell")

class Profile:
    def __init__(self, sName, sWalletAdress, sCardNumber, nCCV, sExpDate, sUserName, sPassword):
        self.__sName = sName
        self.__sWalletAdress = sWalletAdress
        self.__sCardNumber = sCardNumber
        self.__nCCV = nCCV
        self.__sExpDate = sExpDate
        self.__sUserName = sUserName
        self.__sPassword = sPassword

        print("Profile added")

    def __del__(self):
        print("Profile deleted")

def __main__():
    a = CryptoCoin('bitcoin', True, 1700, 1700)
    b = CryptoCoin('ethereum', True, 1, 1)
    print(a.getCurrentPrice(), b.getCurrentPrice())
    pass

if __name__ == '__main__':
    __main__()

