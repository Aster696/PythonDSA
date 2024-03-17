my_array = [9, 4, 5, 6, 10, 3, 7, 2, 8]

def find_lowest_number():
    num = 0
    for index, array in enumerate(my_array):
        if index == 0 or array < num:
            num = array
    print(f'Lowest value is: {num}')

def find_highest_number():
    num = 0
    for index, array in enumerate(my_array):
        if index == 0 or array > num:
            num = array
    print(f'Highest value is: {num}')

find_lowest_number()   
find_highest_number()