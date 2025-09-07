#Brute Force

# arr=[2,6,5,8,11]

# target=int(input())
# flag=0

# for i in range(len(arr)):
#     if(flag):
#         break
#     for j in range(len(arr)):
#         if(i==j):
#             continue
#         if(arr[i]+arr[j]==target):
#             flag=1
#             print("This is the index for target sum",[i,j])
#             break
# print(flag)


#Better Solution

# arr=[2,6,5,8,11]

# mapper={}

# target=int(input())
# flag=0

# for i in range(len(arr)):
#     if((target-arr[i]) in mapper.keys()):
#         flag=1
#         print("indexes",i,mapper[target-arr[i]])
#         break
#     mapper[arr[i]]=i

# print(flag)



#Optimal Solution

arr=[2,6,5,8,11]

arr=sorted(arr)

target=int(input())
flag=0
i=0
j=len(arr)-1

while(i<j):
    t=arr[i]+arr[j]
    if(t==target):
        flag=1
        print("found at",[i,j])
        break
    elif(t>target):
        j-=1
    else:
        i+=1

print(flag)