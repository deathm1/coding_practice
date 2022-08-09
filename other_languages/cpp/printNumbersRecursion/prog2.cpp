#include <iostream>

using namespace std;

int printNumbersAscending(int myNumber)
{
    if (myNumber == 0)
    {
        return 0;
    }
    printNumbersAscending(myNumber - 1);
    cout << myNumber << endl;
}

int main()
{
    printNumbersAscending(5);
    return 0;
}