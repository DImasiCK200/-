a = [10, 00]

n = 0
for i in range(3):
    n += int(input())

print(a[0] + n // 60, a[1] + n % 60, sep = ':')