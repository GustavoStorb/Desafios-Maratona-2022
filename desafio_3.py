T = int(input())

CONTADOR = []
i = 0


while i < T:
    n = int(input())
    filtro = list(filter(None, input().split(" ")))
    split = [int(x) for x in filtro]

    count = 0

    ii = 0
    while ii < len(split):
        a = ii - 1
        b = ii

        while split[b] < split[a] and a > -1:
            split.insert(a, split.pop(b))
            b = a
            a = a - 1
            count += 1

        ii += 1

    CONTADOR.append(count)

    i += 1

print()
for count in CONTADOR:
    print(count)
