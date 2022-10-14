#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i, num, v[10];
    printf("Entre com um numero: ");
    scanf("%d", &num);
    for(i=0; i<100; i++)
    {
        num++;
        if(num % 5 == 0)
        {
            v[i] = num;
            printf("%d\n", v[i]);
        }
    }
    return 0;
}
