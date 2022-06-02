class Solution:
    def numberOfSteps(self, num: int) -> int:
        step_counter = 0
        
        while num!=0:
            if(num%2):
                num -= 1
            else:
                num /=2
            step_counter +=1
        return step_counter
    
    def numberOfSteps2(self, n: int) -> int:
        c = 0
        while n != 0: n, c = n - 1 if n % 2 else n//2, c + 1
        return c