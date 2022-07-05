

def get_unicode_ascii():
    """To get unicode / Ascii values we use ord()
    to get character from integer we use chr()
    """

    print(ord('A'))
    print(ord('a'))
    print(ord('Z'))
    print(ord('z'))

    print(chr(4645))



def compare_strings():
    print("abcd" > "ABD")
    """here the first character of the string is 
    compared by its UNICODE or ASCII values.
    """
def driver():
    compare_strings()
    get_unicode_ascii()

if(__name__==r"__main__"):
    driver()