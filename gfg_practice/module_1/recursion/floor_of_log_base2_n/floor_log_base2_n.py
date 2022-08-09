def fun(n):
    """This function returns floor of log2(n)
    """
    if n<= 1:
        return 0
    else:
        return 1 + fun(n//2)

def driver():
    print(fun(18))

if __name__ == "__main__":
    driver()