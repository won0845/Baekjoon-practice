import sys
input = sys.stdin.readline

def main():
    n = int(input())

    for i in range(1, n+1):
        a,b = map(int, input().split())
        print("Case #{}: {} + {} = {}".format(i,a,b,a+b))
        
if __name__ == "__main__":
    main()