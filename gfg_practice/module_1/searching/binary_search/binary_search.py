def binary_search(arr : list, elem : int):
    """Time complexity is O(log n) and auxilliary space is O(1)
    """
    low = 0
    high = len(arr)-1

    while low<=high:
        mid = (low+high)//2

        if(arr[mid] == elem):
            return mid
        elif(arr[mid] < elem):
            low = mid + 1
        else:
            high = mid - 1
        

    return -1

def binary_search_recursion(l, x, low, high):
    """Time complexity is O(log n) and auxilliary space is O(log n) as recursive solution iwll take n stack calls
    """
    if low > high:
        return -1

    mid = (low+high) // 2

    if(l[mid] == x):
        return mid
    elif(l[mid] > x):
        return binary_search_recursion(l, x, low, mid-1)
    else:
        return binary_search_recursion(l, x, mid+1, high)



def driver():
    l = [10,20,30,40,50]
    print(binary_search_recursion(l, 21, 0, len(l)-1))
    #print(binary_search(l, 2))
    



if(__name__ == "__main__"):
    driver()