import sys

input = sys.stdin.readline  # input을 더 빠르게 받기 위해
INF = int(1e9)
# n: 노드의 갯수, m, 간선의 갯수
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def smallestValue():
    minValue = INF
    index = 0
    for i in range(1, n + 1):
        if minValue > distance[i] and not visited[i]:
            minValue = distance[i]
            index = i
    return index


def dijestra(start):
    distance[start] = 0
    visited[start] = True
    # 한번에 이어지는 경우
    for i in graph[start]:
        distance[i[0]] = i[1]
    for i in range(1, n - 1):
        now = smallestValue() # 현재 최단 거리가 가장 짧은 노드를 꺼냄
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijestra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
