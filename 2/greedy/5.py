# 모험가 길드
# 모험가 N명에게 공포도를 측정했다.
# 공포도가 x인 모험가는 반드시 x명이상으로 구성된 모험가 그룹에 참여해야한다.
# 몇개의 모험가 그룹을 만들 수 있을까(최대)

# 정렬한다음에 작은애들부터 구성하면 제일 많이 만들 수 있지 않을까
n = int(input())
array = list(map(int, input().split()))

array.sort()

count = 0 # 공포도 포함된 사람 수
group = 0 # 그룹수

for i in array:
    count += 1
    if count >= i:
        group += 1
        count = 0

print(group)
