#Brute force
arr=[1,2,8,8,8,10,11]

ele=int(input())

first=-1
last=-1

for i in range(len(arr)):
    if(arr[i]==ele):
        if(first==-1):
            first=i
        last=i
print(first,last)  


#Better Solution
arr=[1,2,8,8,8,10,11]

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

def Floor_LB(arr,ele,l,h):
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

ele=int(input())

lb=Ceil_LB(arr,ele,l,h)


if(lb==(h+1) or arr[lb]!=ele):
    print(-1,-1)
else:
    print(lb," ",Floor_LB(arr,ele,l,h)-1)
    
#Optimal Solution

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

print(first_occ(arr,ele,n),last_occ(arr,ele,n))
    