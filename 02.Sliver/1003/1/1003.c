#include <stdio.h>
#include <time.h>

int fibonacci(int n);

int zero = 0;
int one = 0;

int main()
{
    int number;   

    int repeat = 0;
    scanf("%d", &repeat);
    for (int i=0; i<repeat; ++i)
    {
        scanf("%d", &number);

        int time = clock();
        fibonacci(number);
        printf("%d %d\n", zero, one);

        time = clock()-time;
        printf("%dms\n\n", time);
        zero = 0;
        one = 0;
    }

    return 0;
}

int fibonacci(int n)
{
    if (n == 0)
    {
        ++zero;
        return 0;
    }
    else if (n == 1)
    {
        ++one;
        return 1;
    }
    else return fibonacci(n-1) + fibonacci(n-2);
}