# 모험가 N명의 공포도 측정
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야함
# 동빈이는 최대 몇개의 그룹을 만들 수 있을까?
# -> 정렬 후 가장 큰 숫자만큼 팀 만들고,, 팀이 안된 것중에 가장 큰 숫자만큼 팀 만들고.. 반복


n = int(input())
Team = list(map(int, input().split()))
Team.sort()

maxPerson = Team[n - 1] # 가장 큰 공포도..
teamNum = 0
while n > 0:
    # 남은 인원이 현재 애 공포도 보다 작으면 옆팀에 붙여줌
    if n < maxPerson:
        maxPerson = Team[n-1]
        n -= 1
    # 딱 맞게 남았으면 팀만들고 break
    elif n == maxPerson:
      teamNum += 1
      break
    else:
        n -= Team[n-1]
        maxPerson = Team[n-1]
        teamNum += 1

print(teamNum)
