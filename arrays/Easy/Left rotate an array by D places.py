arr=[1,2,3,4]

d=int(input())

n=len(arr)

#Brute Force

# d=d%n
# temp=[]

# for i in range(d):
#     temp.append(arr[i])
# for i in range(d,n):
#     arr[i-d]=arr[i]
# for i in range(n-d,n):
#     arr[i]=temp[i-(n-d)]


#Optimal solution

arr[:d]=arr[:d][::-1]
arr[d:]=arr[d:][::-1]
arr=arr[::-1]
    
print(arr)