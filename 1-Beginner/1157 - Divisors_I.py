# https://www.urionlinejudge.com.br/judge/en/problems/view/1145

n = int(input())

for i in range(1, n+1):
    if n % i == 0:
        print(i)
      