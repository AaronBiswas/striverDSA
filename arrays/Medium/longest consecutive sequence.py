#Brute force

arr=[102,4,100,1,101,3,2,1,1]
longest=1


def ls(arr,x):
    if x in arr:
        return True
    return False

for i in range(len(arr)):
    x=arr[i]
    count=1
    while(ls(arr,x+1)):
        x=x+1
        count=count+1
    longest=max(count,longest)
print(longest)

#Better Solution

arr=[102,4,100,1,101,3,2,1,1]
longest=1
curr=0
lastSmaller=10**(-18)
arr.sort()


for i in range(len(arr)):
    if(arr[i]-1 == lastSmaller):
        curr+=1
        lastSmaller=arr[i]
    elif(arr[i]!=lastSmaller):
        curr=1
        lastSmaller=arr[i]
    longest=max(longest,curr)
print(longest)

#Optimal

arr=[102,4,100,1,101,3,2,1,1]
longest=1
curr=0
set_arr=set(arr)
print(set_arr)

def ls(x,set_arr):
    if(x in set_arr):
        return True
    return False

for i in set_arr:
    if (i-1) not in set_arr:
        curr=1
        x=i
        while(ls(x+1,set_arr)):
            curr+=1
            x+=1
        longest=max(longest,curr)
print(longest)
    