#User function Template for python3

def theSequence(n):
    """S(n) = n+ n*(S(n-1)) and S(0) = 1

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if n == 0:
        return 1
    return n + n*theSequence(n-1)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        
        print(theSequence(n))
# } Driver Code Ends