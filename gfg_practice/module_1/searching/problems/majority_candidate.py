# User function template for Python 3

from sys import stdin
import math


class Solution:
    def majorityElement(self, arr, n):
        # Boyer-Moore Majority Vote Algorithm
        candidate = -1
        votes = 0

        # Finding majority candidate
        for i in range(n):
            if (votes == 0):
                candidate = arr[i]
                votes = 1
            else:
                if (arr[i] == candidate):
                    votes += 1
                else:
                    votes -= 1
        count = 0

        # Checking if majority candidate occurs more than n/2
        # times
        for i in range(n):
            if (arr[i] == candidate):
                count += 1

        if (count > n // 2):
            return candidate
        else:
            return -1


# {
 # Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(A, N))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
