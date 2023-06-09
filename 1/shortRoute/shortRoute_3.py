INF = int(1e9)

n = int(input())
m = int(input())
# 2차원
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기자신 -> 자기자신은 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            # 기존에 저장된 a에서 b로 가는 방법이랑 k를 거쳐서 a에서 b로 가는거중에 최소값을 저장함,
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print("INFINITY", end = ' ')
        else:
            print(graph[a][b], end = ' ')
    print()
