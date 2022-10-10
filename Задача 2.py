n = int(input())
n = list(str(n))
a = []

for i in n:
    for j in n:
        for k in n:
            s = i + j + k
            if s.count(i) == 1 and s.count(j) == 1 and s.count(k) == 1:
                a.append(int(s))

for i in range(len(a)):
    print(a[i])
