#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

vector<int> g1;
int convertToBinary(int number)
{
    if (number == 0)
    {
        return 0;
    }

    int remainder = int(number % 2);
    int quotient = int(number / 2);
    g1.push_back(remainder);
    cout << remainder << endl;

    return convertToBinary(quotient);
}

int main()
{
    convertToBinary(75);
    for (auto ir = g1.rbegin(); ir != g1.rend(); ++ir)
        cout << *ir << " ";
    cout << "\n";
    return 0;
}
