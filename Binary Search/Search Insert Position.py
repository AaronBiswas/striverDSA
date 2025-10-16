#Optimal solution
arr=[1,2,4,7]

def SearchPosLB(arr,ele,l,h):
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

print(SearchPosLB(arr,3,l,h))

#This is lower bound implemented in the problem