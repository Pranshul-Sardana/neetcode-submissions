class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # Initiate global res
        res = []

        # Backtrack(string, open count, close count)
        def dfs(string, o, c):
            if o == c == n: 
                res.append(string)
                return
            
            # if open less than n
            if o < n:
                # append open
                dfs(string+'(', o+1, c)
            # If close count open count
            if c < o:
                # Recurse
                dfs(string+')', o, c+1)

        # Call backtrack
        dfs("", 0, 0)

        #Return res
        return res