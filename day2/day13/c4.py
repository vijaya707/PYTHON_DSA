import heapq
nums=[10,8,20,7,6,15]
nums=[-num for num in nums]
heapq.heapify(nums)
print(nums)
nums=(-num for num in nums)
print(nums)


#heappush
import heapq
nums=[10,8,20,7,6,15]
max_heap=[]
nums=[-num for num in nums]
for i in nums:
    heapq.heappush(max_heap,i)
for i in nums:
    print(max_heap)
    heapq.heappop(max_heap) 
