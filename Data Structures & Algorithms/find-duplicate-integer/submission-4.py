class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Use Floyd's algorithm

        #Stage 1: Use fast and slow pointers to obtain the location where they match
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        #Stage 2: Initiate a second slow pointer and find the location where they match
        slow2 = 0 
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow