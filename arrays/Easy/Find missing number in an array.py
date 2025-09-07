#Brute Force

# arr=[1,1,2,9,5,11,11,2,5]

# n=int(input())

# var=-1

# for i in range(1,n):
#     check=False
#     for j in arr:
#         if(i==j):
#             check=True
#             break
#     if(not(check)):
#         var=i
# print(var)

#Better
# arr=[1,2,3,5,6,7,8,9,10]

# n=int(input())

# var=[0]*(n+1)

# for i in range(len(arr)):
#     var[arr[i]]=1
# for j in range(1,len(arr)):
#     if(var[j]==0):
#         print(j)
#         break

#optimal 1
# add=0
# arr=[1,2,3,5,6,7,8,9,10]

# n=int(input())

# for i in arr:
#     var=(n*(n+1))//2
# print(var-add)

#optimal 2

xor1=0
xor2=0

arr=[1,2,3,5,6,7,8,9,10]

n=int(input())

for i in range(1,n+1):
    xor1^=i
for j in arr:
    xor2^=j
    
print(xor1^xor2)