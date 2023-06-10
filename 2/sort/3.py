# 두 배열의 원소교체
# 두 배열은 N개의 원소이며 자연수.
# 동빈이는 최대 K번을 바꿔치기 연산 수행가능
# 최종목표 : A 배열의 모든 원소의 합이 최대가 되어야한다.

# A를 작은순으로 정렬, B를 큰순으로 정렬해서 서로 바꿔치기 (만약에 A가 더 크면 바꿔치기 X)
n, k = map(int, input().split())
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))
arrayA.sort()
arrayB = sorted(arrayB, reverse=True)

for i in range(k):
    if arrayA[i] < arrayB[i]:
        arrayA[i],arrayB[i] = arrayB[i],arrayA[i]
    else:
        break

result = 0
for i in arrayA:
    result += i

print(result)
