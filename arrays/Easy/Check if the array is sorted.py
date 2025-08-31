arr=[1,2,3,4]

boolean=True

for i in range(1,len(arr)):
    if(arr[i-1]>arr[i]):
        boolean=False
        break
print(boolean)
