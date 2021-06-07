class Solution:
    # @param A : integer
    # @return an integer
    import math
    def isPrime(self, A):
        B = int(math.sqrt(A))
        if A<=1:
            return 0
            
        for i in range(2,B+1):
            if A % i == 0:
                return 0
        return 1
