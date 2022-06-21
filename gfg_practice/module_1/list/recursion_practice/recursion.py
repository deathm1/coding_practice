"""
T(n) = T(n/4) + T(n/2) + Cn
1
Cn
T(n/4)  T(n/2)

2
Cn
Cn/4    Cn/2
T(n/16) T(n/8)  T(n/8) T(n/4)


Cn                      Cn
Cn/4    Cn/2            3Cn/4
Cn/16 Cn/8  Cn/8 Cn/4   9Cn/16


total work O(n)



T(n) = T(n-1) + T(n-2) + C

1
C
T(n-1)  T(n-2)

2
C
2C
4C

Total Work Done O(2^n)
"""


def rec_ex_4(n):
    """Recursion Tree method

    T(n) = 2T(n/2) + C

    1
    C
    T(n/2)  T(n/2)

    2
    C
    C   C
    T(n/4)  T(n/4)  T(n/4)  T(n/4)

    Work Done Tree
    C               C
    C   C           2C
    C   C   C   C   4C

    C + 2C + 4C
    because of T(n/2) this series will have log(n) terms

    Sum = C(2^log(n) - 1) / r-1
    th(n)


    Args:
        n (_type_): _description_
    """
    if int(n)==1:
        return 
    print(n)

    rec_ex_4(n/2)
    rec_ex_4(n/2)

def rec_ex_3(n):
    """
    Recursion Tree Method

    Expression : T(n) = T(n/2) + C

    1
    C
    T(n/2)

    2
    C
    C
    T(n/4)

    Work Done
    C
    C
    C
    C

    Sum = C + C + C + C = th(log(n))

    T(n) = T(n/2) + th(log(n))

    Args:
        n (_type_): _description_
    """
    if int(n)==1:
        return
    print(n)
    rec_ex_3(n/2)
def rec_ex_2(n):
    """
    Recursion Tree Method

    T(n) = 2T(n-1) + C

    1
    C
    T(n-1)  T(n-1)
    
    2
    C
    C  C
    T(n-2)  T(n-2)  T(n-2)  T(n-2)

    Work Pattern

    C               C
    C   C           2C
    C   C   C   C   4C

    Sum = C + 2C + 4C....

    a(r^n-1)/r-1 => th(2^n)

    T(n) = 2T(n-1) + th(2^n)


    Args:
        n (_type_): _description_
    """
    if(n==1):
        return
    print(n)
    rec_ex_2(n-1)
    rec_ex_2(n-1)
def rec_print_gfg(n):
    """
    Recurrence Relation of this function
    T(n)= 2*T(n/2) + th(n)
    T(n)= 2T(n/2)[Recursive part] + Cn[Non recursive part]
    T(1)= th(1)

    Recursion Tree Method
    1
    Cn
    T(n/2)  T(n/2)

    2
    Cn => Cn
    Cn/2                Cn/2 => Cn
    T(n/4)  T(n/4)      T(n/4)  T(n/4) => Cn

    Total Work at every level
    We are dividing a number by 2 in every iteration = > log(n)
    Cn                             Cn
    Cn/2    Cn/2                   Cn
    Cn/4    Cn/4    Cn/4    Cn/4   Cn

    Total Work done = Cn*log(n)

    Cn - is the total work done in this tree
    log(n) = is because of T(n/2)

    T(n) = 2T(n/2) + th(nlog(n))



    Args:
        n (int): Number of times to be printed.
    """
    if int(n)==1:
        return

    my_arr = []
    for i in range(int(n)):
        my_arr.append(i)
    print(my_arr, n)
    rec_print_gfg(n/2)
    rec_print_gfg(n/2)


def driver():
    #rec_print_gfg(10)
    #rec_ex_2(5)
    rec_ex_3(10)

if(__name__ =="__main__"):
    driver()


