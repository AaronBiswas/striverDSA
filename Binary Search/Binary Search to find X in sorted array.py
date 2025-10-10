#Brute Force(Iterative method)

def binary_search(arr,n,target):
    low=0
    high=n-1
    
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==target):
            return True
        elif(arr[mid]<target):
            low=mid+1
        else:
            high=mid-1
    return False



arr=[3,4,6,7,9,13,14,19]

target=7

result=binary_search(arr,len(arr),target)

print(result)

#Recursion Method

arr=[1,2,3,4,7,8,9,12,13]

def BinSearch(arr,ele,l,h):
    mid=(l+h)//2
    if(l<=h):
        if(arr[mid]==ele):
            return True
        elif(ele>arr[mid]):
            return BinSearch(arr,ele,mid+1,h)
        else:
            return BinSearch(arr,ele,l,mid-1)
    return False


l=0
h=len(arr)-1

ele=int(input())

print(BinSearch(arr,ele,l,h))