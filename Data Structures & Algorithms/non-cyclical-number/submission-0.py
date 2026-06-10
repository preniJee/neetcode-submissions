class Solution:
    def isHappy(self, n: int) -> bool:

        visited = set()
        visited.add(n)

        digits = str(n)
        digits = [int(digit) for digit in digits]
        
        while True:
            d_sum = 0
            for d in digits :
                d_sum += d ** 2
            
            if d_sum == 1:
                return True
            if d_sum in visited:
                return False
            visited.add(d_sum)

            digits = str(d_sum)
            digits = [int(digit) for digit in digits]




        