#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void add(int x, int* set);
void remove0(int x, int* set);
int check(int x, int* set);
void toggle (int x, int* set);
void all(int* set);
void empty(int* set);
void test_print(int* set);

int main()
{
    int m = 0;
    scanf("%d", &m);
    getchar();

    int set[30] = {};
    
    for (int i=0; i<m; ++i)
    {
        char input[20];
        int x = 0;
        scanf("%[^\n]s", input);
        getchar();
    
        char* ptr = input;
        while (*ptr != '\0')
        {
            if (*ptr == ' ')
            {
                *ptr = '\0';
                x = atoi(ptr+1);
            }
            ++ptr;
        }
        
        if (strcmp(input, "add") == 0) add(x, set);
        else if (strcmp(input, "remove") == 0) remove0(x, set);
        else if (strcmp(input, "check") == 0) printf("%d\n", check(x, set));
        else if (strcmp(input, "toggle") == 0) toggle(x, set);
        else if (strcmp(input, "all") == 0) all(set);
        else if (strcmp(input, "empty") == 0) empty(set);

        // test_print(set);
    }

    return 0;
}

void add(int x, int* set)
{
    int i = 0;
    if (check(x, set) == 0)
    {
        while (set[i] != 0) ++i;
        set[i] = x;
    }
}

void remove0(int x, int* set)
{
    int i = 0;
    if (check(x, set) == 1)
    {
        while (set[i] != x) ++i;
        set[i] = 0;

        while (set[i+1] != 0)
        {
            set[i] = set[i+1];
            ++i;
        }
        set[i] = 0;
    }
}

int check(int x, int* set)
{
    int i = 0;
    while (set[i] != 0)
    {
        if (set[i] == x) return 1;
        ++i;
    }
    return 0;
}

void toggle (int x, int* set)
{
    int is_x_inSet = check(x, set);
    if (is_x_inSet == 0) add(x, set);
    else if (is_x_inSet == 1) remove0(x, set);
}

void all(int* set)
{
    int i = 0;
    empty(set);
    for (int num=0; num<20; ++num) set[num] = num+1;
}

void empty(int* set)
{
    int i = 0;
    while(set[i] != 0)
    {
        set[i] = 0;
        ++i;
    }
}

void test_print(int* set)
{
    printf("//");

    int i = 0;
    while (set[i] != 0)
    {
        printf("%d ", set[i]);
        ++i;
    }
    printf("\n");
}
