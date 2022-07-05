
#User function Template for python3


class Solution:
    
    #Complete this code
    #Function to return the count of non-repeated elements in the array.
    def countNonRepeated(self,arr,n):
        my_dict = {}
        ctr = 0
        
        for i in range(n):
            
            my_dict[arr[i]] = my_dict.get(arr[i], 0) + 1
                
        
        for elem in my_dict:
            if(my_dict.get(elem)==1):
                ctr+=1
        return ctr
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        print(Solution().countNonRepeated(arr,n))
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends