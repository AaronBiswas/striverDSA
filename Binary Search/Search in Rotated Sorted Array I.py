#Brute Solution
arr=[7,8,9,1,2,3,4,5,6]

ans=-1
x=int(input())

for i in range(len(arr)):
    if(arr[i]==x):
        ans=i
print(ans)
        

#Optimal Solution
arr=[7,8,9,1,2,3,4,5,6]

def Rotated_BinSearch(arr,x,n):
    l=0
    h=n-1
    while(l<=h):
        mid=(l+h)//2
        if(arr[mid]==x):
            return mid
        if(arr[l]<=arr[mid]):
            if(arr[l]<=x and x<=arr[mid]):
                h=mid-1
            else:
                l=mid+1
        else:
            if(arr[mid]<=x and x<=arr[h]):
                l=mid+1
            else:
                h=mid-1
    return -1

x=int(input())

print(Rotated_BinSearch(arr,x,len(arr)))