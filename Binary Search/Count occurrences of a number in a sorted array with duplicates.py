arr=[1,2,8,8,8,10,11]

def first_occ(arr,ele,n):
    l=0
    h=n-1
    first=-1
    while(l<=h):
        mid=(l+h)//2
        if(arr[mid]==ele):
            first=mid
            h=mid-1
        elif(arr[mid]>ele):
            h=mid-1
        else:
            l=mid+1
    return first
    
def last_occ(arr,ele,n):
    l=0
    h=n-1
    last=-1
    while(l<=h):
        mid=(l+h)//2
        if(arr[mid]==ele):
            last=mid
            l=mid+1
        elif(arr[mid]>ele):
            h=mid-1
        else:
            l=mid+1
    return last

ele=int(input())
n=len(arr)


print((last_occ(arr,ele,n)-first_occ(arr,ele,n))+1) #Counting the occurence by (last occurence - first occurence + 1)
    