my_array = [9, 4, 5, 6, 10, 3, 7, 2, 8]

def set_value_lowest_to_highest():
    lowest = []
    for i in range(len(my_array) - 1):
        for j in range(len(my_array) - i - 1):
            if(my_array[j] > my_array[j+1]):
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
    print('Lowest to highes: ', my_array)

def set_value_highest_to_lowest():
    lowest = []
    for i in range(len(my_array) - 1):
        for j in range(len(my_array) - i - 1):
            if(my_array[j] < my_array[j+1]):
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
    print('Highest to lowest: ', my_array)

set_value_lowest_to_highest()
set_value_highest_to_lowest()