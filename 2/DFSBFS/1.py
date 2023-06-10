# 음료수 얼려먹기
# nxm크기의 얼음틀이 있음
# 구멍이 뚫려있으면 0, 칸막이가 존재하면 1
# 구멍이 뚫려있는경우 서로 연결된 것으로간주
# 생성될 수 있는 아이스크림의 갯수?

# dfs로 풀이.. 모든 노드를 방문할거고. 연결된곳은 다 진입처리 하지만 결과를 +1 안해주면 될듯
def dfs(graph, v):
    graph[v[0]][v[1]] = 1
    # 상 하 좌우 확인
    vectorX = [0, 0, -1, 1]
    vectorY = [1, -1, 0, 0]

    for i in range(4):
        dx = v[0] + vectorX[i]
        dy = v[1] + vectorY[i]
        # 그래프를 넘어간다면 넘어가줌
        if dx < 0 or dx >= n or dy < 0 or dy >= m:
            continue
        if graph[dx][dy] == 0:
            dfs(graph, [dx, dy])

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(graph, [i, j])
            result += 1

print(result)
