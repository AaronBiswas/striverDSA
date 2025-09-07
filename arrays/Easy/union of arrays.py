#Brute force

# arr1=[1,2,3,4,4]
# arr2=[5,6,7,8,8]

# set1=set(arr1)
# set2=set(arr2)

# arr3=list(set1|set2)

# print(arr3)

#Optimal solution

arr1=[1,2,3,4,4]
arr2=[5,6,7,8,8]
arr3=[]

n=len(arr1)
m=len(arr2)

i,j=[0]*2

while(i<n and j<m):
    if(arr1[i]<=arr2[j]):
        if((len(arr3)==0) or (arr3[-1]!=arr1[i])):
            arr3.append(arr1[i])
        i+=1
    else:
        if((len(arr3)==0) or (arr3[-1]!=arr2[j])):
            arr3.append(arr2[j])
        j+=1
while(i<n):
    if((len(arr3)==0) or (arr3[-1]!=arr1[i])):
        arr3.append(arr1[i])
    i+=1
while(j<m):
    if((len(arr3)==0) or (arr3[-1]!=arr2[j])):
        arr3.append(arr2[j])
    j+=1
    
        
print(arr3)