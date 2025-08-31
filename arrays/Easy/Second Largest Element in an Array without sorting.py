arr=[1,2,3,4,0]

temp=arr[0]
second=-1

for i in range(1,len(arr)):
    if(arr[i]>temp):
        second=temp
        temp=arr[i]
    elif(arr[i]>second and arr[i]<temp):
        second=arr[i]
print(second)