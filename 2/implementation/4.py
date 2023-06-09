# 게임 개발
# NxM 직사각형에 게임캐릭터가 있다.
# 각각의 칸은 바다 or 육지
# 동서남북중 하나를 이동. 바다로는 못감
# 각맵은 (A, B)로 표현 A: 북쪽으로부터 떨어진 칸의 갯수, B: 서쪽으로부터 떨어진 칸의 갯수
# 캐릭터의 이동 메뉴얼
# 1. 현재위치에서 현재방향을 기준으로 왼쪽방향부터 갈 곳을 정함
# 2. 왼쪽에 가보지 않은 칸이 존재한다면 왼쪽으로 회전 후 왼쪽으로 전진. 왼쪽에 가보지 않은 칸이 없다면 회전만함
# 3. 네 방향 모두 가본칸이거나 바다라면 바라보는 방향을 유지한채로 한칸 뒤로 가고 1단계로 돌아감.
# 4. 뒤쪽방향이 바다인 칸이라 뒤로 못가는경우 움직임을 멈춤
# 캐릭터가 방문한 칸의 수?
# 0: 북, 1: 동, 2: 남, 3: 서
# 0: 육지, 1: 바다
n, m = map(int, input().split())
a, b, d = map(int, input().split())

# 방향벡터 (북동남서..)
vectorX = [-1, 0, 1, 0]
vectorY = [0, 1, 0, -1]

array = [[]] # 지도는 1,1이 원점이라.. 맨처음은 공백 배열로 ..
for i in range(n):  # 세로크기
    array.append(list(map(int, input().split())))

result = 0
count = 0
# 현재위치도 방문처리
array[a][b] = 1

while True:
    # 왼쪽보기..
    d -= 1
    if d == -1:
        d = 3
    # 왼쪽에 가보지 않은칸 존재하는지 확인
    dx = a + vectorX[d]
    dy = b + vectorY[d]
    # 가보지 않았다면.. 전진!
    if array[dx][dy] != 1:
        array[dx][dy] = 1
        result += 1
        a = dx
        b = dy
    else:
        count += 1
        # 네방향 다 가봤거나 바다라면 한칸 뒤로 이동
        if count == 4:
            a = a - vectorX[d]
            b = b - vectorY[d]
            if array[a][b] == 1:
                break
        continue

print(result)
