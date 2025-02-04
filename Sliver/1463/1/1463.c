#include <stdio.h>
#include <stdlib.h>

int makeone(int num, int* arr);

int main()
{
    int* arr = (int*)malloc(sizeof(int) * 1000000);
    int num;

    while (1)
    {
        scanf("%d", &num);
        printf("%d\n", makeone(num, arr));
    }

    free(arr);
    return 0;
}

int makeone(int num, int* arr)
{
    if (1 == num) return 0;

    else if (arr[num-1] != 0) return arr[num-1];
    
    else
    {
        int temp;
        int count = 10000000;

        if (0 == num%3)
        {
            temp = makeone(num/3, arr) +1;
            if (temp < count) count = temp;
        }
        if (0 == num%2)
        {
            temp = makeone(num/2, arr) +1;
            if (temp < count) count = temp;
        }

        temp = makeone(num-1, arr) +1;
        if (temp < count) count = temp;

        arr[num-1] = count;
        return count;
    }
}