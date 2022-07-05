#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

##Complete this function
#Function to check if there is a pair with the given sum in the array.
def sumExists(arr, N, sumx):
    for i in arr:
        required_value = sumx - i
        # second condition is to check whether the req val is not equal to itself 
        # 
        # 7
        # 61 14 75 71 36 34 12
        # 68
        if required_value in arr and required_value !=i:
            return 1
    return 0

#{ 
#Driver Code Starts.

def main():
    testcases=int(input())
    while(testcases>0):
        
        N=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        
        sum=int(input())
        
        
        print(sumExists(arr,N,sum))
        
        testcases-=1
        
        

if __name__=="__main__":
    main()
#} Driver Code Ends