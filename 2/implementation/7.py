# 뱀
# 사과를 먹으면 뱀길이가 늘어남
# 벽 or 자기자신의 몸과 부딪히면 게임이 끝남
# NXN 보드판위에 사과가 놓여져있으며 NXN밖에는 벽이 있다.
# 게임시작 시 뱀은 맨위 맨좌측에 위치하고 뱀의길이는 1
# 뱀은 처음에 오른쪽을 향함
# 뱀의 규칙
# 뱀은 몸길이를 늘려 머리를 다음칸에 위치
# 만약 이동한 칸에 사과가 있다면 그 칸의 사과가 사라지고 꼬리는 움직이지 않음
# 만약 이동한 칸에 사과가 없다면 몸길이를 줄여 꼬리가 위치한 칸을 비워줌 (몸길이는 안변함)
# 게임이 끝나는 초 수?
from collections import deque

n = int(input())
k = int(input())

graph = [[False for i in range(n)] for j in range(n)]  # 그래프
mineGraph = [[False for i in range(n)] for j in range(n)]  # 뱀의 몸체가 차지하는것

for i in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = True

l = int(input())  # 뱀의 방향전환 횟수
vectorBamArray = []
vectorBamIdx = 0
for i in range(l):
    time, vectorBam = input().split()
    vectorBamArray.append((int(time), vectorBam))

vectorX = [0, 1, 0, -1]
vectorY = [1, 0, -1, 0]
nowVector = 0
x = 0
y = 0
result = 0
q = deque()
q.append((0, 0))
while True:
    result += 1
    x += vectorX[nowVector]
    y += vectorY[nowVector]
    if x < 0 or x >= n or y < 0 or y >= n or mineGraph[x][y]:
        break

    if not graph[x][y]:  # 사과가 없을 때
        dx, dy = q.popleft()
        mineGraph[dx][dy] = False  # 꼬리 제거
    mineGraph[x][y] = True
    q.append((x, y))

    # 방향전환
    if vectorBamIdx < len(vectorBamArray) and result == vectorBamArray[vectorBamIdx][0]:
        if vectorBamArray[vectorBamIdx][1] == "L":
            nowVector -= 1
        else:
            nowVector += 1
        nowVector %= 4
        vectorBamIdx += 1

print(result)
