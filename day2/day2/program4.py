#print all unique pair combinations in the
nums=input().split(',')
l=len(nums) #4
for i in range(l):
    for j in range(i+1,l):
        print(nums[i],nums[j])