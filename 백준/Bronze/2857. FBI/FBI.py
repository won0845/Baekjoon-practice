lst = []
answer = "HE GOT AWAY!"

for i in range(5):
    agent = input().strip()
    if "FBI" in agent:
        answer = ""
        print(i + 1, end=" ")
if answer != "":
    print("HE GOT AWAY!")

