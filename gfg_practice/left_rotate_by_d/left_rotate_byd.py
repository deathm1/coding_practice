from collections import deque


def left_rotate_by_deque(my_list: list, d:int) -> list:
    """Gives max of integer

    Args:
        my_list (list): i/p

    Returns:
        int: max
    """
    dq = deque(my_list)
    dq.rotate(-d)
    
    return list(dq)

def left_rotate_by_slicing(my_list: list, d:int) -> list:
    """Gives max of integer

    Args:
        my_list (list): i/p

    Returns:
        int: max
    """
    my_list = my_list[d:] + my_list[0:d]
    
    return my_list

def left_rotate_by_loop_naive(my_list: list, d:int) -> list:
    """Takes more auxilary space Theeta O(nd)

    Args:
        my_list (list): i/p

    Returns:
        int: max
    """

    for i in range(0, d):
        my_list.append(my_list.pop(0))
    return my_list


def left_rotate_by_3_reverse(my_list: list, d:int) -> list:
    """Efficient solution O(n) Auxilary space O(1)

    Args:
        my_list (list): i/p

    Returns:
        int: max
    """
    n = len(my_list)
    my_list = reverse_list(my_list, 0, d-1)
    my_list = reverse_list(my_list, d, n-1)
    my_list = reverse_list(my_list, 0, n-1)
    return my_list


def reverse_list(my_list: list, s, e) -> int:
    """Gives max of integer

    Args:
        my_list (list): i/p

    Returns:
        int: max
    """
    while s<e:
        a = my_list[s]
        b = my_list[e]
        my_list[s] = b
        my_list[e] = a
        s+=1
        e-=1
    
    return my_list


def main():
    """Driver
    """
    my_arr = [1,2,3,5,6]
    print(left_rotate_by_3_reverse(my_arr,2))
if(__name__=="__main__"):
    main()