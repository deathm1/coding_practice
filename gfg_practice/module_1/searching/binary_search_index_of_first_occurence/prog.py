def binary_search(arr: list, elem: int):
    """Time complexity is O(log n) and auxilliary space is O(1)
    """
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2
        if (arr[mid] == elem):
            # here we check if mid is at the first index or
            # the previous element is same as current
            if mid == 0 or arr[mid-1] != arr[mid]:
                return mid
            else:
                high = mid - 1
        elif (arr[mid] < elem):
            low = mid + 1
        elif (arr[mid] > elem):
            high = mid - 1

    return -1


def driver():
    l = [20, 20, 20, 40, 40]
    print(binary_search(l, 20))


if (__name__ == "__main__"):
    driver()
