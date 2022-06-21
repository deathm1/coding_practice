#User function Template for python3

# inf has been imported in driver code

#Asked in VMWARE

def maximumElement(arr,n):
    maximum = arr[0]
    
    for i in arr[1:]:
        if(i>maximum):
            maximum = i
    return maximum
def minimumElement(arr,n):
    minimum = arr[0]
    
    for i in arr[1:]:
        if(i<minimum):
            minimum = i
            
    return minimum

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
        
        max_=maximumElement(arr,n,)
        min_=minimumElement(arr,n)
        print(max_,min_)
# } Driver Code Ends