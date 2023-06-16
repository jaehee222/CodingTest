# 볼링공 고르기
# A, B가 서로 다른 무게의 볼링공을 고르려고함 (볼링공은 총 N개)
# 볼링공은 1번부터 순서대로 번호가 부여됨
# 볼링공의 무게는 1~M의 자연수로 존재.
# 두사람이 볼링공을 고르는 경우의 수

# 순서대로 정렬함.
n, m = map(int, input().split())
k = list(map(int, input().split()))
k.sort()

result = 0
for i in range(n):
    for j in range(i+1, n):
        # 겹치지 않았을 경우에 +1
        if k[i] != k[j]:
            result += 1

print(result)
