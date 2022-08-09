#include <iostream>
#include <math.h>
using namespace std;

int TOH(int numberOfDisks, char source, char auxiliary, char destination)
{
    if (numberOfDisks == 1)
    {
        printf("Move 1 from %c to %c\n", source, destination);
        return 1;
    }
    else
    {
        TOH(numberOfDisks - 1, source, destination, auxiliary);
        printf("Move %d from %c to %c\n", numberOfDisks, source, destination);
        TOH(numberOfDisks - 1, auxiliary, source, destination);
        return pow(2, numberOfDisks) - 1;
    }
}

int main()
{
    cout << TOH(3, 'A', 'B', 'C') << endl;
    return 0;
}