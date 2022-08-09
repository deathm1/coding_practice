def TOH(n, source, auxiliary, destination):
    """This gets instructions for tower of hanoi.
    T(1) = 1
    T(n) = 2T(n-1) + 1

    1
    T(n-1)  T(n-1)

    1
    1   1
    T(n-1)  T(n-1)  T(n-1)  T(n-1)

    1               1
    1   1           2
    1   1   1   1   4
    so on

    T(n) = 2^0 + 2^1 + 2^2 + ......2^(n-1)

    T(n) = n(2^n - 1)/2 - 1  [GP formula]

    = 2^n-1

    time complexity = Theeta(2^n - 1)

    """
    if(n == 1):
        print(f"Move 1 from {source} to {destination}")

        # this gets number of moves
        return 1
    else:
        #move from a to b using c as aux
        TOH(n-1, source=source, auxiliary=destination, destination=auxiliary)


        print(f"Move {n} from {source} to {destination}")

        # move from b to c using a as aux
        TOH(n-1, source=auxiliary, auxiliary=source, destination=destination)

        # this gets number of moves
        return 2**n-1

    

def driver():
    print(TOH(3, 'A', 'B', 'C'))

if __name__ == "__main__":
    driver()