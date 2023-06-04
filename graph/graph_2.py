# 루트노드를 찾아주는 함수
def findParent(parent, x):
    # 루트노드가 아니라면 재귀적으로 함수 호출하여 찾아주기
    if parent[x] != x:
        return findParent(parent, parent[x])
    return parent[x]

# 유니온 함수
def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# x: 노드, y: 간선
x, y = map(int, input().split())
parent = [0] * (x + 1)

edges = []
result = 0

# 모든 요소를 루트노드로 초기화
for i in range(1, x + 1):
    parent[i] = i

for i in range(y):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 금액순으로 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클이 있는건 제외시킴..
    if findParent(parent, a) != findParent(parent, b):
        unionParent(parent, a, b)
        result += cost

print(result)
