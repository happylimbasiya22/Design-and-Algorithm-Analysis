def binarysearch(arr, l , r , key):
    if l <= r:
        mid = (l+r)//2
        if(arr[mid]==key):
            return mid
        elif(arr[mid]<key):
            return binarysearch(arr,mid+1,r,key)
        else:
            return binarysearch(arr, l, mid-1, key)
    else:
        return-1
    
print(binarysearch([1,3,5,7,9],1,4,5))
        
