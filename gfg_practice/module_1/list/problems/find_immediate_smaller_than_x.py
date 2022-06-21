#User function Template for python3

class Solution:
    def immediateSmaller(self,arr,n,x):
        maximum = -1
        for i in arr:
            if(i<x):
                
                if(i>maximum):
                    maximum = i

                
        return maximum
                
            

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
        ans=ob.immediateSmaller(arr,n,x)
        print(ans)
# } Driver Code Ends