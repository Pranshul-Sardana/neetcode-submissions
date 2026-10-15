class Solution:
    def rob(self, nums: List[int]) -> int:
        #Split the circular problem into 2 linear sub-problems
        #Rob either the first house, or the last house, or neither
        return max(nums[0], self.help(nums[1:]), self.help(nums[:-1]))

    def help(self, nums):
        #Initial rob amount
        rob1, rob2 = 0, 0

        #Iterate through elements
        for item in nums:
            temp = max(rob1+item, rob2)
            rob1 = rob2
            rob2 = temp

        #Return max amount
        return max(rob1, rob2)