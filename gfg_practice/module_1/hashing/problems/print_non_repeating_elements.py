#User function Template for python3
class Solution:
    
    #Complete this function
    #Function to return non-repeated elements in the array.
    def printNonRepeated(self,arr,n):
        my_dict = {}
        res=[]

        
        for i in range(n):
            my_dict[arr[i]] = my_dict.get(arr[i], 0) + 1
            
                
        for elem in arr:
            if(my_dict[elem]==1):
                res.append(elem)
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        l = Solution().printNonRepeated(arr,n)
        print(*l)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends