#include <stdio.h>

void fibonacci(int index, int *zeroPtr, int *onePtr);

int main()
{
    int number;

    int repeat;
    scanf("%d", &repeat);
    for (int i=0; i<repeat; ++i)
    {
        int zeroArr[50] = {};
        int oneArr[50] = {};

        scanf("%d", &number);

        fibonacci(number, zeroArr, oneArr);
        printf("%d %d\n", zeroArr[0], oneArr[0]);
    }

    return 0;
}

void fibonacci(int index, int *zeroPtr, int *onePtr)
{
    if (index == 0)
    {
        *zeroPtr = 1;
        *onePtr = 0;
    }
    else if(index == 1)
    {
        *zeroPtr = 0;
        *onePtr = 1;
        fibonacci(0, zeroPtr+1, onePtr+1);
    }
    else
    {   
        if (*(onePtr+2) == 0)
            fibonacci(index-2, zeroPtr+2, onePtr+2);
        if (*(onePtr+1) == 0)
            fibonacci(index-1, zeroPtr+1, onePtr+1);

        *zeroPtr = *(zeroPtr+2) + *(zeroPtr+1);
        *onePtr = *(onePtr+2) + *(onePtr+1);
    }
}