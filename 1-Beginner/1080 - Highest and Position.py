# https://www.urionlinejudge.com.br/judge/en/problems/view/1080

t = 0
l = []
while t < 100:
    a = int (input())
    l.append (a)
    t = t + 1
print (max(l))
print (l.index(max(l)) + 1)
