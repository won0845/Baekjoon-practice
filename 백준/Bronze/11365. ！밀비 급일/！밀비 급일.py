import sys

input = sys.stdin.readline

string = input().strip()
while string != "END":
    print(string[::-1])
    string = input().strip()