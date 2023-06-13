# 전보
# N개의 도시가 있으며 각 도시에 보내고자하는 메시지 있는 경우 다른곳으로 메시지 보낼 수 있다.
# X -> Y 전보 보내려면 통로가 있어야함 (단방향)
# C에 위급상황이 발생해 최대한 많은 도시로 메시지를 보내고자 한다.
# 각 도시의 번호와 통로가 설치되어있는 정보 주어졌을 때 도시C에서 보낸 메시지를 받게되는 도시의 개수와 걸리는 시간을 계산

# 다익스트라 사용. 보낸 메시지를 받는다는건 거리가 무한이 아님 & 무한이 아닌 거리들의 최댓값을 구하면 될거같다.
import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline
n, m, c = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)

count = 0
max_clock = 0
for i in distance:
    if i != INF:
        count += 1
        max_clock = max(i, max_clock)

print(count - 1, max_clock)
