# 맵 생성 x[0] 세로, x[1] 가로
X = list(map(int, input().split()));

# 캐릭터 위치 (man[0], man[1]) man[2] : 보고 있는 쪽 0: 북, 1: 동, 2: 남, 3: 서
man = list(map(int, input().split()))
directionX = [1, 0, -1, 0]
directionY = [0, 1, 0, -1]

gameMap = [[0] * X[0] for i in range(X[1])]
visitedMap = [];
# 게임 맵 받기
for i in range(X[0]):
    gameMap[i] = list(map(int, input().split()));

tmpX = man[0]
tmpY = man[1]

# 밟은 땅의 횟수 (현재 땅도 포함!)
count = 1
donMove = 0
while True:
    donMove += 1
    # 4번동안 이동을 못한것 -> 이동 불가!
    if donMove == 5: break

    # 현재방향에서 왼쪽 바라보기
    man[2] += 1
    # 서쪽에서 왼쪽 바라보는거면 다시 북쪽..
    if (man[2] == 4): man[2] = 0

    # 왼쪽으로 이동..
    tmpX += directionX[man[2]]
    tmpY += directionY[man[2]]

    # 맵을 벗어났을 때
    if (tmpX > X[1] or tmpX < 0 or tmpY > X[1] or tmpY < 0): continue
    # 막혀있을 때
    if (gameMap[tmpX][tmpY] == 1): continue
    # 이미 가본 곳일 때
    isVisit = False
    for j in visitedMap:
        if (j[0] == tmpX and j[1] == tmpY):
            isVisit = True
            break
    if (isVisit): continue

    man[0] = tmpX
    man[1] = tmpY
    count += 1
    donMove = 0
    visitedMap.append([tmpX, tmpY])

print(count)
