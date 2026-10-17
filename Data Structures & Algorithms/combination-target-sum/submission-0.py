class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #Initiate return array
        ret = []
        #DFS
        def dfs(i, curr, total):
            #If sum reached, append to return array
            if target == total:
                ret.append(curr.copy())
                return
            #If total > target or iterating above the element, end search
            if total > target or i == len(nums):
                return

            #DFS with current element and updated sum
            #DFS with new element and current sum
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i+1, curr, total)

        #Call DFS
        dfs(0, [], 0)

        #Return
        return ret