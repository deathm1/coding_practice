#User function Template for python3

"""
input - 
s - given string 

output - 
return 0 if not panagram else return 1
"""
class Solution:
    def isPanagram(self,s):
        if len(s)<26:
            return 0
        ret = 1
        
        a = [chr(i) for i in range(97,123)]
        
        for char in a:
            if (char not in s) and (char.upper() not in s):
                ret = 0
                break
            
        return ret
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(int(Solution().isPanagram(s)))
        t = t-1

# } Driver Code Ends