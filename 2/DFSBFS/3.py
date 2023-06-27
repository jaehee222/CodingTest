# 특정 거리의 도시 찾기
# 1~N번까지의 도시와 M개의 단방향 도로가 존재
# 거리는 모두 1
# X로부터 출발하여 도달 할 수 있는 모든 도시중에서 최단거리가 K 인 도시의 번호를 출력

# 최단거리문제 -> BFS
from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for i in range(n+1)]
visited = [0] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque()
q.append(x)
while q:
    x = q.popleft()
    for i in graph[x]:
        if visited[i] == 0:
            visited[i] += visited[x] + 1
            q.append(i)

count = 0
for i in range(len(visited)):
    if visited[i] == k:
        print(i)
        count += 1

if count == 0:
    print(-1)
