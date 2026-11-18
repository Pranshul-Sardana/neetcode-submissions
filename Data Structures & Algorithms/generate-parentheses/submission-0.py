class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # Initiate global res
        res = []
        stack = []

        # Backtrack(string, open count, close count)
        def dfs(o, c):
            if o == c == n: 
                res.append("".join(stack))
                return
            
            # if open less than n
            if o < n:
                # append open
                stack.append('(')
                # Recurse
                dfs(o+1, c)
                stack.pop()
                
            # If close count open count
            if c < o:
                # append close
                stack.append(")")
                # Recurse
                dfs(o, c+1)
                stack.pop()

        # Call backtrack
        dfs(0, 0)

        #Return res
        return res