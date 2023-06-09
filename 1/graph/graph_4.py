# 팀결성
# 0~N번까지 번호 부여
# 팀합치기, 같은팀 여부 확인

def findParent(parent, x):
    if parent[x] != x:
        return findParent(parent, parent[x])
    return parent[x]

# 팀합치기
def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# n: 학생에게 부여한 번호 수, m: 입력으로 주어지는 연산 갯수
n, m = map(int, input().split())
parent = [0] * (n + 1)
result = []

for i in range(1, n+1):
    # 자기자신을 부모로 초기화
    parent[i] = i

for i in range(m):
    info, a, b = map(int, input().split())
    # info 0: 팀합치기, 1: 같은팀여부 확인
    if info == 0:
        unionParent(parent, a, b)
    else:
        if findParent(parent,a) == findParent(parent,b):
            result.append("YES")
        else:
            result.append("NO")

for i in result:
    print(i)
