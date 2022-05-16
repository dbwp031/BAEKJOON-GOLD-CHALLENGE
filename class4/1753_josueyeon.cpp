// 1754 최단 경로: 다익스트라

#include <vector>
#include <queue>
#include <stdio.h>
using namespace std;

// 한점에서 다른 모든점까지의 최단경로이므로 다익스트라

vector<pair<int, int>> graph[20001];
int dist[20001];

void Dijkstra(int start)
{
	// 우선순위 큐
    priority_queue<pair<int, int>> q;

    q.push({0, start});
    dist[start] = 0;

    while (!q.empty())
    {
        int w = q.top().first * -1;
        int now = q.top().second;

        q.pop();

        if (dist[now] < w)
            continue;

        for(int i = 0;i < graph[now].size();i++)
        {
            int temp = w + graph[now][i].second;

            if (temp < dist[graph[now][i].first])
            {
                dist[graph[now][i].first] = temp;
                q.push({temp * -1, graph[now][i].first});
            }
        }
    }
}
int main()
{
    //V(node), E(edge), start(시작 노드)
    int V, E, start;
    scanf("%d %d %d", &V, &E, &start);
    
    for(int i = 0;i < E;i++)
    {
        int a, b, c;
        scanf(" %d %d %d", &a, &b, &c);
        
        graph[a].push_back({b, c});
    }
   
    // 처음에는 무한대로 초기화	
    for(int i = 1;i <= V;i++)
        dist[i] = 1e9;
   
    Dijkstra(start);

    for(int i = 1;i <= V;i++)
    {
        if (dist[i] == 1e9)
            printf("INF\n");
            
        else
            printf("%d\n", dist[i]);
    }
    return 0;
}

