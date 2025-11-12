n = input().strip()

if n[0] == '-':
    first = int(n[1])
else:
    first = int(n[0])

last = int(n[-1])

print(first + last)