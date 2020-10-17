const int MAX = 50;

#include <stdio.h>
/// returns length of the char array
int length(char input[])
{
    int index = 0;
    while (input[index] != '\0')
    {
        index++;
    }
    return index;
}

int min(int a, int b)
{
    if (a > b)
    {
        return b;
    }
    else
    {
        return a; // equal or lesser
    }
}

int max(int a, int b)
{
    if (a > b)
    {
        return a;
    }
    else
    {
        return b; // equal or greater
    }
}

int main(void)
{
    char str1[50];
    char str2[50];

    printf("\n Enter source String  :  ");
    scanf("%s", str1);
    printf("\n Enter target String  :  ");
    scanf("%s", str2);
    int count = 0;
    int m = length(str1);
    int n = length(str2);
    char arr[m][n];
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (min(i, j) == 0)
            {
                // printf("min=0 i=%d j=%d",i,j);
                arr[i][j] = max(i, j);
            }
            else
            {
                int a = arr[i - 1][j] + 1;
                int b = arr[i][j - 1] + 1;
                int c;
                if (str1[i] == str2[j])
                {
                    c = arr[i - 1][j - 1];
                }
                else
                {
                    c = arr[i - 1][j - 1] + 1;
                }
                int minABC = min(min(a, b), c);
                // printf("min %d,%d,%d=%d",a,b,c,minABC);
                arr[i][j] = minABC;
            }
        }
    }
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%d", arr[i][j]);
        }
        printf("\n");
    }
    printf("len=%d", arr[m - 1][n - 1]);
    return 0;
}

/***output****
 Enter source String  :  sitting

 Enter target String  :  bitting      
0123456
1012345
2101234
3210123
4321012
5432101
6543210
len=0
 * /