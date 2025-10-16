#Lower Bound(First True method)
arr=[1,2,3,3,5,8,8,10,10,11]

def BinSearchLB(arr,ele,l,h):
    ans=len(arr)
    while(l<=h):
        mid=(l+h)//2
        if(arr[mid]>=ele):
            ans=mid
            h=mid-1
        else:
            l=mid+1
    return ans
    
l=0
h=len(arr)-1
    
print(BinSearchLB(arr,1,l,h))