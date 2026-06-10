class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        parantheses = []
        for _ in range(n):
            parantheses.append("(")
            parantheses.append(")")

        answers = []
        combination = []
        # at each step we have two option, either to add ( or add ) 
        # we can make all cominations and then keep the ones that are valid using a 
        # stack
        def check_valid(comb):
            stack = []
            for p in comb:
                if p == "(":
                    stack.append(p)
                elif p == ")":
                    if not stack:
                        return False
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
            
            if not stack:
                return True
            if stack:
                return False


        def backtrack(open_n, close_n):
            print(combination, open_n, close_n)
            if open_n == close_n == n :
                # if valid add to answers
                if check_valid(combination):
                    answers.append("".join(combination.copy()))
                return
            
            # choice 1
            if open_n < n:
                combination.append("(")
                backtrack(open_n + 1, close_n)
                combination.pop()
        
            # choice 2
            if close_n < open_n:
                combination.append(")")
                backtrack(open_n , close_n + 1)
                combination.pop()

        backtrack(0, 0)

        return answers


