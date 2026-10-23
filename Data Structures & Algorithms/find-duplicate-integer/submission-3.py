class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Get two pointer (fast and slow)
        slow, fast = 0, 0

        #Stage 1: Find where the slow and fast pointer intersect
        # Iterate
        #Increment the pointers
        #Break at intersection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        

        #Stage 2: Initiate a second slow pointer and find where the first and second slow meet
        #Initaite the second slow
        #Increment the points
        #Return where they overlap

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow