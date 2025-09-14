#brute force 
# arr = [1,2,-5,-6,4,-8,2,0,-1]
# neg =[]
# pos =[]

# for i in arr:
#     if(i<0):
#         neg.append(i)
#     else:
#         pos.append(i)

# j=0
# z=0

# for i in range(len(arr)):
#     if(i%2):
#         arr[i]=neg[j]
#         j+=1
#     else:
#         arr[i]=pos[z]
#         z+=1
# print(arr)





#brute force 2 pointer
# arr = [1,2,-5,-6,4,-8,2,0,-1]
# ans=[0]*len(arr)
# pos=0 
# neg=1


# for i in arr:
#     if(i<0):
#         ans[neg]=i
#         neg+=2
#     else:
#         ans[pos]=i
#         pos+=2


# print(ans)



#Another vairiant of the previous question this is for un even array elements postives and negatives count
arr = [1,2,-5,-6,4,-8,2,0,-1,-1,-2,-3,-5]
pos=[]
neg=[]


for i in arr:
    if(i<0):
        neg.append(i)
    else:
        pos.append(i)


if(len(pos)>len(neg)):
    for i in range(len(neg)):
        arr[2*i]=pos[i]
        arr[i*2+1]=neg[i]
    j=len(neg)*2    
    for i in range(len(neg),len(pos)):
        arr[j]=pos[i]
        j+=1

else:
    for i in range(len(pos)):
        arr[2*i]=pos[i]
        arr[i*2+1]=neg[i]
    j=len(pos)*2    
    for i in range(len(pos),len(neg)):
        arr[j]=neg[i]
        j+=1


print(arr)
