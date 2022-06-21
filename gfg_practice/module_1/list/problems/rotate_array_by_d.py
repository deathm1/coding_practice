#User function Template for python3

import traceback

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        #using 3 reverse technique

        D = D%N
        # this is used to make sure D does not cross N

        
        
        A = self.reverse_list(A, 0, D-1)
        A = self.reverse_list(A, D, N-1)
        A = self.reverse_list(A, 0, N-1)

        
    def reverse_list(self, my_list, s, e):
        while s<e:
            a = my_list[s]
            b = my_list[e]
            my_list[s] = b
            my_list[e] = a
            s+=1
            e-=1
        
        return my_list

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
def main():
    T=int(input())
    
    while(T>0):
        nd=[int(x) for x in input().strip().split()]
        N=nd[0]
        D=nd[1]
        A=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.rotateArr(A,D,N)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends