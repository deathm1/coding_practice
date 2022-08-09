#include <iostream>
using namespace std;

int printNumber(int myNumber)
{
    if (myNumber <= 0)
    {
        return 0;
    }

    cout << myNumber << endl;
    printNumber(myNumber - 1);
}

int main()
{
    printNumber(5);
    return 0;
}