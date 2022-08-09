#include <iostream>
#include <math.h>

using namespace std;

bool checkIfAnagram(string s1, string s2)
{
    if (s1.size() != s2.size())
    {
        return false;
    }

    int arr[256] = {0};
    int size = sizeof(arr) / sizeof(int);

    for (int i = 0; i < s1.size(); i++)
    {
        arr[int(s1[i])] += 1;
        arr[int(s2[i])] -= 1;
    }

    for (int i = 0; i < size; i++)
    {

        if (arr[i] != 0)
        {
            return false;
        }
    }

    return true;
}

int main()
{
    cout << checkIfAnagram("abcd", "dcba") << endl;
    return 0;
}