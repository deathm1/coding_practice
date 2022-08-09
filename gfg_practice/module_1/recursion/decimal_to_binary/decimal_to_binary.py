def fun(n):
    """This converts decimal to binary
    """

    if n == 0:
        return 0
    fun(n//2)
    print(n%2)
    

def driver():
    print(fun(18))

if __name__ == "__main__":
    driver()