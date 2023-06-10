# 성적이 낮은 순서로 학생 출력하기
# N명의 학생정보 있음. 성적이 낮은 순서로 학생이름을 출력

n = int(input())
array = []
for i in range(n):
    array.append(list(input().split()))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0],end=' ')
