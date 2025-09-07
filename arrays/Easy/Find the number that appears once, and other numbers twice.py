#brute Force
# arr=[1,1,2,5,9,11,11,9,2]

# ans=-1

# for i in range(len(arr)):
#     count=1
#     curr=arr[i]
#     for j in range(len(arr)):
#         if(arr[j]==curr and i!=j):
#             count+=1
#     if(count==1):
#         ans=curr
#         break
# print(ans)

#Better

# dic={}

# arr=[1,1,2,5,9,11,11,9,2]

# for i in arr:
#     dic[i]=dic.setdefault(i,0)+1
# for k,v in dic.items():
#     if(v==1):
#         print(k)
#         break

#optimal

xor=0
arr=[1,1,2,5,5,11,11,9,2]

for i in arr:
    xor^=i
print(xor)