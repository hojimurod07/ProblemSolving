

ls  = ["3:1","2:2","1:5","4:0"]

uz= 0
another = 0
scores = 0


for i in ls:
    num1 = int(i.split(":")[0])
    num2 = int(i.split(":")[1])
    uz+=num1
    another+=num2
    if num1>num2:
        scores+=3

    elif num1==num2:
        scores+=1

print(f"{scores} scores {uz}-{another}" )