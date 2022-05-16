#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int N;
    int result = 0;
    int ans = 0;
    
    scanf("%d", &N);
    
    vector<int> v;
    for(int i = 0;i < N;i++)
    {
        int temp;
        scanf(" %d", &temp);
        
        v.push_back(temp);
    }
    
    sort(v.begin(), v.end());
    
    for(int i = 0;i < v.size();i++)
    {
        result = result + v[i];
        ans += result;
    }
    
    printf("%d\n", ans);
    
    return 0;
}

