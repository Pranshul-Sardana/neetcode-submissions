class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # Backtracking
        # Time complexity: target * len(nums)
        # Space complexity: len(nums)!

        # Initiate result
        res = []

        # Backtracking(index, curr_sum, curr_list)
        def dfs(i, curr_sum, curr_list):
            # If index == len(nums) or sum exceeds, return
            if i == len(nums) or curr_sum > target:
                return
            # elif curr_sum == target, append to res
            elif curr_sum == target:
                res.append(curr_list.copy())
                return

            # Add the current list
            # Recurse with i and curr_sum + curr_elem
            curr_list.append(nums[i])
            dfs(i, curr_sum+nums[i], curr_list)

            # Pop the elemetn
            # Recurse with i + 1 and curr_sum
            curr_list.pop()
            dfs(i+1, curr_sum, curr_list)

        # Call backtracking
        dfs(0, 0, [])

        # Return resutlt
        return res

