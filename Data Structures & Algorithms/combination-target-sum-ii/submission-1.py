class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # Sort
        candidates.sort()

        # Initiate Res
        res = []

        def dfs(i, total, curr):
            # If total reached, append to curr and return None
            # If total exceeded, return none
            if total == target:
                if curr not in res:
                    res.append(curr.copy())
                return None
            elif total > target or i == len(candidates):
                return None

            # Backtracking
            curr.append(candidates[i])
            dfs(i+1, total+candidates[i], curr)
            curr.pop()
            # Skip candidates
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, total, curr)
            
        # call dfs
        dfs(0,0,[])

        # return res
        return res