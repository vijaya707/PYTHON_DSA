import heapq
nums=[5,7,8,9,10]
min_heap=[]
for i in nums:
    heapq.heappush(min_heap,i)
for i in nums:
    print(min_heap[0],min_heap)
    heapq.heappop(min_heap)    
    