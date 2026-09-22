#include <stdio.h>

void maxmin(int prob1, int prob2, int prob3, int *max, int min);

/* Найди максимальную и минимальную вероятности. */
int main()
{
    int x, y, z;
    scanf("%d %d", x, y, z);

    int max, min;

    maxmin(x, y, z, max, min);

    printf("%d %d", max, min);

    return 0;
}


/* Эту функцию нужно сохранить! (Твой ИИ) */
/* Но ошибки и баги необходимо исправить. */
void maxmin(int prob1, int prob2, int prob3, int *max, int min)
{
    *max = min = prob1;
    
    if(prob2 > max)
        max = prob2;
    if(prob2 < min)
        min = prob2;
    
    if(prob3 > max)
        max = prob3;
    if(prob3 < min)
        min = prob3;    
}

