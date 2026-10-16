class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #Initiate global and local lists
        res = []

        subset = []

        #Implement DFS
        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return

            # Add an element and run dfs
            subset.append(nums[i])
            dfs(i+1)

            # Pop and run dfs
            subset.pop()
            dfs(i+1)

        #Call DFS
        dfs(0)

        return res