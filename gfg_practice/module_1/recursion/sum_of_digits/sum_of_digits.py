def fun(n):
    """This gets sum of digits
    """
    # return if there is single digit
    if n < 10:
        return n
    # this recursively adds the last digit (n%10) to the remaining digits (n//10)
    return fun(n//10) + n%10

    

def driver():
    print(fun(253))

if __name__ == "__main__":
    driver()