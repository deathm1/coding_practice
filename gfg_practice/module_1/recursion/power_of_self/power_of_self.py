def power_of_self1(n, k):
    if k == 0:
        return 1
    return n * power_of_self(n, k-1)
def power_of_self(n, k):
    return power_of_self1(n, k)%1000000007






    

def driver():
    print(power_of_self(605,506))

if __name__ == "__main__":
    driver()