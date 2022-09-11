# User function Template for python3

import math


class Solution:
    # Complete this code
    def countOnes(self, arr, N):
        low = 0
        high = N - 1

        while low <= high:
            mid = (low+high)//2

            if arr[mid] == 0:
                high = mid - 1
            elif mid+1 < N and arr[mid+1] == 1:
                low = mid + 1
            else:
                return mid + 1
        return 0


# {
 # Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]

        ob = Solution()
        print(ob.countOnes(A, N))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
