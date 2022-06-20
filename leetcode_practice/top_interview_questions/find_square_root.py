class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x//2 # because a square root is always less than half that no.
        
        print(left, right)
        if x==1 or x==0:
            return x
        while (left <=right ):
            mid = (left + right) // 2
            
            # print (left, right,mid)
            
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif (mid*mid) > x:
                right = mid -1
            elif (mid*mid) < x:
                left = mid +1
    
    def mySqrt1(self, x: int) -> int:
        if (x == 0 or x == 1):
            return x
        i = 1; result = 1
        
        while (result <= x):
            i += 1
            result = i * i
            
        return i - 1
    