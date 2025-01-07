#include <stdio.h>

int main()
{
    int a, b, c;
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);

    printf("%d\n", a+b-c);

    if (b/1000!=0) a *= 10000;
    else if (b/100!=0) a*=1000;
    else if (b/10!=0) a*=100;
    else a*=10;
    printf("%d", a+b-c);
    
    return 0;
}