#Brute force

# arr=[1,2,0,4,0,5,0,9,8]
# temp=[]

# zero_count=0

# for i in arr:
#     if (i!=0):
#         temp.append(i)
#     else:
#         zero_count+=1
# arr=temp+([0]*zero_count)

# print(arr)

#optimal solution

arr=[1,2,0,4,0,5,0,9,8]

j=-1

for i in range(len(arr)):
    if(arr[i]==0):
        j=i
        break
for i in range(j+1,len(arr)):
    if(arr[i]!=0):
        arr[i],arr[j]=arr[j],arr[i]
        j+=1
print(arr)