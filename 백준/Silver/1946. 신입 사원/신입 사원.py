import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

test_num = int(input())

for _ in range(test_num):
    applicant_num = int(input())
    grade_list = []
    for _ in range(applicant_num):
        brief_grade, interview_grade = map(int, input().split())
        grade_list.append([brief_grade, interview_grade])
    grade_list.sort(key=lambda x: x[0])

    count = 1
    first = grade_list[0][1]
    for i in range(1, len(grade_list)):
        if first >= grade_list[i][1]:
            first = grade_list[i][1]
            count += 1
    print(count)
