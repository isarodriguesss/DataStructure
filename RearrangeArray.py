from operator import length_hint
import re


array = [i for i in range(10)]

def rearrange(array):
    for i in range(len(array)):
        for j in array:
            if i != j:
                result = 1
                break
            else:
                result = 0
    if result == 1:
        print("different")
    else:
        print("not different")

rearrange(array)