from pycoingecko import CoinGeckoAPI
import cbpro

class CryptoCoin():
    def __init__(self, sCoinName, bActive, fMaxSell, fMinSell, sWalletAdress, sCurrency):
        self.__sCoinName = sCoinName
        self.__bActive = bActive
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

    def IsWithinParameters(self):
        fCurrent = self.GetCurrentPrice()

        if self.__fMaxSell < fCurrent or self.__fMinSell > fCurrent:
            print(fCurrent)

    def bSell(self, bActivator):
        if bActivator == True:
            print("sell")

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
        aDetails = [self.__sCardNumber, self.__nCCV, self.__sExpDate]
        return aDetails
    
    def GetLoginDetails(self):
        aDetails = [self.__sUserName, self.__sPassword]
        return aDetails

    def SetName(self, sName):
        self.__sName = sName
    
    def SetCardDetails(self, sCardNumber, nCCV, sExpDate):
        self.__sCardNumber = sCardNumber
        self.__nCCV = nCCV
        self.__sExpDate = sExpDate

    def AddCoin(self, sCoinName, fMaxSell, fMinSell, sWalletAdress, sCurrency):
        self.aCoinList.append(CryptoCoin(sCoinName, True, fMaxSell, fMinSell, sWalletAdress, sCurrency))

    def __del__(self):
        print("Profile deleted")

def __main__():
    Victor = Profile("Victor", "xx", 567, "02/22", "vl", "lkadsjfla")
    Victor.AddCoin('ethereum', 1700, 1700, "xx", 'usd')
    pass

if __name__ == '__main__':
    __main__()

