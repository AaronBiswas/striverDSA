#Brute Force

arr=[1,2,3,-3,1,1,1,4,2,-3]
k=int(input())

count=0

for i in range(len(arr)):
    add=0
    for j in range(i,len(arr)):
        add+=arr[j]
        if(add==k):
            count+=1
print(count)