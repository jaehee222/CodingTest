# 루트노드 찾기
def findRootNode(parent, a):
    if parent[a] != a:
        return findRootNode(parent, parent[a])
    return a

# 유니온집합 합치기
def unionParent(parent, a, b):
    a = findRootNode(parent, a)
    b = findRootNode(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# x: 노드의 갯수, y: 간선의 갯수
x, y = map(int, input().split())
parent = [0] * (x + 1)  # 부모 초기화

# 자기자신은 부모로 초기화
for i in range(1, x + 1):
    parent[i] = i

# 간선 입력받고 유니온 수행하기
for i in range(y):
    a, b = map(int, input().split())
    unionParent(parent, a, b)

print("각 원소가 속한 집합: ", end='')
for i in range(1, x + 1):
    print(findRootNode(parent, i), end=' ')

print()

print("부모 테이블: ", end='')
for i in range(1, x + 1):
    print(parent[i], end=' ')
