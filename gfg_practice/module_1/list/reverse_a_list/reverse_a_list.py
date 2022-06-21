def reverse_list(my_list: list) -> int:
    """Gives max of integer

    Args:
        my_list (list): i/p

    Returns:
        int: max
    """
    e = len(my_list)-1

    s = 0

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
    print(reverse_list(my_list=my_arr))
if(__name__=="__main__"):
    main()