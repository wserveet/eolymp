a = int(input())
while True:
    liste = list(map(int, input().split()))
    if len(liste) == a:
        break
print(max(liste)+min(liste))