#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<pair<int, int>> graph[801];
int dist[801];

void dijkstra(int start)
{
    priority_queue<pair<int, int>> pq;
    
    // {가중치, 노드}
    pq.push({0, start});
    dist[start] = 0;
    
    while(!pq.empty())
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
    // N(node), E(edge)
    int N, E;
    cin>>N>>E;
    
    for(int i = 0;i < E;i++)
    {
        int a, b, c;
        cin>>a>>b>>c;
        
        // {(a,b)를 잇는 간선 가중치 c}
        graph[a].push_back({b, c});
        graph[b].push_back({a, c});
    }
    
    // 반드시 지나가야 하는 정점 2개
    int temp1, temp2;
    cin>>temp1>>temp2;
    
    // 1->temp1->temp2->N or 1->temp2->temp1->N 두가지 경우 존재
    int result = 0;

      fill_n(dist, N + 2, 1e9);
    // temp1-temp2 거리
    dijkstra(temp1);
    result += dist[temp2];
    if (result >= 1e9)
    {
        cout<<-1<<"\n";
        return 0;
    }
    
    // 1-temp1 temp2-N거리
    int t1 = 0;
    fill_n(dist, N + 2, 1e9);
    dijkstra(1);
    t1 = dist[temp1];
    if (t1 >= 1e9)
    {
        cout<<-1<<"\n";
        return 0;
    }
    fill_n(dist, N + 2, 1e9);
    dijkstra(temp2);
    t1 += dist[N];
    if (t1 >= 1e9)
    {
        cout<<-1<<"\n";
        return 0;
    }
   
    // 1-temp2 temp1-N 거리
    int t2 = 0;
    fill_n(dist, N + 2, 1e9);
    dijkstra(1);
    t2 = dist[temp2];
    if (t2 >= 1e9)
    {
        cout<<-1<<"\n";
        return 0;
    }
    fill_n(dist, N + 2, 1e9);
    dijkstra(temp1);
    t2 += dist[N];
    if (t2 >= 1e9)
    {
        cout<<-1<<"\n";
        return 0;
    }
    
    result += min(t1, t2);
    
    cout<<result<<"\n";

    return 0;
}


