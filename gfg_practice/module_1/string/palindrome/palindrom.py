
def check_palindrome(txt: str):
    low = 0
    high = len(txt)-1

    while low<high:
        if(txt[low]!=txt[high]):
            return False
        low+=1
        high-=1

    return True
    


def driver():
    print(check_palindrome("ABCA"))

if(__name__==r"__main__"):
    driver()