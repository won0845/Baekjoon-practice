sleepTime = int(input())
wakeTime = int(input())

if 20 <= sleepTime <= 23:
    print(24-sleepTime+wakeTime)
else:
    print(wakeTime-sleepTime)