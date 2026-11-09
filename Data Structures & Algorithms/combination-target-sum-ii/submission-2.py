class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort
        candidates.sort()

        # Initiate Res
        res = []

        def dfs(i, total, curr):
            #edge case equality
            #edge case total is greater or i exceeds the len of candidates
            if total == target:
                res.append(curr.copy())
                return
            elif total > target or i == len(candidates):
                return

            # Backtracking
            # Append and recurse
            curr.append(candidates[i])
            dfs(i+1, total+candidates[i], curr)

            # Pop
            curr.pop()

            # Skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            # Recurse
            dfs(i+1, total, curr)


        # Call dfs
        dfs(0,0,[])

        # reutrn
        return res