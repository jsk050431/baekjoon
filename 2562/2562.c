#include <stdio.h>

int main()
{   
    int max=0, num, loc;
    for (int i=0; i<9; i++)
    {
        scanf("%d", &num);
        if (num > max)
        {
            max = num;
            loc = i+1;
        }
    }
    printf("%d\n%d", max, loc);

    return 0;
}