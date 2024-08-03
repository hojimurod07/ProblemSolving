def GenerateNumsFibo(n: int):
    ls = [1, 1]
    while len(ls) < n:
        ls.append(ls[-1] + ls[-2])
    return ls




def Peramida(son:int):
    ls = GenerateNumsFibo(son)

    for i in range(1, son + 1):
        for j in range(2 * son - 1):
            if j >= son - i and j <= son + i - 2:
                print("*", end=" ")
            else:
                print(" ", end="")
        print("")
Peramida(5)
