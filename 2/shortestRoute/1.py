# 미래도시
# 방문판매원 A씨, 1~N의 회사중 X회사로 방판 예정
# 방판 전에 소개팅해야해서 K번회사를 먼저 들릴거임
# 최소시간?
# 어딜들리는거니까 플로이드 워셜..

INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for i in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
           graph[a][b] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for a in range(1, n+1):
    for b in range(1, n+1):
        for c in range(1, n+1):
            graph[b][c] = min(graph[b][c], graph[b][a] + graph[a][c])

result = graph[1][k] + graph[k][x]

if result >= INF:
    print(-1)
else:
    print(result)
