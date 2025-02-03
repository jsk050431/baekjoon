#include <stdio.h>
#include <time.h>

void fibonacci(int index, /* int *numptr, */ int *zeroPtr, int *onePtr);

int main()
{
    int number;
    long startTime;
    long endTime;

    int repeat;
    scanf("%d", &repeat);
    for (int i=0; i<repeat; ++i)
    {
        // int numArr[50] = {};
        int zeroArr[50] = {};
        int oneArr[50] = {};

        scanf("%d", &number);
        startTime = clock();

        fibonacci(number, /* numArr, */ zeroArr, oneArr);
        printf("%d %d\n", zeroArr[0], oneArr[0]);

        endTime = clock();
        int totalTime = endTime - startTime;
        printf("%ldms\n\n", totalTime);
    }

    return 0;
}

void fibonacci(int index, /* int *numPtr, */ int *zeroPtr, int *onePtr)
{
    if (index == 0)
    {
        // *numPtr = 0;
        *zeroPtr = 1;
        *onePtr = 0;
    }
    else if(index == 1)
    {
        // *numPtr = 1;
        *zeroPtr = 0;
        *onePtr = 1;
        fibonacci(0, /* numPtr+1, */ zeroPtr+1, onePtr+1);
    }
    else
    {   
        if (*(onePtr+2) == 0)
            fibonacci(index-2, /* numPtr+2, */ zeroPtr+2, onePtr+2);
        if (*(onePtr+1) == 0)
            fibonacci(index-1, /* numPtr+1, */ zeroPtr+1, onePtr+1);

        // *numPtr = *(numPtr+2) + *(numPtr+1);
        *zeroPtr = *(zeroPtr+2) + *(zeroPtr+1);
        *onePtr = *(onePtr+2) + *(onePtr+1);
    }
}