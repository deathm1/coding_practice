#include <iostream>
#include <stdio.h>
#include <math.h>
#include <vector>

using namespace std;

bool checkIfPalindrome(string txt)
{

    int low = 0;
    int high = txt.size() - 1;

    while (low < high)
    {
        if (txt[low] != txt[high])
        {
            return false;
        }
        low += 1;
        high -= 1;
    }

    return true;
}

int main()
{
    cout << checkIfPalindrome("ABCBA") << endl;
    return 0;
}