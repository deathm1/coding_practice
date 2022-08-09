#include <iostream>
#include <math.h>

using namespace std;

int *reverseList(int arr[], int size)
{
    int s = 0;
    int e = size - 1;

    while (s < e)
    {
        int a = arr[s];
        int b = arr[e];

        arr[s] = b;
        arr[e] = a;

        s += 1;
        e -= 1;
    }

    return arr;
}

int main()
{
    int arr[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr) / sizeof(int);

    int *ptr = reverseList(arr, size);

    for (int i = 0; i < size; i++)
    {
        cout << ptr[i];
    }

    return 0;
}