class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # Initiate res
        res = []

        def dfs(i, total, curr):
            # If target met, append in the res and return none
            # If target exceeded, return none
            if total == target:
                res.append(curr.copy())
                return None
            elif total > target or i == len(nums):
                return None

            # Backtracking
            curr.append(nums[i])
            dfs(i, total+nums[i], curr)
            curr.pop()
            dfs(i+1, total, curr)
            

        # call dfs
        dfs(0, 0, [])

        # return res
        return res
        