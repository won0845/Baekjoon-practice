import sys

input = sys.stdin.readline


def main():
    Num = int(input())
    list1 = list(map(int, input().split()))
    print("{} {}".format(min(list1), max(list1)))

if __name__ == "__main__":
    main()
