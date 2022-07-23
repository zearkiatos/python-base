import utils.convertMoney as convertMoney

def executeConvertDollars(trm:float)->None:
    pesos = float(input('Type the amount in pesos: '))
    dollars = convertMoney.convertToDollars(pesos, trm)
    print(pesos, 'pesos is', round(dollars, 2), ' dollars')

def executeConvertPesos(trm:float)->None:
    dollars = float(input('Type the amount in dollars: '))
    pesos = convertMoney.convertToPesos(dollars, trm)
    print(dollars, 'dollars is', round(pesos, 0), ' pesos')

def initialization()->None:
    trm = float(input('Type the TRM: '))
    executeConvertDollars(trm)
    executeConvertPesos(trm)

initialization()