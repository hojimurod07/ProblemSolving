

a = int(input("A: "))

b = int(input("b: "))

max = ((a // b) * a + (b // a) * b) // (a // b + b // a)
print(max)

