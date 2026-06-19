class solution:
    def search(self,nums: list[int], target: int) -> int:
     low=0
     high=len(num)-1
     while low<=high:
        mid = (low+right)//2 
        if nums [mid]== target: 
            return mid
        elif num[mid] < target:
            low=mid+1
        else:
            high=mid+1
    return-1      


