#{ 
#Driver Code Starts
#Initial Template for Python 3


import math



 # } Driver Code Ends
#User function Template for python3

class Solution:
    ##Complete the below codes
    #Function to find median of the array elements.
    def median(self,A,N):
        
        A.sort()
        
        
        
        if(len(A)%2==0):
            my_mid = int(len(A)/2)
            return int((A[my_mid]+A[my_mid-1])/2)
        else:
            return A[int(len(A)/2)]
     
    #Function to find mean of the array elements.   
    def mean(self,A,N):
        my_sum = 0
        
        
        for i in A:
            my_sum+=i
        return int(my_sum/len(A)) 

#{ 
#Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        a=[int(x) for x in input().strip().split()]
        ob=Solution()
        print(ob.mean(a,N),ob.median(a,N))
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends