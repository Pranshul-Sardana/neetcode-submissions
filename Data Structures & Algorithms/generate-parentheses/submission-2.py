class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # Backtracking

        # Empty list for return
        res = []

        def dfs(curr, o, c):
            # if o or c exceeds n or c exceeds o, return to the previous step
            if o > n or c > o :
                return 
            # if o=c=n, append to the list and Return to the previous step 
            if o == c == n:
                res.append(curr)
                return 
            
            # Add "(" to string and increase o, recurse
            dfs(curr+"(", o+1, c)
            # Add ")" to string and increase c, recurse
            dfs(curr+")", o, c+1)
        

        dfs("", 0, 0)

        # return the list
        return res