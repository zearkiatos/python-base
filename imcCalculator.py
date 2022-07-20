def poundToKilogramers(pound:float)->float:
    return pound*0.45
def inchToMeters(inch:float)->float:
    return inch*0.025
def imcCalculator(pounds: float, inch: float)->float:
    kilogramers = poundToKilogramers(pounds)
    meters = inchToMeters(inch)
    return round(kilogramers/(meters**2),2)

print(imcCalculator(30,10))