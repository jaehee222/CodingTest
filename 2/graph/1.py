# 팀결성
# 0~N번까지 학생에게 번호 부여. 팀은 N+1개 존재
# 팀합치기, 같은팀여부확인 연산을 사용
# 연산 결과 출력하는 프로그램 작성

def findParent(parent, x):
    if parent[x] != x:
        return findParent(parent, parent[x])
    return parent[x]


def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n + 1)

# 초기화
for i in range(n):
    parent[i] = i

for i in range(m):
    tema, a, b = map(int, input().split())
    if tema == 0:  # 팀합치기 연산
        unionParent(parent, a, b)
    elif tema == 1:
        if findParent(parent, a) == findParent(parent, b):
            print('YES')
        else:
            print('NO')
