# 동빈이네 떡집
n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2

    # 떡볶이 떡 자르기
    for i in array:
        if i > mid:
            total += i - mid

    # 자른 자투리 떡볶이 떡 길이 총 합이
    # 손님이 원한 최솟값 보다 큰지 확인
    if total < m:
        end = mid -1 # 떡볶이의 양이 부족할 경우 앞쪽으로 자르기
    else:
        result = mid
        start = mid + 1 #양이 충분하지만 최대한 덜 잘라야하니까 ..!

print(result)
