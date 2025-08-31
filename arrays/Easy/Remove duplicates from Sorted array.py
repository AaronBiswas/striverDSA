arr=[1,1,2,2,3,3,4,4]


#Brute Force

# sett=set(arr)

# i=0

# for a in sett:
#     arr[i]=a
#     i+=1
# print(arr[0:i])


#Optimal Solution

def remove(arr):
    i=0
    for j in range(1,len(arr)):
        if(arr[i]!=arr[j]):
            i+=1
            arr[i]=arr[j]
    return i+1

n=remove(arr)

for i in range(n):
    print(arr[i])