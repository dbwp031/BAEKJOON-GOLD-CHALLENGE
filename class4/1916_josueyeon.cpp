#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<pair<int, int>> graph[1001];
int dist[1001];

void dijkstra(int start)
{
    priority_queue<pair<int, int>> pq;
    
    // {가중치, 노드}
    pq.push({0, start});
    dist[start] = 0;
    
    while (!pq.empty())
    {
        int w = pq.top().first * -1;
        int now = pq.top().second;
        
        pq.pop();
        
        if (dist[now] < w)
            continue;
        
        for(int i = 0;i < graph[now].size();i++)
        {
            int cost = w + graph[now][i].second;
            
            if (cost < dist[graph[now][i].first])
            {
                dist[graph[now][i].first] = cost;
                pq.push({cost * -1, graph[now][i].first});
            }
        }
    }
}
int main()
{
    // N(node), M(edge)
    int N, M;
    cin>>N>>M;
    
    for(int i = 0;i < M;i++)
    {
        int a, b, c;
        cin>>a>>b>>c;
        
        // {노드, 가중치}
        graph[a].push_back({b, c});
    }
    int start, target;
    cin>>start>>target;
    
    fill_n(dist, N + 1, 1e9);
        
    dijkstra(start);
    
    cout<<dist[target]<<"\n";
    
    return 0;
}

