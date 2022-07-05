#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

#Function to check if two numbers in the array have sum equal to the given sum.
def sumExists(arr, N, sumx):
    d = set(arr)
    
    
    for i in range(N):
        s = sumx - arr[i]
        
        if s in d and s!=arr[i]:
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