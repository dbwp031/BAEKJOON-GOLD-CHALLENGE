#include <iostream>
#include <vector>
#include <stack>
#include <queue>
using namespace std;

vector<pair<int, int>> graph[1001];
// 부모 노드 저장 용도
int route[1001];
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
				// 경로 저장을 위해 배열에 현재 노드를 넣어서 부모노드를 체크함
                route[graph[now][i].first] = now;
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
    fill_n(route, 1001, 0);
    
    dijkstra(start);
    
    cout<<dist[target]<<"\n";
    
    stack<int> st;
    st.push(target);
    
    while(1)
    {
        target = route[target];
        if (target == 0)
            break;
        st.push(target);
    }
    
    cout<<st.size()<<"\n";
    while(!st.empty())
    {
        cout<<st.top()<<" ";
        st.pop();
    }
    
    return 0;
}

