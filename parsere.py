import urllib.request
import re
webUrl  = urllib.request.urlopen('http://www.vokrugsveta.ru/encyclopedia/index.php?title=%D0%9A%D1%83%D1%80%D1%81%D1%8B_%D0%B2%D1%81%D0%B5%D1%85_%D0%B2%D0%B0%D0%BB%D1%8E%D1%82_%D0%BC%D0%B8%D1%80%D0%B0')
webUrlCrypto = urllib.request.urlopen('https://www.vbr.ru/crypto/')
cryptootvet = str(webUrlCrypto.read())
otvet = str(webUrl.read())
cryptoind = cryptootvet.find('price-rub')
ind = otvet.find('>643')
cryptofindstr = cryptootvet[cryptoind:]
findstr = otvet[ind:]
USDind = findstr.find('= ')
USD = findstr[USDind+2:USDind+9]
findstr = findstr[USDind+3:]
EURind = findstr.find('= ')
EUR = findstr[EURind+2:EURind+9]
findstr = findstr[EURind+3:]
GBPind = findstr.find('= ')
GBP = findstr[GBPind+2:GBPind+10]
findstr = findstr[GBPind+3:]
CHFind = findstr.find('= ')
CHF = findstr[CHFind+2:CHFind+9]
findstr = findstr[CHFind+3:]
CADind = findstr.find('= ')
CAD = findstr[CADind+2:CADind+9]
findstr = findstr[CADind+3:]
AUDind = findstr.find('= ')
AUD = findstr[AUDind+2:AUDind+9]
findstr = findstr[AUDind+3:]
TRYind = findstr.find('= ')
TRY = findstr[TRYind+2:TRYind+9]
findstr = findstr[TRYind+3:]
SGDind = findstr.find('= ')
SGD = findstr[SGDind+2:SGDind+9]
findstr = findstr[SGDind+3:]
UAHind = findstr.find('= ')
UAH = findstr[UAHind+2:UAHind+9]
findstr = findstr[UAHind+3:]
DKKind = findstr.find('= ')
DKK = findstr[DKKind+2:DKKind+9]
findstr = findstr[DKKind+3:]
NOKind = findstr.find('= ')
NOK = findstr[NOKind+2:NOKind+9]
findstr = findstr[NOKind+3:]
SEKind = findstr.find('= ')
SEK = findstr[SEKind+2:SEKind+9]
findstr = findstr[SEKind+3:]
CNYind = findstr.find('= ')
CNY = findstr[CNYind+2:CNYind+9]
print(CNY)
BTC = re.search('\d+\s\d+\,\d', cryptofindstr)
cryptoind = cryptofindstr.find(BTC.group(0))
cryptofindstr = cryptofindstr[cryptoind:]
cryptoind = cryptofindstr.find('price-rub')
ETH = re.search('\d+\D\d+\,\d', cryptofindstr[cryptoind:])
cryptoind = cryptofindstr.find(ETH.group(0))
cryptofindstr = cryptofindstr[cryptoind:]
cryptoind = cryptofindstr.find('price-rub')
LTC = re.search('\d+\D\d+\,\d', cryptofindstr[cryptoind:])