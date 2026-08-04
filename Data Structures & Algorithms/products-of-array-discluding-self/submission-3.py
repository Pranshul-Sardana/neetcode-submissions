class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out_arr = [1]*len(nums)

        prefix = 1
        for i in range(len(nums)):
            out_arr[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1, -1):
            out_arr[i] *= postfix
            postfix *= nums[i]

        return out_arr
            