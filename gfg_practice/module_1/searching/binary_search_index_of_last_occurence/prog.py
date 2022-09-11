

def get_index_of_last_occurence(arr: list, x: int):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2

        if (arr[mid] == x):
            # second condition is to check if the element after the last occurence is greater than the current element
            if mid == len(arr)-1 or x < arr[mid + 1]:
                return mid
            else:
                low = mid + 1
        elif (arr[mid] < x):
            low = mid+1
        elif (arr[mid] > x):
            high = mid-1
    return -1


def driver():
    print(get_index_of_last_occurence([1, 2, 2, 2, 3, 3, 3, 3, 4], 3))


if __name__ == "__main__":
    driver()
