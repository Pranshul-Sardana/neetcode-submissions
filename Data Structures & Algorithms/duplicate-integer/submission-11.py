class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for item in nums:
            if item in hashSet:
                return True
            else:
                hashSet.add(item)

        return False