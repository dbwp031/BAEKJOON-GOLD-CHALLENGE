str = input()
data = [0]*26
for s in str:
    s = s.lower()
    data[ord(s)-ord('a')]+=1

maxV = max(data)
if data.count(maxV)==1:
    answer = chr(data.index(maxV)+ord('a')).capitalize()
    print(answer)
else:
    print('?')