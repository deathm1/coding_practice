#include <iostream>
using namespace std;

int decimalToBinary(int myNumber)
{

    if (myNumber == 0)
    {
        return 0;
    }

    int myQuotient = int(myNumber / 2);
    int myRemainder = int(myNumber % 2);

    cout << myQuotient << "-" << myRemainder << endl;

    decimalToBinary(myQuotient);
    cout << myRemainder << endl;

    return 0;
}

int main()
{

    decimalToBinary(4);
    return 0;
}