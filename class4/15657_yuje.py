import itertools
n,m = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
for per in itertools.combinations_with_replacement(data,m):
    for x in per:
        print(x,end=' ')
    print()

