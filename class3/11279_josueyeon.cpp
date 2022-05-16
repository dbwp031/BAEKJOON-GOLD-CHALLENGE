#include <stdio.h>
#include <vector>
#include <queue>
using namespace std;

int main()
{
    int N;
    priority_queue<int> pq;
    
    scanf("%d", &N);
    
    for(int i = 0;i < N;i++)
    {
        int temp;
        scanf(" %d", &temp);
        
        if (temp == 0)
        {
            if (pq.empty() == true)
                printf("0\n");
            else
            {
                printf("%d\n", pq.top());
                pq.pop();
            }
        }
        else
            pq.push(temp);
    }
    return 0;
}

