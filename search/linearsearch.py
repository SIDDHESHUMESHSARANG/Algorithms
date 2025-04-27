def linearSearch(values,target) :
    for i in range(len(values)) :
        if values[i] == target :
            return i
    return -1

values = [1,3,5,6,4]
target = 6


found = linearSearch(values,target)

if found == -1 :
    print(f"{target} not found in the list {values}")
else :
    print(f"{target} is found at index {found}")