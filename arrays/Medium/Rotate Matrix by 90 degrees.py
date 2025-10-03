#Brute force

arr=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

n=len(arr)

matrix = []

rows, cols = n, n
matrix = [[0 for _ in range(cols)] for _ in range(rows)]


print("Before 90 rotation")

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()

print("After 90 rotation")

for i in range(n):
    for j in range(n):
        matrix[j][n-i-1]=arr[i][j]


for i in range(n):
    for j in range(n):
        print(matrix[i][j],end=" ")
    print()

#Optimal Solution


# arr=[[1,2,3],[4,5,6],[7,8,9]]

arr=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

n=len(arr)

matrix = []

rows, cols = n, n
matrix = [[0 for _ in range(cols)] for _ in range(rows)]


print("Before 90 rotation")

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()

print("After 90 rotation")

for i in range(n):
    for j in range(i,n):
       arr[i][j],arr[j][i]=arr[j][i],arr[i][j]
    
for i in range(n):
    arr[i]=arr[i][::-1]

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()