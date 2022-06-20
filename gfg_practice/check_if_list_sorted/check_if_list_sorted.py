def check_if_list_sorted(my_list: list) -> bool:
    """Gives max of integer

    Args:
        my_list (list): i/p

    Returns:
        int: max
    """
    for i in range(1, len(my_list)):
        if(my_list[i]<my_list[i-1]):
            return False
    return True
    
def main():
    """Driver
    """
    my_arr = [1,2,2,3,4,5,5,6,6, 7, 8, 8, 9, 10,2]
    print("Sorted List" if check_if_list_sorted(my_list=my_arr) else "List is not sorted")
if(__name__=="__main__"):
    main()