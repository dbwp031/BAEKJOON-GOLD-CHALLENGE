// 1003 피보나치 함수: dynamic programming

#include <vector>
#include <stdio.h> // 시간 제한 위해 printf, scanf 사용함
using namespace std;

// dynamic programming으로 바로 횟수 구할 수 있도록
int main()
{
    int T;
    scanf("%d", &T);
    
    while (T-- > 0)
    {
        int N;
        scanf(" %d", &N);
        
        // {0이 출력되는 횟수, 1이 출력되는 횟수}
        vector<pair<int, int>> v(41, {-1, -1});
        
		// 초기화
        v[0].first = 1;
        v[0].second = 0;
        
        v[1].first = 0;
        v[1].second = 1;
        
        for(int i = 2;i <= N;i++)
        {
            // dynamic programming - 메모이제이션 사용
            v[i].first = v[i - 1].first + v[i - 2].first;
            v[i].second = v[i - 1].second + v[i - 2].second;
        }
        printf("%d %d\n", v[N].first, v[N].second);
    }
    return 0;
}

