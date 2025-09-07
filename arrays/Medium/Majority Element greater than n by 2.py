#Brute Force

# arr=[2,2,1,3,3,2,2]

# n=len(arr)//2

# temp=0

# for i in range(len(arr)):
#     count=1
#     for j in range(len(arr)):
#         if(i!=j and arr[i]==arr[j]):
#             count+=1
#         if(count>n):
#             temp=arr[i]
#             break
# print(temp)


#Better Solution

# arr=[2,2,1,3,3,2,2]

# n=len(arr)//2

# mapper={}

# for i in arr:
#     mapper[i]=mapper.setdefault(i,0)+1

# for k,v in mapper.items():
#     if(v>n):
#         print(k)
#         break

#Optimal Solution(Moore's voting algorithm)

arr=[2,2,1,3,3,2,2]

n=len(arr)//2

count=0
count1=0

temp=0

for i in range(len(arr)):
    if(count==0):
        temp=arr[i]
        count+=1
    elif(arr[i]==temp):
        count+=1
    else:
        count-=1

for i in arr:
    if(i==temp):
        count1+=1

if(count1>n):
    print(temp)
else:
    print("No such element")