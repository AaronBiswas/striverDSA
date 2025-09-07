#Brute Force and Optimal Solution

arr1=[1,2,3,4,4,7]
arr2=[5,6,7,8,8]
arr3=[]

i,j=0,0

n=len(arr1)
m=len(arr2)

while(i<n and j<m):
    if(arr1[i]<arr2[j]):
        i+=1
    elif(arr2[j]<arr1[i]):
        j+=1
    else:
        arr3.append(arr1[i])
        i+=1
        j+=1
print(arr3)