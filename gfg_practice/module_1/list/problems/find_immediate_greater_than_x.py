#User function Template for python3

class Solution:
    # inf has been imported in driver code
    def immediateGreater(self,arr,n,x):
        res = -1
        store_diff = 100000
        for i in arr:
            if(i>x):
                diff = i-x
                if(diff<store_diff):
                    res = i
                    store_diff = diff
                
                
                
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    from math import inf
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(e) for e in input().split()]
        x=int(input())
        
        ans=Solution().immediateGreater(arr,n,x)
        print(ans)
# } Driver Code Ends