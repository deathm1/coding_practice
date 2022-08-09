#User function Template for python3

class Solution:
    #Complete this function
    def power(self,N,R):
        self.N = N
        if R == 0:
            return 1
            
        ans = self.power(self.N, R//2)
        
        if R%2==0:
            return (ans*ans)%(1000000007)
            
        else:
            return self.N*ans*ans%(1000000007)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends