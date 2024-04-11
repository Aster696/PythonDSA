my_array = [9, 4, 2, 5, 6, 10, 3, 7, 8]

def add_data():
    print(my_array)
    store_data=0
    for index, array in enumerate(my_array):
        if(index == 4):
            store_data = array
            my_array[index] = 1
            my_array.append(store_data)
    print(my_array)
    
    # for i in range(6, 0, -1):
    #     print(i)

add_data()