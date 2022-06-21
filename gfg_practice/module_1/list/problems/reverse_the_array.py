#User function Template for python3

def reverseArray(arr,n):
    start = 0
    end = len(arr)-1
    
    
    while start<end:
        a = arr[start]
        b = arr[end]
        
        arr[start] = b
        arr[end] = a
        
        start+=1
        end-=1
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        
        reverseArray(arr,n)
        
        for e in arr:
            print(e,end=' ')
        print()
# } Driver Code Ends