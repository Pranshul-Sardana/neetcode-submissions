class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []

        subset = []

        def dfs(i):
            if i == len(nums):
                ret.append(subset.copy())
                return None

            # Add element and run DFS
            #print(i)
            subset.append(nums[i])
            dfs(i+1)

            #Pop element and run DFS
            subset.pop()
            dfs(i+1)

        dfs(0)

        return ret