def first_occurence(arr: list, elem: int):
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


def last_occurence(arr: list, elem: int):
    """Time complexity is O(log n) and auxilliary space is O(1)
    """
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2
        if (arr[mid] == elem):
            # here we check if mid is at the first index or
            # the previous element is same as current
            if mid == len(arr)-1 or elem < arr[mid+1]:
                return mid
            else:
                low = mid + 1
        elif (arr[mid] < elem):
            low = mid + 1
        elif (arr[mid] > elem):
            high = mid - 1

    return -1


def count_occurences(arr: list, elem: int):
    fo = first_occurence(arr, elem)

    if fo == -1:
        return 0
    else:
        return last_occurence(arr, elem) - fo + 1


def driver():
    l = [20, 20, 20, 40, 40, 50]
    print(count_occurences(l, 50))


if (__name__ == "__main__"):
    driver()
