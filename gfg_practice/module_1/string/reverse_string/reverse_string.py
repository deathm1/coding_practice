
def reverse_string_by_slicing(s:str):
    """Gets string inout and reverses it.

    Args:
        s (str): Input string

    Returns:
        str: Reversed string
    """
    return s[::-1]



def reverse_string_by_loop(s: str):
    """Gets string and reverses it by for loop

    Args:
        s (str): input string

    Returns:
        str: Output reversed string 
    """
    mystr = ''
    for character in s:
        mystr = character+mystr
    return mystr
def driver():
    print(reverse_string_by_loop("someString"))
    print(reverse_string_by_slicing("someString"))

if(__name__==r"__main__"):
    driver()