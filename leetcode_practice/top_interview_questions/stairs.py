class Solution:
    def climbStairs(self, n: int) -> int:
        if  n==1:
            return 1
        num1 = 1
        num2 = 1
        my_sum = 0
        
        # get fibonacci sequence sum one less than original sequence
        for i in range(n-1):
            my_sum = num1 + num2
            num1 = num2
            num2 = my_sum
        return my_sum