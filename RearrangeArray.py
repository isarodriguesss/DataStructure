array = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]

def rearrange(array):
    array = sorted(array)
    for i in range(len(array)):
        for j in range(len(array)):
            if i == array[j]:
                controle = 1
                array[i] = array[j]
                break
            else:
                controle = 0
        if controle != 1:
            array[i] = -1
    print(array)

rearrange(array)

