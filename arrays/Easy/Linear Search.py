#Brute Force and optimal

arr=[1,2,4,5,6,3]

num=int(input())

n=len(arr)

for i in arr:
   if (i==n):
       print("Found",i)
       break 