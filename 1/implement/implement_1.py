X = int(input())

arr = input().split()

mineX = 1;
mineY = 1;

# 입력받은 arr만큼 좌표 이동..
for i in range(len(arr)):
    if arr[i] == 'L' and mineY > 1:
        mineY -= 1
    elif arr[i] == 'R' and mineY < X:
        mineY += 1
    elif arr[i] == 'U' and mineX > 1:
        mineX -= 1
    elif arr[i] == 'D' and mineX < X:
        mineX += 1

print("%d %d" % (mineX, mineY))
