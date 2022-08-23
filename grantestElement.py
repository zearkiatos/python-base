def search_grantest (numbers:list)->int:
    if not len(numbers):
        gratest_number = -1
    else:
        gratest_number = numbers[0]
        for number in numbers:
            if (number>gratest_number):
                gratest_number = number
    return gratest_number

number_list = [1,7,-1,90,10]
print(search_grantest(number_list))
number_list = []
print(search_grantest(number_list))