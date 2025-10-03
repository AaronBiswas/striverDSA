#Optimal Solution

arr=[[1,2,3,4,5],
[16,17,18,19,6],
[15,24,25,20,7],
[14,23,22,21,8],
[13,12,11,10,9]]

ans=[]

top,left=0,0
n=len(arr)
bottom,right=n,n

while(left<right and top<bottom):
    for i in range(left,right):
        ans.append(arr[top][i])
    top+=1
    
    for i in range(top,bottom):
        ans.append(arr[i][right-1])
    right-=1
    
    if(top<bottom):
        for i in range(right-1,left-1,-1):
            ans.append(arr[bottom-1][i])
        bottom-=1
    
    if(left<right):
        for i in range(bottom-1,top-1,-1):
            ans.append(arr[i][left])
        left+=1
print(ans)
