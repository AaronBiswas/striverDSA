#Brute Force
#use merge sort

#Better Solution

# arr=[0,1,2,0,1,1,0,2,2]

# c0,c1,c2=0,0,0


# for i in arr:
#     if(i==0):
#         c0+=1
#     elif(i==1):
#         c1+=1
#     else:
#         c2+=1
# for i in range(c0):
#     arr[i]=0
# for i in range(c0,c0+c1):
#     arr[i]=1
# for i in range(c0+c1,len(arr)):
#     arr[i]=2
    
# print(arr)



#Optimal Solution
arr=[0,1,2,0,1,1,0,2,2,0]

low=0
mid=0
high=len(arr)-1

while(mid<=high):
    if(arr[mid]==0):
        arr[low],arr[mid]=arr[mid],arr[low]
        mid+=1
        low+=1
    elif(arr[mid]==1):
        mid+=1
    else:
        arr[mid],arr[high]=arr[high],arr[mid]
        high-=1
    
print(arr)