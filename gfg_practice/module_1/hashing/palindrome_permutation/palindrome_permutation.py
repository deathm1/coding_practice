from collections import Counter


def is_palindrome(my_str : str):
    """Total time complexity will be Theeta(n)

    Args:
        my_str (str): _description_

    Returns:
        _type_: _description_
    """

    # this is Theeta(n)
    cnt = Counter(my_str)
    odd_freq = 0


    # This is O(n)
    for freqency in cnt.values():
        if freqency%2!=0:
            odd_freq+=1
            if(odd_freq>1):
                return False
    return True

def driver():
    print(is_palindrome("abaaac"))

if __name__ == "__main__":
    driver()