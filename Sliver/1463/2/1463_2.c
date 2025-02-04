#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define min(a,b) a<b?a:b

int main()
{
    int* arr = (int*)malloc(sizeof(int) * 1000001);
    memset(arr, 0, sizeof(int)*1000001);
    int num;

    scanf("%d", &num);
    for (int i=2; i<=num; ++i)
    {
        arr[i] = arr[i-1]+1;

        if (0 == i%2)
            arr[i] = min(arr[i/2]+1, arr[i]);

        if (0 == i%3)
            arr[i] = min(arr[i/3]+1, arr[i]);
    }
    printf("%d", arr[num]);        

    return 0;
}