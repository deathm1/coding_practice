#User function Template for python3

class Solution:
    
    def is_palin(self, s, i):
        if i > len(s) / 2:
            return True
            
        return s[i] == s[len(s)-i-1] and self.is_palin(s, i+1)
    
    
    def isPalin(self, N):
        return self.is_palin(str(N), 0)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        obj = Solution()
        print(int(obj.isPalin(n)))
# } Driver Code Ends