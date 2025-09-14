#brute force
1. generate all permuation
2. do linear search on all the generation permuation array and find the given array in the permutation 
and then take the next element array .
3. if the given array is the last index in the permuation array print the 0th index array as answer



#optimal
arr=[2,1,5,4,3,0,0]
ind=-1
n=len(arr)

for i in range(n-2,0,-1):
    if(arr[i]<arr[i+1]):
        ind=i
        break


if(ind==-1):
    print(arr[::-1])

for i in range(n-1,ind,-1):
    if(arr[i]>arr[ind]):
        arr[i],arr[ind]=arr[ind],arr[i]
        break

arr[ind+1:]=arr[ind+1:][::-1]
print(arr)
