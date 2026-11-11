class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ## Backtracking

        nums.sort()

        # Initiate ret
        ret = []

        # Initiate local set
        curr = []

        # DFS
        def dfs(i):
            # If i equals len(nums)
            if i == len(nums):
                # If not in result, append local to result
                #if curr not in ret:
                ret.append(curr.copy())
                # Return to previous backtrack
                return

            # Append to local, recurse with i+1
            curr.append(nums[i])
            dfs(i+1)

            # Pop from local, recurse with i+1
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)

        # Call dfs
        dfs(0)

        # return global
        return ret