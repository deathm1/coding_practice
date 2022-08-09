def jos(n, k):
    """This is the josephus problem.
    here each kth person out of n persons is killed.
    T(1) = Theeta(1)
    T(n) = T(n-1) + Theeta(1)
    Constant amount of work in every iteration 
    so Time complexity is = Theeta(n)
    """
    if(n == 1):
        return 0
    else:
        # we are adding k to jos(n-1,k) to match the required case 
        # %n (modular arithmetic) is make sure result is from 0 
        # to n-1 because the sum can become more than n
        return (jos(n-1, k) + k)%n


def josBeginsWith1 (n, k):
    return jos(n, k) + 1

    

def driver():
    print(jos(5,3))

if __name__ == "__main__":
    driver()