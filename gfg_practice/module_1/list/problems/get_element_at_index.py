#User function Template for python3

def getByIndex(arr,n,idx):
    if(idx>len(arr)-1):
        return -1
    else:
        return arr[idx]
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        
        idx=int(input())
        
        print(getByIndex(arr,n,idx))
# } Driver Code Ends