class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ## Backtracking

        # Initiate an empty list
        ret = []

        # DFS(i, curr)
        def dfs(i, curr):
            # When index reached, append to local
            if i == len(nums):
                ret.append(curr.copy())
                return

            # Append to subset, run DFS with next index
            curr.append(nums[i])
            dfs(i+1, curr)

            # Pop from the subset, run DFS with next index
            curr.pop()
            dfs(i+1, curr)

        # Call DfS
        dfs(0, [])

        # Return
        return ret
