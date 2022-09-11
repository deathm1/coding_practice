def find_sum_pair(arr: list, elem: int, si: int):
    """Time complexity is O(n) and auxilliary space is O(1)
    """
    low = si
    high = len(arr)-1

    while low < high:
        if arr[low] + arr[high] == elem:
            return True
        elif arr[low] + arr[high] < elem:
            low += 1
        else:
            high -= 1

    return False


def is_triplet(arr: list, elem: int):
    # -2 is there because we are checking it for 3 elements
    # why to check it when remaining elments are 2
    for i in range(len(arr)-2):
        if (find_sum_pair(arr, elem-arr[i], i+1)):
            return True
    return False


def driver():
    l = [2, 5, 10, 15, 18]
    print(is_triplet(l, 17))


if (__name__ == "__main__"):
    driver()
