class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Backtracking

        #Sort to avoid repeats
        nums.sort()

        # Global ret
        res = []

        # Local update
        curr = []

        # DFS(i)
        def dfs(i):
            # if i reaches length, append a copy to global
            if i == len(nums):
                res.append(curr.copy())
                return

            # append current indx nums to local and run recursion with the next step
            curr.append(nums[i])
            dfs(i+1)

            # Pop the most recent element
            curr.pop()

            # while you see repeats, skip index
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            # run recursion with the next step
            dfs(i+1)

            
        # Call dfs
        dfs(0)

        #Return
        return res