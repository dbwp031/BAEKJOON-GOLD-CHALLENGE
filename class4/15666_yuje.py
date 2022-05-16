import itertools
n,m = map(int,input().split())
data = list(map(int,input().split()))

# data = set(data) # n
# data = list(data) # n
# data.sort() # nlogn
data.sort() # nlogn
set_data = []
now = -1

for d in data:
    if d == now:
        continue
    else:
        set_data.append(d)
        now = d
        
for per in itertools.combinations_with_replacement(set_data,m):
    for x in per:
        print(x,end=' ')
    print()

