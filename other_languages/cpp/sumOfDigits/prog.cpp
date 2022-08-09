#include <iostream>
#include <math.h>
using namespace std;

int getSumOfDigits(int n)
{
    if (n < 10)
    {
        return n;
    }

    // this recursively adds the last digit (n%10) to the remaining digits (n//10)
    // Summing up starts from left to right.
    return getSumOfDigits(int(n / 10)) + n % 10;
}

int main()
{
    return 0;
}
