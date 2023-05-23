#  동빈이네 전자매장

# 1. 이진탐색
def binerySearch(array, target, start, end):
    if  start > end:
        return None

    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binerySearch(array, target, start, mid - 1)
    else:
        return binerySearch(array, target, mid + 1, end)

# 동빈이
N = int(input())
arrayN = list(map(int, input().split()))

# 손님
M = int(input())
arrayM = list(map(int, input().split()))

# 손님이 찾는 부품을 하나하나 꺼내서 동빈이가 가지고 있는지 비교하기
for i in arrayM:
    result = binerySearch(arrayN, i, 0, N-1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')

# 2. 계수정렬
n = int(input())
array = [0] * 10000001
for i in input().split():
    array[int(i)] = 1

m = int(input())
for i in input().split():
    if array[int(i)] == 1:
        print('yes', end=' ')
    else:
        print('no', end= ' ')

#3. 집합자료형
n = int(input())
# set: 집합자료형이며 단순히 특정원소가 있는지의 여부를 판단할 때 빠르게 확인 가능하다
array = set(map(int, input().split()))
m = int(input())
arrayM = list(map(int, input().split()))

for i in arrayM:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
