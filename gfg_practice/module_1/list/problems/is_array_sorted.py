#User function Template for python3

class Solution:
    def isSorted(self,arr,n):

        for i in range(1, n-1):
            if(arr[i-1] <=arr[i]<=arr[i+1] or arr[i-1] >=arr[i]>=arr[i+1]):
                continue
            else:
                return 0
        return 1
            
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

if __name__ =='__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        
        print(Solution().isSorted(arr,n))
# } Driver Code Ends