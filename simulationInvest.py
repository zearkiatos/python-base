amountForSave = float(input('Type your amount for save: $'))
interestRate = float(input('Type your interest rate: '))
years = int(input('Type the number of year: '))

newAmount = round(amountForSave*pow((1+interestRate/100),years),2)
print('Your initial Amount')
print(amountForSave)

print('The projection in '+str(years)+' years with interest rate '+str(interestRate))

print('The hope amount')
print(newAmount)