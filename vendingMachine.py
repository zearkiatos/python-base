def exchangeCalculator(change:int)->str:
    fiveHundredCoins = round(change//500)
    change-=500*fiveHundredCoins
    twoHundredCoins = round(change//200)
    change-=200*twoHundredCoins
    oneHundredCoins = round(change//100)
    change-=100*oneHundredCoins
    fiftyCoins = round(change//50)
    change-=50*fiftyCoins
    return str(fiveHundredCoins)+','+str(twoHundredCoins)+','+str(oneHundredCoins)+','+str(fiftyCoins)

print(exchangeCalculator(1500))