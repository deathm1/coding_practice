#User function Template for python3

class Solution:
    def printArrayRecursively(self,arr,n):
        self.print_arr(arr, 0)
        
    def print_arr(self, arr, i):
        if i == len(arr):
            return
        
        print(arr[i], end=" ")
        
        return self.print_arr(arr, i+1)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs = int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        ob.printArrayRecursively(arr,n)
        print()
# } Driver Code Ends