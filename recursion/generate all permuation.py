#brute force 
# def permuteall(arr, temp, ans, mapper):
#     if(len(temp)==len(arr)):
#         ans.append(temp[:])
#         return

#     for i in range(len(arr)):
#         if(mapper[i]==0):
#             mapper[i]=1
#             temp.append(arr[i])
#             permuteall(arr,temp,ans,mapper)
#             temp.pop()
#             mapper[i]=0


# arr=[2,1,3]
# temp=[]
# ans=[]
# mapper=[0]*len(arr)
# permuteall(arr,temp,ans,mapper)
# print(ans)




#optimal

def permuteall(arr, ans, counter):
    if(counter==len(arr)):
        ans.append(arr[:])
        return-

    for i in range(counter,len(arr)):
        arr[i],arr[counter]=arr[counter],arr[i]
        permuteall(arr,ans,counter+1)
        arr[i],arr[counter]=arr[counter],arr[i]

       

arr=[2,1,3]
ans=[]
permuteall(arr,ans,0)
print(ans)


