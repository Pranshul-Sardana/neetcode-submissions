class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        for item in nums:
            if item in hashmap:
                return True
            else:
                hashmap.add(item)

        return False