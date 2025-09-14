# #Brute Force
# import sys

# def maxSubarraySum(arr, n): 
#     maxi = -sys.maxsize - 1 # infinite negative

#     for i in range(n):
#         sum = 0
#         for j in range(i, n):
#             # current subarray = arr[i.....j]

#             #add the current element arr[j]
#             # to the sum i.e. sum of arr[i...j-1]
#             sum += arr[j]

#             maxi = max(maxi, sum) # getting the maximum

#     return maxi

# arr = [ -2, 1, -3, 4, -1, 2, 1, -5, 4]
# n = len(arr)
# maxSum = maxSubarraySum(arr, n)
# print("The maximum subarray sum is:", maxSum)

#Optimal Solution
#this solution is also for Print subarray with maximum subarray sum (extended version of above problem)
arr=[-2,-3,4,-1,-2,1,5,-3]


summ=0
maxi=10**(-18)
start=-1
ansstart=-1
ansend=-1

for i in range(len(arr)):
    if(summ==0):
        start=i
    summ+=arr[i]
    if(summ>maxi):
        maxi=summ
        ansstart=start
        ansend=i
    if(summ<0):
        summ=0
        
print(maxi,ansstart,ansend)