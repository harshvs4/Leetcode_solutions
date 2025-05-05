# Last updated: 5/6/2025, 7:30:10 AM
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            if n == 1:
                return True
            visited.add(n)

            square = 0
            while n > 0:
                x = n%10
                square += (x**2)
                n //= 10
            n = square

        return False