

def ex_4(n):
    """Auxilary space is how much 
    is the order of growth of 
    extra space required by the operation.

    Space Complexity => O(n) or th(n)
    Auxilary Space => O(n) or th(n)

    Constant auxilary space as we do not need 
    anything other than input.

    fun(3)
    fun(2)
    fun(1)
    fun(0)

    Because of return n+ex_4(n-1) the existing state
    of function is stored in a stack adn from there it
    goes to the next state

    so our stack has 4 function states this means
    input was 3
    thats why O(n) or th(n)




    """


    if n<=0:
        return 0
    else:
        return n+ex_4(n-1)


def ex_3(l):
    """Auxilary space is how much 
    is the order of growth of 
    extra space required by the operation.

    Space Complexity => O(n) or th(n)
    Auxilary Space => O(1) or th(1)

    Constant auxilary space as we do not need 
    anything other than input.
    """


    sum = 0

    for x in l:
        sum = sum + x
    return sum

def ex_3(l):
    """Constant Space 

    Space Complexity => O(n) or th(n)

    because number of varables are constant
    """


    sum = 0

    for x in l:
        sum = sum + x
    return sum

def ex_2(n):
    """Constant Space 

    Space Complexity => O(1) or th(1)

    because number of varables are constant

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """


    sum = 0

    i = 1
    while i<=n:
        sum = sum+i
        i=i+1
    return sum

def ex_1(n):
    """Constant Space 

    Space Complexity => O(1) or th(1)

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    return n*(n+1)/2


def driver():
    pass

if(__name__=="__main"):
    driver()