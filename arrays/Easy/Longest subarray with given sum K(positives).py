from collections import defaultdict

#Brute Force

# count=0
# maxi=10**(-18)

#s=int(input())

# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         count+=arr[j]
#         if(s==count):
#             maxi=max((j-i)+1,maxi)
#         elif(count>s):                #The array contains only +ve elements so this condition is implemented
#             break

#Better Solution (also works for negative integers and is the optimal case for it)
       
# hashed = defaultdict(int)
# maxi=0
# add=0

# arr = [2,0,0,3]

# k = int(input())

# for i in range(len(arr)):
#     add+=arr[i]
#     if(add==k):
#         maxi=max(maxi,i+1)
  
#     rem=add-k 
#     if(rem in hashed.keys()):
#         maxi=max(maxi,i-hashed[rem])
#     if(add not in hashed.keys()):
#         hashed[add]=i

    
# print(maxi)


#Optimal Solution(Only for all positive integers)

arr=[2,0,0,3]

k=int(input())

count=arr[0]
maxi=0

i=0
j=0

while( j<len(arr)):
    while(i<=j and count>k ):
        count-=arr[i]
        i+=1
    if(count==k):
        maxi=max(maxi,j-i+1)
    j+=1
    if(j<len(arr)):
        count+=arr[j]
        
        
print(maxi)