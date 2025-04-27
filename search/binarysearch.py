def BinarySearch(values,target) :
    low = 0
    high = len(values) - 1
    values.sort()
    print(f"Sorted list : {values}")
    while low <= high :
        mid = (low + high) // 2
        if target == values[mid] :
            return True 
        elif target < values[mid] :
            high = mid - 1 
        else :
            low = mid + 1
            return False
        
values = [1,3,6,4,6,5,6,4]
target = 8

oldval = values.copy()

found = BinarySearch(values,target)

if found :
    print(f"{target} was found in the {oldval} list")
else :
    print(f"{target} is not found in the {oldval} list")

