#Brute Force
arr=[[1,1,1],[1,0,1],[1,0,0]]
n,m=len(arr),len(arr[0])
def markRow(i):
    for j in range(m):
        if(arr[i][j]!=0):
            arr[i][j]=-1
def markCol(j):
    for i in range(n):
        if(arr[i][j]!=0):
            arr[i][j]=-1

for i in range(n):
    for j in range(m):
        if(arr[i][j]==0):
            markRow(i)
            markCol(j)

for i in range(n):
    for j in range(m):
        if(arr[i][j]==-1):
            arr[i][j]=0

print(arr)

#Better Solution
arr=[[1,1,1],[1,0,1],[1,0,0]]
n,m=len(arr),len(arr[0])
R1=[0]*n
C1=[0]*m


for i in range(n):
    for j in range(m):
        if(arr[i][j]==0):
            R1[i]=-1
            C1[j]=-1

for i in range(n):
    for j in range(m):
        if(R1[i]==-1 or C1[j]==-1):
            arr[i][j]=0

print(arr)

#Optimal
arr=[[1,1,1,1],[1,0,1,1],[1,1,0,1],[0,1,1,1]]

n,m=len(arr),len(arr[0])

col0=1
if(arr[0][0]==0):
    col0=0

for j in range(1,m):
    if(arr[0][j]==0):
        arr[0][0]=0
        break

for i in range(1,n):
    if(arr[i][0]==0):
        col0=0
        break


for i in range(1,n):
    for j in range(1,m):
        if(arr[i][j]==0):
            arr[0][j]=0
            arr[i][0]=0





for i in range(1,n):
    for j in range(1,m):
        if(arr[0][j]==0 or arr[i][0]==0):
            arr[i][j]=0


if(arr[0][0]==0):
    for j in range(m):
        arr[0][j]=0

if(col0==0):
    for i in range(n):
        arr[i][0]=0



print(arr)