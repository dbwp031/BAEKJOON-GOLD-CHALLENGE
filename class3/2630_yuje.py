data = []
n = int(input())
for _ in range(n):
    data.append(list(map(int,input().split())))

blue = 0
white = 0

def paper(pp):
    global blue,white
    a = 0
    n = len(pp)
    for p in pp:
        a += sum(p)
    
    if a == 0:
        white +=1
        return
    elif a == n**2:
        blue +=1
        return
    p1 = [row[0:n//2] for row in pp[:n//2]]
    p2 = [row[0:n//2] for row in pp[n//2:]]
    p3 = [row[n//2:] for row in pp[:n//2]]
    p4 = [row[n//2:] for row in pp[n//2:]]
    paper(p1)
    paper(p2)
    paper(p3)
    paper(p4)
paper(data)
print(white)
print(blue)