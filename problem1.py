

n = int(input("N sonini kiriting:  "))
k = int(input("K sonini kiriting:  "))

ls = ["I" for i in range(n)]

for i in range(k):
    s,e = list(map(int,input().split()))
    for j in range(s-1,e):
        ls[j] = "*"
print(" ".join(ls))