# 부품찾기
# 부품N개. 각 부품은 정수형태의 고유번호가 있다.
# 손님이 M개의 종류의 부품을 대량으로 구매요청
# M개의 종류 모두 확인해서 견적서를 작성.
# 있으면 yes, 없으면 no를 출력

# 이진탐색을 사용해서 부품 찾기
def binerySearch(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binerySearch(array, target, start, mid - 1)
    else:
        return binerySearch(array, target, mid + 1, end)


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()
b.sort()

for i in b:
    result = binerySearch(a, i, 0, n - 1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
