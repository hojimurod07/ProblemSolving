


ls = input("Enter names: ").split()


if len(ls)<0:
    print("No one likes this")
elif len(ls)==1:
    print(f"{ls[0]} likes this")
elif len(ls)==2:
    print(f"{ls[0]} and {ls[1]} likes this")
else:
    j = ""
    for i in range(len(ls)-2):
        j+=f"{ls[i]}, "
    j+=f"{ls[-2]}"
    j+=f" and {ls[-1]} like this "
    print(j)