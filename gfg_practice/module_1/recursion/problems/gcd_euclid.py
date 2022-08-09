#User function Template for python3

class Solution:
    def GCD(self,a,b):
        if a == 0:
            return b
        return self.GCD(b%a, a)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ =='__main__':
    tcs= int(input())
    
    for _ in range(tcs):
        a,b=[int(x) for x in input().split()]
        ob=Solution()
        print(ob.GCD(a,b))
# } Driver Code Ends