def TotalCost(arr) :
    cost = 0
    while len(arr) >= 2 :   
        arr.sort()
        total_sum = arr[0] + arr[1]
        cost += total_sum
        arr = arr[2:]      #slicing the first two elements of arr
        arr.append(total_sum)
    return cost 

arr = [4,5,3,6,8]
result = TotalCost(arr)
print(f"Total cost : {result}")