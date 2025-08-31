def merge(arr,l,mid,h):
    left=l
    right=mid+1
    temp=[]
    while(left<=mid and right<=h):
        if(arr[left]<arr[right]):
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while(left<=mid):
        temp.append(arr[left])
        left+=1
    while(right<=h):
        temp.append(arr[right])
        right+=1
    for i in range(l,h+1):
        arr[i]=temp[i-l]


def mergesort(arr,l,h):
    if(l>=h):
        return
    mid=(l+h)//2
    mergesort(arr,l,mid)
    mergesort(arr,mid+1,h)
    merge(arr,l,mid,h)
    
arr=[2,45,65,3465,3,654,87,5,442343,4687,86,98,654,76]
n=len(arr)

mergesort(arr,0,n-1)
        
print(arr)