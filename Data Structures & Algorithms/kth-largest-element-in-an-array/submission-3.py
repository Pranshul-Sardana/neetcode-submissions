class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Turn the list to negative
        nums = [i*(-1) for i in nums]
        
        #Heapify
        heapq.heapify(nums)

        #Keep poping elements until heap length is k
        for i in range(k-1):
            heapq.heappop(nums)
        
        #Return the absolute of the 0-th element
        return nums[0]*(-1)