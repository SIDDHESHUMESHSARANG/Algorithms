def SelectionSort(arr) :
    for i in range(len(arr)-1,0,-1) : 
        maxPos = 0
        for loc in range(1,i + 1) :
            if arr[loc] > arr[maxPos] :
                maxPos = loc
        arr[i],arr[maxPos] = arr[maxPos],arr[i]

arr = [2,3,5,3,6,3]
print(arr)
SelectionSort(arr)

print(arr)


    