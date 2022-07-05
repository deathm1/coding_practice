
def prefix_sum_and_hashing(my_list):
    prefix_sum = 0
    h = set()

    for i in range(len(my_list)):
        prefix_sum += my_list[i]
        if prefix_sum == 0 or prefix_sum in h:
            return True
        h.add(my_list[i])
    return False

def is_zero_sum_naive(my_list):
    """Here time complexity is O(n^2)
    Ineffiecinet solution

    Args:
        my_list (_type_): _description_

    Returns:
        _type_: _description_
    """
    n = len(my_list)
    for i in range(n):
        for j in range(i+1, n+1):
            if sum(my_list[i:j]) == 0:
                return True
    return False


def driver():
    print(prefix_sum_and_hashing([-3, 4, -3, -1, 1]))
    print(is_zero_sum_naive([-3, 4, -3, -1, 1]))

if(__name__=="__main__"):
    driver()