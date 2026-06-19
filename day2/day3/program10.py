nums=[5,4,3,1,2]
def s(nums):
     if len(nums)<=1: return nums
     L=len(nums)
     left=nums[:L//2]
     right=nums[L//2:]
     print(s(left),s(right))  
     return nums
s(nums)