#User function Template for python3

class Solution:
    #Function to find element with more appearances between two elements in an array.    
    def majorityWins(self, arr, n, x, y):
        
        x_ctr = 0
        y_ctr = 0
        
        for i in arr:
            if(i==x):
                x_ctr+=1
            if(i==y):
                y_ctr+=1
                
        if(x_ctr>y_ctr):
            return x
        elif(y_ctr>x_ctr):
            return y
        else:
            return y if x>y else x
    

#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while(T>0):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        x,y=map(int,input().strip().split())
        
        print(Solution().majorityWins(arr,n,x,y))
        T-=1

# } Driver Code Ends