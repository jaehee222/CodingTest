# 효율적인 화폐 구성
# n가지 종류의 화폐를 최소한으로 해서 가치의 합이 M원이 되도록 한다.
# M원을 만들기 위한 최소한의 화폐 수

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0

for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:  # array[i] 동전을 넣을 수 있는 경우
            d[j] = min(d[j], d[j-array[i]] + 1) # 기존방법 vs 현재방법

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
