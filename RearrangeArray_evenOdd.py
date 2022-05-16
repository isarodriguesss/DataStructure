def evenOdd(array):
    array = sorted(array)
    n = int(len(array)/2)
    even = [i for i in array[:n+1]]
    odd = [i for i in array[n+1:]]
    b = [0 for i in range(len(array))]
    
    contador = n
    
    for i in range(0, len(b), 2):
        b[i] = even[contador]
        contador = contador - 1
    
    contador = 0
    
    for i in range(1, len(b), 2):
        b[i] = odd[contador]
        contador = contador + 1

    print(b)

a = [1, 2, 3, 4, 5, 6, 7]  
evenOdd(a)