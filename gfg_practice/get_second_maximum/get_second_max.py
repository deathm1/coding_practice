def get_maximum(my_list: list) -> int:
    """Gives max of integer

    Args:
        my_list (list): i/p

    Returns:
        int: max
    """
    if(len(my_list)==1):
        return my_list[0]
    elif(len(my_list)<1):
        return None
    maximum = my_list[0]
    second_maximum = my_list[0]
    for element in my_list[1:]:
        if(element>maximum):
            second_maximum = maximum
            maximum = element
    return second_maximum
def main():
    """Driver
    """
    my_arr = [1,2,2,3,4,5,5,6,6, 4, 3, 5, 7]
    print(get_maximum(my_list=my_arr))
if(__name__=="__main__"):
    main()