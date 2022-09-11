def find_median(l1: list, l2: list):
    """Time complexity is O(log n) and auxilliary space is O(1)
    """
    n1, n2 = len(l1), len(l2)

    if n1 < n2:
        l1, l2 = l2, l1
        n1, n2 = len(l1), len(l2)

    b1, e1 = 0, n1

    while b1 <= e1:
        i1 = (b1 + e1) // 2
        i2 = (n1+n2+1)//2 - i1  # formula

        mnr1 = float('inf') if i1 == n1 else l1[i1]
        mxl1 = float('-inf') if i1 == 0 else l1[i1-1]
        mnr2 = l2[i2]
        mxl2 = l2[i2-1]

        if mxl1 <= mnr2 and mxl2 <= mnr1:
            if (n1+n2) % 2 == 0:
                return (max(mxl1, mxl2) + min(mnr1, mnr2))/2
            else:
                return max(mxl1, mxl2)
        elif mxl1 > mnr2:
            e1 = i1-1
        else:
            b1 = i1 + 1


def driver():
    l1 = [10, 20, 30]
    l2 = [5, 15, 25, 35, 45]
    print(find_median(l1, l2))


if (__name__ == "__main__"):
    driver()
