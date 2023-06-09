# 마을을 분할할 예정. 분리된 마을 안에 집들은 연결되도록 해야함
# 유지비가 최소로 되게끔 하고 싶어함.

# 루트노드를 찾아주는 함수
def findParent(parent, x):
    if parent[x] != x:
        # 루트노드가 아니라면 재귀적으로 호출
        return findParent(parent, parent[x])
    return parent[x]


def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# n: 집 갯수, m: 집을 연결하는 길 (양방향)
n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n+1):
    parent[i] = i

edges = []
for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 금액순으로 정렬
edges.sort()
# 마을을 2개로 만들거이므로 비용이 큰 간선 하나는 없애도됨..
last = 0 # 가장 비용이 큰 간선
result = 0
for edge in edges:
    cost, a, b = edge
    # 이미 갈 수있는 곳은 무시..
    if findParent(parent, a) != findParent(parent, b):
        unionParent(parent, a, b)
        result += cost
        last = cost

print(result-last)
