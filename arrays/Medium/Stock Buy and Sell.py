#Brute and Optimal Solution
arr=[7,1,5,3,6,4,0,10]

profit=0
mini=arr[0]

for i in range(1,len(arr)):
    cost=arr[i]-mini
    profit=max(profit,cost)
    mini=min(mini,arr[i])
print(profit)