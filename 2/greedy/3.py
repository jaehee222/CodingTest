# 숫자카드 게임
# NxM의 형태로 놓여있음. N: 행, M: 열
# 뽑고자 하는 행 선택 -> 그 카드들중 가장 숫자가 낮은 카드 선택
# 가장 낮은 카드를 선택할거기때문에 처음에 행을 선택할때 최대한 가장 큰 숫자이게끔 전략세우기

n, m = map(int, input().split())

array = []
# 각 열의 가장 작은 수
minNumber = 0
# 각 열의 가장 작은 수 중 가장 큰 수
maxNumber = 0
for i in range(n):
    array = list(map(int, input().split()))
    minNumber = min(array)
    if maxNumber < minNumber:
        maxNumber = minNumber

print(maxNumber)
