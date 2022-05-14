hours = list(range(0,24))
mins = list(range(0,60))
h,m=map(int,input().split())
if m - 45<0:
    h = (h-1)%24
m = (m-45)%60
print(hours[h],mins[m])