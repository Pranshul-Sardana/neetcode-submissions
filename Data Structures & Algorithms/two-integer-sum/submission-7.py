class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, val in enumerate(nums):
            diff = target - val
            if diff in hashmap.keys():
                return [hashmap[diff], i]
            else:
                hashmap[val] = i