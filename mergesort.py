def mergesort(arr):
    if(len(arr)<=1):
        return arr
    mid=int(len(arr)//2)
    arr1= arr[:mid]
    arr2 = arr[mid:]
    arr1=mergesort(arr1)
    arr2= mergesort(arr2)   
    return (merge(arr1,arr2)) 
    
def merge(arr1, arr2):
    result = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i+=1
            
        else:
            result.append(arr2[j])
            j += 1


    while i < len(arr1):
        result.append(arr1[i])
        i += 1


    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result



print(mergesort([1,9,5,3,4]))
