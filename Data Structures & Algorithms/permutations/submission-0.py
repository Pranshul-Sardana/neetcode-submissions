class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # Global permutations (return)
        perms = [[]]

        # Iterate for each number
        for num in nums:
            # temp perms
            temp = []
            # for each element in global perms
            for p in perms:
                # iterate at each location (0, n+1)
                for i in range(0,len(p)+1):
                    # Get a copy of global perms
                    p_copy = p.copy()
                    # Insert new number at every location
                    p_copy.insert(i, num)
                    # Append things to the temp perms
                    temp.append(p_copy)

            # Append to global perms
            perms = temp

        # Return global perms
        return perms