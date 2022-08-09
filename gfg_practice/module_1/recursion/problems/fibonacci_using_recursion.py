#User function Template for python3

class Solution:
    def fibonacci(self,n):
        
        if n == 1 or n ==2:
            return 1
        return self.fibonacci(n-1) + self.fibonacci(n-2)

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        ob=Solution()
        print(ob.fibonacci(n))
# } Driver Code Ends