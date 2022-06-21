#User function Template for python3

class Solution:
    def greaterThanX(self,arr,n,x):
        ctr = 0
        for i in arr:
            if i>x:
                ctr+=1
        return ctr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ =='__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(e) for e in input().split()]
        x=int(input())
        ob=Solution()
        ans=ob.greaterThanX(arr,n,x)
        print(ans)
# } Driver Code Ends