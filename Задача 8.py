sum = 0
count = 0

for i in range(4):
    n = int(input())
    if n % 2 != 0:
        sum += n
        count += 1

print('Количество нечетных: ', count)
print('Сумма нечетных: ', sum)