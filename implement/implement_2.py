X = int(input())

cnt = 0
tmp = [0, 0, 0]
while True:
    # 하나라도 3이 있으면 cnt++
    if str(tmp[0]).find('3') > -1 or str(tmp[1]).find('3') > -1 or str(tmp[2]).find('3') > -1:
        cnt += 1
    # 시간 +1
    tmp[2] += 1
    # 60초 일 경우
    if tmp[2] == 60:
        tmp[2] = 0
        tmp[1] += 1
    if tmp[1] == 60:
        tmp[1] = 0
        tmp[0] += 1

    if tmp[0] == X and tmp[1] == 59 and tmp[2] == 59: break

print(cnt)
