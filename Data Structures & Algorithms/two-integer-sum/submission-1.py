class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Sort the list in ascending order
        #nums = sorted(nums)

        #Iterate over the elements
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    print(f"{nums[i] = } + {nums[j] = }")
                    return [i, j]