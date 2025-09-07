#optimal and brute force

arr=[1,1,0,1,1,1,0,0,1,1]

count=0
maxi=0

for i in range(len(arr)):
    if(arr[i]==1):
        count+=1
    else:
        maxi=max(maxi,count)
        count=0
maxi=max(maxi,count)

print(maxi)