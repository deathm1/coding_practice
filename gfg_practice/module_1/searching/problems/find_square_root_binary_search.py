# User function Template for python3


# Complete this function
import math


class Solution:
    def floorSqrt(self, x):
        low = 1
        high = x

        while low <= high:
            mid = low+((high-low)//2)

            if mid*mid == x:
                return mid
            if mid*mid > x:
                high = mid - 1
            if mid*mid < x:
                low = mid + 1

        return high


# {
 # Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):

        x = int(input())

        print(Solution().floorSqrt(x))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
