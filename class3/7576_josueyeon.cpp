#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

int m, n;
int graph[1001][1001];
vector<pair<int, int>> tomato;

int BFS()
{
    int result = -1;
    
    // {{좌표 x, 좌표 y}, 시간}
    queue<pair<pair<int, int>, int>> pq;
    
    // 토마토가 익어있는 곳을 출발지점으로 설정
    for(auto iter : tomato)
        pq.push({{iter.first, iter.second}, 0});
    
    int prev = -1;
    while(!pq.empty())
    {
        int x = pq.front().first.first;
        int y = pq.front().first.second;
        
        int time = pq.front().second;
        
        if (prev != time)
        {
            prev = time;
            result++;
        }
        
        pq.pop();
        
        for(int dir = 0;dir < 4;dir++)
        {
            int tempX = x + dx[dir];
            int tempY = y + dy[dir];
            
            if (tempX < 0 || tempY < 0 || tempX >= n || tempY >= m)
                continue;
            
            if (graph[tempX][tempY] == 0)
            {
                graph[tempX][tempY] = 1;
                pq.push({{tempX, tempY}, time + 1});
            }
        }
    }
    return result;
}

int main()
{
    // m(가로), n(세로)
    cin>>m>>n;
    
    for(int i = 0;i < n;i++)
    {
        for(int j = 0;j < m;j++)
        {
            cin>>graph[i][j];
            
            if (graph[i][j] == 1)
                tomato.push_back({i, j});
        }
    }
    int result = BFS();
    
    for(int i = 0;i < n;i++)
    {
        for(int j = 0;j < m;j++)
        {
            // 토마토가 익지 못하는 경우
            if (graph[i][j] == 0)
            {
                cout<<-1<<endl;
                return 0;
            }
        }
    }
    cout<<result<<endl;
    
    return 0;
}
