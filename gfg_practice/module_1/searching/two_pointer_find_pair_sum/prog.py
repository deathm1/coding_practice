def find_sum_pair(arr: list, elem: int):
    """Time complexity is O(n) and auxilliary space is O(1)
    """
    low = 0
    high = len(arr)-1

    while low < high:
        if arr[low] + arr[high] == elem:
            return True
        elif arr[low] + arr[high] < elem:
            low += 1
        else:
            high -= 1

    return False


def driver():
    l = [1, 2, 3, 4, 5, 6]
    print(find_sum_pair(l, 5))


if (__name__ == "__main__"):
    driver()
