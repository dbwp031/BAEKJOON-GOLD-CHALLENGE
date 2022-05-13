data = list(map(int,input().split()))
a = True
d = True

for i in range(len(data)-1):
    if data[i] < data[i+1]:
        d = False
    else:
        a = False
if a:
    print('ascending')
elif d:
    print('descending')
else:
    print('mixed')