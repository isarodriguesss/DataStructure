def reverseArray(array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end = end -1
    
A = [1, 2, 3, 4, 5, 6]

reverseArray(A, 0, len(A)-1)

print(A)

#Complexity = O(N)