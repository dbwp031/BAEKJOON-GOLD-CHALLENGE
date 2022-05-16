#include <iostream>
#include <vector>
using namespace std;


int M, N;
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};

void DFS(vector<vector<int>> &v, vector<vector<bool>> &visited, int i, int j)
{
    if (visited[i][j] == true || v[i][j] == 0)
        return;
    
    visited[i][j] = true;
  
    for(int idx = 0;idx < 4;idx++)
    {
        int tempR = i + dx[idx];
        int tempC = j + dy[idx];
        
        if (tempR < 0 || tempC < 0 || tempR >= N || tempC >= M)
            continue;
        
        else if (v[tempR][tempC] == 1 && visited[tempR][tempC] == false)
            DFS(v, visited, tempR, tempC);
    }
}

int main(void)
{
    int T;
    cin>>T;
    // M(가로), N(세로), K(배추 개수)
    int K;
    int resultarr[T];
    
    for(int iter = 0;iter < T;iter++)
    {
        cin>>N>>M>>K;
        int result = 0;
        
        vector<vector<int>> v(N, vector<int>(M, 0));
        vector<vector<bool>> visited(N, vector<bool>(M, false));
        
        for(int i = 0;i < K;i++)
        {
            int r = 0, c = 0;
            cin>>r>>c;
            v[r][c] = 1;
        }
        
        for(int i = 0;i < N;i++)
        {
            for(int j = 0;j < M;j++)
            {
                if (v[i][j] == 1 && visited[i][j] == false)
                    result++;
                    DFS(v, visited, i, j);
            }
        }
        resultarr[iter] = result;
    }
    for(int i = 0; i < T;i++)
        cout<<resultarr[i]<<endl;
}


