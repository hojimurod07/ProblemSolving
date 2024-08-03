ls = [1,1,1,1,1]

c = 0
for i in range(len(ls)):
    for j in range(i+1, len(ls)):  # Start j from i+1 to avoid counting the same pair twice
        if ls[j] == ls[i]:
            c += 1

print(c)
