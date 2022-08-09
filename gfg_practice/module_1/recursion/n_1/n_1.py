def fun(n):
    """prints n to 1
    """

    if (n <= 0):
        return
    else:
        print(n)
        fun(n-1)
   
    

def driver():
    fun(18)

if __name__ == "__main__":
    driver()