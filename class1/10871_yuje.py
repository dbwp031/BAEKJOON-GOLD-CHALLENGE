n,k = map(int,input().split())
data = list(map(int,input().split()))
for d in data:
    if d<k:
        print(d,end=' ')