import flightTicket.shared.constants.airline as airline
import flightTicket.shared.constants.season as season

MINOR_AGE = 18
MAJOR_AGE = 60


def getFee(company: str) -> float:
    fee = 0
    if (airline.ALAS == company):
        fee = 0.3
    if (airline.VOLAR == company):
        fee = 0.2
    return fee


def getFeeByPassegerAge(passengerAge: int) -> float:
    fee = 0
    if (passengerAge < MINOR_AGE):
        fee = 0.5
    return fee


def getSafeLifeAmount(company: str, passengerAge: int) -> int:
    amount = 0
    if (company == airline.VOLAR and passengerAge > MAJOR_AGE):
        amount = 100000
    return amount


def getSeasonFee(company: str, currentSeason: str, isStudent: bool) -> float:
    fee = 0
    if (company == airline.ALAS and currentSeason == season.LOW and isStudent):
        fee = 0.1
    return fee


def calculateTotalPricing(basePrice: int, companyFee: float, ageDiscountFee: float, safeAmount: int, seasonFee: float) -> float:
    return round(basePrice+(basePrice*companyFee)-(basePrice*ageDiscountFee)+safeAmount-(seasonFee*basePrice), 2)
