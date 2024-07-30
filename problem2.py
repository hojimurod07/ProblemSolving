

ls = list(map(int,input().split()))

for i in range(len(ls)):
    if ls[i] in ls[:i]:
        print("Yes")
    else:
        print("No")
