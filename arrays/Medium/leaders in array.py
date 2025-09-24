#Brute force
arr=[10,22,17,11,3,0,6]
ans=[]

for i in range(len(arr)):
    check=False
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            check=True
        else:
            check=False
            break
    if(check):
        ans.append(arr[i])
ans.append(arr[-1])
print(ans)

#Optimal

arr=[10,22,17,11,3,0,6]
ans=[]
n=len(arr)-1
maxi=10**(-18)

for i in range(n,0,-1):
    if(arr[i]>maxi):
        ans.append(arr[i])
    maxi=max(arr[i],maxi)
print(ans)