list = ['star', 'rats', 'car', 'arc', 'arts', 'stars']

def verify_len(word, array):
    new_list = [word]
    for i in array:
        if  len(word) == len(i):
            new_list.append(i)
    return new_list

def anagram_check(array):
    anagrams = []
    for i in array:
        array.remove(i)
        anagrams.append(verify_len(i, array))
    return anagrams
        

print(anagram_check(list))

#Complexity = 2*O(N)