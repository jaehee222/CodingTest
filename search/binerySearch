def binerySearch(array, start, end, target):
    if start > end:
        return None
    # 가운데
    mid = (start + end) // 2
    # 원하는 데이터 찾았음
    if array[mid] == target:
        return mid
    # 타겟은 mid 보다 왼쪽에 있음
    elif array[mid] > target:
        return binerySearch(array, start, mid - 1, target)
    # 타겟은 mid 보다 오른쪽에 있음
    else:
        return binerySearch(array, mid + 1, end, target)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binerySearch(array, 0, n - 1, target)
if result == None:
    print("찾으려는 원소가")
else:
    print(result+1)
