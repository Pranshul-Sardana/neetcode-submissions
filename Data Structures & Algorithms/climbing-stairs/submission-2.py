class Solution:
    def climbStairs(self, n: int) -> int:
        ## Solving by bottom-up DP ##

        one, two = 1, 1

        for _ in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one