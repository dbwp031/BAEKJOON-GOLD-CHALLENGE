// 11724 연결 요소의 개수: DFS

#include <vector>
#include <iostream>
using namespace std;

vector<int> graph[1001];
vector<bool> visited(1001, false);

void DFS(int node)
{
    visited[node] = true;

    for(int i = 0;i < graph[node].size();i++)
    {
        if (visited[graph[node][i]] == false)
            DFS(graph[node][i]);
    }
}
int main()
{
    // N(node), M(edge)
    int N, M;
    cin>>N>>M;

	// 간선 정보 입력 받기(방향 없으니까 양방향으로)
    for(int i = 0;i < M;i++)
    {
        int a, b;
        cin>>a>>b;

        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    int result = 0;
    for(int i = 1;i <= N;i++)
    {
		// 방문하지 않은 노드라면 연결정보 ++ 해주고 DFS
        if (visited[i] == false)
        {
            result++;
            DFS(i);
        }
    }

    cout<<result<<endl;

    return 0;
}
