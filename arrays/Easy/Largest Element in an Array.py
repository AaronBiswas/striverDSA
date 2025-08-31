arr=[1,2,3,4,0]

temp=arr[0]

for i in range(1,len(arr)):
    if(temp<arr[i]):
        temp=arr[i]
print(temp)