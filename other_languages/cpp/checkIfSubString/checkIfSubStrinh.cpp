#include <iostream>
#include <math.h>

using namespace std;

bool checkIfSubString(string a, string b)
{
    string larger = "";
    string smaller = "";
    if (a.size() > b.size())
    {
        larger = a;
        smaller = b;
    }
    else
    {
        larger = b;
        smaller = a;
    }
    int s_ctr = 0;
    for (int i = 0; i < larger.size(); i++)
    {
        if (s_ctr == smaller.size())
        {
            break;
        }
        if (larger[i] == smaller[s_ctr])
        {
            s_ctr += 1;
        }
        else
        {
            s_ctr = 0;
        }
    }
    return s_ctr == smaller.size() ? true : false;
}

int main()
{
    cout << checkIfSubString("asdasdas", "sd") << endl;
    return 0;
}