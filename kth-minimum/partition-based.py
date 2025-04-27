def partition(arr,start,end) :
    pivot = arr[end]
    i = start - 1
    for j in range(start,end) :
        if arr[j] <= pivot :
            i = i + 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[end] = arr[end],arr[i+1]
    return i+1

def kthsmallest(arr,start,end,k) :
    if start == end :
        return arr[start]
    if start < end :
        q = partition(arr,start,end)
        count = q-start+1
        if count == k :
            return arr[q]
        elif count < k :
            return kthsmallest(arr,start,q-1,k)
        else :
            return kthsmallest(arr,q+1,end,k-count)
            