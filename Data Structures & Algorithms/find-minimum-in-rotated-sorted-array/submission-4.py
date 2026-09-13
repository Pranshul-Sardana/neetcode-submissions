class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        smallest = nums[l]

        while l <= r:
            
            m = (l+r)//2

            if nums[m] <= nums[r]:
                r = m - 1
            else:
                l = m + 1

            smallest = min(nums[m], smallest)

        return smallest