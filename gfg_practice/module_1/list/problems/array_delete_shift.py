#User function Template for python3

def deleteFromArray(arr,n,idx):
    arr.pop(idx)
    arr.append(0)
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

#CONTRIBUTED BY RavinderSinghPB
if __name__ == '__main__':
    tcs= int(input())
    
    for _ in range(tcs):
        n=int(input())
        idx=int(input())
        
        arr=[i+1 for i in range(n)]
        
        deleteFromArray(arr,n,idx)
        
        for e in arr:
            print(e,end=' ')
        print()
        
# } Driver Code Ends    