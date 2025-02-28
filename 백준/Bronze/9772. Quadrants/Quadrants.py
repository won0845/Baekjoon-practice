def determine_quadrant(x, y):
    if x == 0 or y == 0:
        return 'AXIS'
    elif x > 0 and y > 0:
        return 'Q1'
    elif x < 0 and y > 0:
        return 'Q2'
    elif x < 0 and y < 0:
        return 'Q3'
    elif x > 0 and y < 0:
        return 'Q4'

if __name__ == '__main__':
    while True:
        x, y = map(float, input().split())
        print(determine_quadrant(x, y))
        if x == 0 and y == 0:
            break
