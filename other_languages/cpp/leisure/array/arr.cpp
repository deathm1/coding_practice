#include <iostream>

using namespace std;

int main()
{
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8};
    int size = sizeof(arr) / sizeof(int);

    int x = 2;

    // O(n)

    for (
        int i = 0;
        i < size;
        i++)
    {
        // cout << arr[i] << endl;

        if (arr[i] == x)
        {
            cout << i << endl;
        }
    }

    return 0;
}