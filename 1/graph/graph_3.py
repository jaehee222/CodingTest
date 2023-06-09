from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

# 간선정보 입력받기
for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1 # b 진입차수 1증가

def topologySort():
    result = [] # 결과를 저장하기 위한 변수
    q = deque()

    # 진입차수가 0인 것은 전부 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌때까지 반복
    while q:
        now = q.popleft()
        result.append(now) # 큐꺼낸건 결과에 저장

        for i in graph[now]:
            indegree[i] -= 1 # now는 이미 꺼냈으니까 그에 해당되는 진입차수 빼기
            if indegree[i] == 0:
                q.append(i) # 빼준 진입차수가 0인것은 다시 큐에 삽입

    for i in result:
        print(i, end= ' ')

topologySort()
