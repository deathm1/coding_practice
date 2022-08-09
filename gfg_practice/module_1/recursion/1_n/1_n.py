def fun(n):
    """This cprints 1 to n
    """

    if n == 0:
        return
    fun(n-1)
    print(n)
    

def driver():
    fun(18)

if __name__ == "__main__":
    driver()