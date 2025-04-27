def bubbleSort(arr) :
    for p in range(len(arr)-1,0,-1) :
        for i in range(p) :
            if arr[i] > arr[i+1] :
                arr[i],arr[i+1] = arr[i+1], arr[i]

arr=[1,3,2,5,4,6]
bubbleSort(arr)
print(f"Sorted array : {arr}")
