#include <stdio.h>
#include <cmath>
using namespace std;

int r, c;
int result = 0;
void Z(int x, int y, int size)
{
    
    if (x == r && y == c)
    {
        printf("%d\n", result);
        return;
    }
    
    // 범위 내에 있다면
    else if ((r >= x && r < x + size) && (c >= y && c < y + size))
    {
        // 구역 탐색
        int newSize = size / 2;
        Z(x, y, newSize);
        Z(x, y + newSize, newSize);
        Z(x + newSize, y, newSize);
        Z(x + newSize, y + newSize, newSize);
    }
    
    else
        result += size * size;
}

int main()
{
    int N;
    scanf("%d %d %d", &N, &r, &c);
    
    Z(0, 0, (int)pow(2, N));
    
    return 0;
}

