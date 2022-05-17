array = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]

def rearrange(array):
    array = sorted(array)
    for i in range(len(array)):
        if array[i] != -1 and array[i] != i:
            x = array[i]

            # check if desired place
            # is not vacate
            while array[x] != -1 and array[x] != x:
                # store the value from
                # desired place
                y = array[x]
                # place the x to its correct
                # position
                array[x] = x
                # now y will become x, now
                # search the place for x
                x = y
            # place the x to its correct
            # position
            array[x] = x

            # put -1 at
            # the vacated place
            if array[i] != -1:
                array[i] = -1

    print(array)

rearrange(array)

#Complexity = O(N^2)
