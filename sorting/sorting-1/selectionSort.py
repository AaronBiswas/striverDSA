arr=[1,2,3,4,0]

for i in range(len(arr)):
    mini=i
    for j in range(i,len(arr)):
        if(arr[j]<arr[mini]):
            mini=j
    arr[mini],arr[i]=arr[i],arr[mini]
print(arr)