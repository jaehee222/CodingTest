# 도시분할계획
# 마을 N개 연결하는 길 M개가 있고 양방향이다. 유지비도 있음
# 이장은 마을을 2개로 분할할 계획을 세운다.
# 분리된 마을은 집들이 서로 연결되도록 분할한다.
# 최소유지비를 가지기 위한 프로그램

# 크루스칼알고리즘을 사용해서 전체를 연결하고 2개로 분리되므로 가장 비싼 길 하나를 없앤다.
def findParent(parent, x):
    if parent[x] != x:
        return findParent(parent, parent[x])
    return parent[x]


def uinonParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(n):
    parent[i] = i

totalCost = 0
edges = []
for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
last = 0
for edge in edges:
    cost, a, b = edge
    if findParent(parent, a) != findParent(parent, b):
        totalCost += cost
        uinonParent(parent, a, b)
        last = cost # 제일 큰 간선은 뺄 것임
        
result = totalCost - last

print(result)
