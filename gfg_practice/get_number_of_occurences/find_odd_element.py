def get_maximum(my_list: list) -> int:
    """ Naive approach will be to use count and %2

    Args:
        my_list (list): i/p

    Returns:
        int: max
    """
    if(len(my_list)==1):
        return my_list[0]
    elif(len(my_list)<1):
        return None
    storage = 0
    for element in my_list:
        storage = storage ^ element
    return False if storage==1 else True
def main():
    """Driver
    """
    my_arr = [1, 1,2,2,3,3,4,3,5,5,6,6,6]
    print(get_maximum(my_list=my_arr))
if(__name__=="__main__"):
    main()