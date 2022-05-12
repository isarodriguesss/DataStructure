array = [i for i in range(1, 11)]

def rotate(array, element):
    new_list = array[element:]+array[:element]
    return new_list

print(rotate(array, 3))