# 상하좌우
# NxN 크기의 정사각형 공간 위에있음
# 왼쪽위 (1,1) 오른쪽아래 (n,n) - 시작은 항상 (1,1)
# 계획서에는 LRUD 중 하나의 문자가 반복적으로 적혀있다. (L-왼, R- 오, U- 위, D- 아래)
# 계획에 따라 도착할 좌표 출력.

n = int(input())
plan = list(input().split())

x = 1
y = 1
for i in plan:
    tmpX = x
    tmpY = y
    if i == 'L':
        tmpY -= 1
    elif i == 'R':
        tmpY += 1
    elif i == 'U':
        tmpX -= 1
    elif i == 'D':
        tmpX += 1
    if tmpX > 0 and tmpX <= n and tmpY > 0 and tmpY <= n:
        x = tmpX
        y = tmpY

print(x,y)
