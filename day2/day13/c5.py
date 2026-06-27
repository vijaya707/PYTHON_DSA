import heapq
nums=[3,2,1,7,5,6,4]
min_heap=[]
for i in nums:
    heapq.heappush(min_heap,i)
    if len(min_heap)>K:
        heapq_heappop(min_heap)
return min_heap[0] 