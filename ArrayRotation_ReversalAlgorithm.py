array = [i for i in range(1, 8)]

def reverseArray(array, start, end): 
    while (start < end):
        temp = array[start]
        array[start] = array[end]
        array[end] = temp
        start += 1
        end = end-1

def rotate(array, d):
    n = len(array)
    reverseArray(array, 0, d-1)
    reverseArray(array, d, n-1)
    reverseArray(array, 0, n-1)

rotate(array, 2)
print(array)

#Complexity = O(N)