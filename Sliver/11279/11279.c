#include <stdio.h>

unsigned heap[100000] = {};
int length = 0;

void swap(unsigned* ptr1, unsigned* ptr2)
{
    unsigned temp = *ptr1;
    *ptr1 = *ptr2;
    *ptr2 = temp;
}

void pop(unsigned num)
{
    if (length == 0)
        printf("0\n");
    else
    {
        printf("%u\n", heap[0]);
        heap[0] = heap[length-1];
        heap[length-1] = 0;
        --length;

        int index = 0;
        int nextIdx;
        while (1)
        {
            if (2*index+1 > length-1)
                break;
            else if (2*index+2 > length-1 || heap[2*index+1] >= heap[2*index+2])
                nextIdx = 2*index+1;
            else
                nextIdx = 2*index+2;

            if (heap[nextIdx] > heap[index])
            {
                swap(heap+nextIdx, heap+index);
                index = nextIdx;
            }
            else break;
        }
    }
}

void push(unsigned num)
{
    int index = length;
    heap[index] = num;
    ++length;
    int nextIdx;
    while (1)
    {
        if (index == 0) break;

        nextIdx = (index-1)/2;
        if (heap[nextIdx] == 0 || heap[index] > heap[nextIdx])
        {
            swap(heap+index, heap+nextIdx);
            index = nextIdx;
        }
        else break;
    }
}

int main()
{
    int repeat;
    scanf("%d", &repeat);
    for (int i=0; i<repeat; ++i)
    {
        unsigned inputNum;
        scanf("%u", &inputNum);

        if (inputNum == 0)
            pop(inputNum);
        else
            push(inputNum);
    }
    return 0;
}