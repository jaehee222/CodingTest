# 떡볶이 떡만들기
# 일정하지 않은 떡길이를 똑같이 한번에 절단하고 남은 자투리를 손님이 가져간다(?!)
# 손님이 왔을 때 요청한 총길이는 M이고 적어도 M만큼 가져가게 절단기 설정하는 최댓값?
n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

maxResullt = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in array:
        if i > mid:
            total += i - mid
    if total >= m:
        maxResullt = mid
        start = mid + 1
    else:
        end = mid - 1

print(maxResullt)
