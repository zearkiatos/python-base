def average_list (numbers:list)->float:
    totalNumber = 0
    sumNumbers = 0
    for number in numbers:
        if (number > 0):
            totalNumber+=1
            sumNumbers+=number
    return sumNumbers/totalNumber


numbers = [2,-1,3,90,100,-8,120]
print(average_list(numbers))