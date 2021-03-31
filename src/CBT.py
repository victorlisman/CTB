from pycoingecko import CoinGeckoAPI
import cbpro

class CryptoCoin():
    def __init__(self, sCoinName, fMaxSell, fMinSell, sWalletAdress, sCurrency):
        self.__sCoinName = sCoinName
        self.__fMaxSell = fMaxSell
        self.__fMinSell = fMinSell
        self.__sWalletAdress = sWalletAdress
        self.__sCurrency = sCurrency

        print("Coin added")
    
    def __del__(self):
        print("Coin deleted")

    def GetCoinName(self):
        return self.__sCoinName

    def GetCurrentPrice(self):
        price = CoinGeckoAPI().get_price(self.__sCoinName, self.__sCurrency)
        res = []

        for key in price.keys():
            res.append(price[key])
        
        return res[0][self.__sCurrency]

    def bSell(self, bActivator):
        if bActivator == True:
            print("sell")

    def IsOutOfParameters(self):
        fCurrent = self.GetCurrentPrice()

        if self.__fMaxSell < fCurrent or self.__fMinSell > fCurrent:
            self.bSell(True)


class Profile:
    def __init__(self, sName, sCardNumber, nCCV, sExpDate, sUserName, sPassword):
        self.__sName = sName
        self.__sCardNumber = sCardNumber
        self.__nCCV = nCCV
        self.__sExpDate = sExpDate
        self.__sUserName = sUserName
        self.__sPassword = sPassword
        self.aCoinList = []

        print("Profile added")

    def GetName(self):
        return self.__Name
    
    def GetCardDetails(self):
        return [self.__sCardNumber, self.__nCCV, self.__sExpDate]
    
    def GetLoginDetails(self):
        return [self.__sUserName, self.__sPassword]

    def SetName(self, sName):
        self.__sName = sName
    
    def SetCardDetails(self, sCardNumber, nCCV, sExpDate):
        self.__sCardNumber = sCardNumber
        self.__nCCV = nCCV
        self.__sExpDate = sExpDate

    def SetLoginDetails(self, sUserName, sPassword):
        self.__sUserName = sUserName
        self.__sPassword = sPassword

    def AddCoin(self, sCoinName, fMaxSell, fMinSell, sWalletAdress, sCurrency):
        self.aCoinList.append(CryptoCoin(sCoinName, fMaxSell, fMinSell, sWalletAdress, sCurrency))

    def __del__(self):
        print("Profile deleted")

def __main__():
    pass

if __name__ == '__main__':
    __main__()

