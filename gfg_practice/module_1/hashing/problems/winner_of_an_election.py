#User function Template for python3

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner1(self,arr,n):
        candidates_vote = {}
        
        for name in arr:
            votes = arr.count(name)
            if votes in candidates_vote:
                name = min(name, candidates_vote[votes])
            candidates_vote[votes] = name
            
        
        max_vote = max(candidates_vote.keys())
        return candidates_vote[max_vote], max_vote
    
    def winner(self,arr,n):
        from collections import Counter
        counter_dict = Counter(arr)
        max_val = [max(counter_dict.values())]
        
        d = [k for k,v in counter_dict.items() if v == max_val[0]]
        d.sort()
        return (d[0], max_val[0])
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])
# } Driver Code Ends