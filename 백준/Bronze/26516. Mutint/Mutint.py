while True:
    n = list(map(int, input()))

    if n[0] == 0:
        break

    max_n = max(n)
    max_p = n.index(max_n)

    if max_n % 2 == 1:
        n[max_p] = 0
    else:
        max_n += 4
        if max_n > 9:
            string_max = str(max_n)
            max_n = int(string_max[1])

        n[max_p] = max_n

    print(int("".join(map(str, n))))