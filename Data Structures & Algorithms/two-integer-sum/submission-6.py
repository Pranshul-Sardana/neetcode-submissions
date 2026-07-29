class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        hashmap = {}

        for i, item in enumerate(nums):
            diff = target - item
            if diff in hashmap.keys():
                return [hashmap[diff], i]
            else:
                hashmap[nums[i]] = i