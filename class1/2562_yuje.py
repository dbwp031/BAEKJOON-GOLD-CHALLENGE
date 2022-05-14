data = []
for _ in range(9):
    data.append(int(input()))
maxV = max(data)
print(maxV)
print(data.index(maxV)+1)