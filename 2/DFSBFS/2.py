# 미로탈출
# 동빈이는 nxm크기의 직사각형 형태의 미로에 갇혀있다.
# 동빈이는 (1,1) 에 위치 되어있다.
# 그래프는 괴물이 있으면 0, 없으면 1
# 동빈이가 탈출하기 한 최소의 갯수?
from collections import deque


def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    # 상하좌우
    vectorX = [0, 0, -1, 1]
    vectorY = [-1, 1, 0, 0]
    while queue:
        dx, dy = queue.popleft()
        for i in range(4):
            tmpX = dx + vectorX[i]
            tmpY = dy + vectorY[i]
            # 그래프 넘어가면 넘어감
            if tmpX < 0 or tmpX >= n or tmpY < 0 or tmpY >= m:
                continue
            if graph[tmpX][tmpY] == 1:
                # 갈 수있는 곳이면 이전이동횟수에 +1 해줌
                graph[tmpX][tmpY] = graph[dx][dy] + 1
                queue.append((tmpX, tmpY))


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 그래프는 0,0 부터 시작하니까 1,1 은 0,0
bfs(graph, 0, 0)

print(graph[n - 1][m - 1])
