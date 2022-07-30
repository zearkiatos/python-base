import flightTicket.logic.ticketPricing as ticketPricing
import flightTicket.shared.constants.basePricing as basePricing


def calculator() -> None:

    company = input(
        print('Choose a company: \n ✈️ ALAS \n ✈️ VOLAR\n ')).upper()
    fee = ticketPricing.getFee(company)
    age = int(input("Type passenger age: "))
    isStudent = input("Is the passenger a student? \n y/n ").lower()
    season = input(
        print('Choose the current season: \n 📈 HIGH \n 📉 LOW\n ')).upper()
    student = isStudent == "y"
    ageFee = ticketPricing.getFeeByPassegerAge(age)
    safeLifeAmount = ticketPricing.getSafeLifeAmount(company, age)
    seasonFee = ticketPricing.getSeasonFee(company, season, student)
    price = ticketPricing.calculateTotalPricing(
        basePricing.BOGOTA_TOKIO, fee, ageFee, safeLifeAmount, seasonFee)
    print('The flight from Bogota to Tokio is ', price)


def initialization() -> None:
    calculator()


initialization()
