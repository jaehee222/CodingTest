# 개미전사
# 개정해진 수의 식량을 저장하고 있으며 선택적으로 약탈해서 뺏음
# 인접한 식량창고가 공격받으면 바로 알아차려 한칸이상 떨어진 식량창고를 약탈해야한다.
# n: 식량창고 개수, 저장된 식량개수 K

n = int(input())
array = list(map(int, input().split()))
d = [0] * 100
d[0] = array[0]
d[1] = max(array[0], array[1])
# 앞에 식량을 턴 경우, 앞에 식량을 털지 않은경우로 나눠서 생각..
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[n - 1])

print(d[n-1])
