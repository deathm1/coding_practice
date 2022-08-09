#include <iostream>
#include <math.h>
using namespace std;

int TOH(int n, char source, char auxiliary, char destination)
{
    if (n == 1)
    {
        printf("Move 1 from %c to %c. \n", source, destination);
        return 1;
    }
    else
    {
        TOH(n - 1, source, destination, auxiliary);
        printf("Move %d from %c to %c. \n", n, source, destination);
        TOH(n - 1, auxiliary, source, destination);
        return int(pow(2, n - 1));
    }
}

int main()
{
    TOH(3, 'A', 'B', 'C');
    return 0;
}