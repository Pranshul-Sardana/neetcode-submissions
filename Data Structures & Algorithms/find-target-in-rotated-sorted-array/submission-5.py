class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Initiate pointers
        l, r = 0, len(nums) - 1

        #Apply binary search
        #Use middle and left ptr to identify what part of array we are in
        while l <= r:
            m = (l+r)//2

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1

            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

        return -1
        