#Ceil Method

arr=[1,2,4,7]

def Ceil_LB(arr,ele,l,h):
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

print(Ceil_LB(arr,3,l,h))


#Floor Method

arr=[1,2,4,7]

def Floor_LB(arr,ele,l,h):
    ans=-1
    while(l<=h):
        mid=(l+h)//2
        if(arr[mid]<=ele):
            ans=mid
            l=mid+1         #Here the lower value will be mid+1 because condition is arr[mid]<=ele
        else:
            h=mid-1         #Here the higher value will be mid-1 because condition is arr[mid]<=ele
    return ans
l=0
h=len(arr)-1

print(Floor_LB(arr,3,l,h))