def insertionSort(arr) :
    for i in range(1,len(arr)) :
        currVal = arr[i]
        pos = i
        while pos > 0 and arr[pos - 1] > currVal :
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = currVal

arr = [2,3,4,3,3,5]

print(arr)

insertionSort(arr)

print(arr)

