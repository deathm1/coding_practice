def left_rotate_by_function(my_list: list) -> int:
    """Gives max of integer

    Args:
        my_list (list): i/p

    Returns:
        int: max
    """
    my_list.append(my_list.pop(0))
    
    return my_list

def left_rotate_by_slicing(my_list: list) -> int:
    """Gives max of integer

    Args:
        my_list (list): i/p

    Returns:
        int: max
    """
    my_list = my_list[1:] + my_list[0:1]
    
    return my_list

def left_rotate_by_loop(my_list: list) -> int:
    """Gives max of integer

    Args:
        my_list (list): i/p

    Returns:
        int: max
    """
    endel = my_list[0]
    for i in range(1, len(my_list)):
        my_list[i-1] = my_list[i]


    my_list[len(my_list)-1] = endel
    
    return my_list


def main():
    """Driver
    """
    my_arr = [1,2,3,5,6]
    print(left_rotate_by_loop(my_list=my_arr))
if(__name__=="__main__"):
    main()