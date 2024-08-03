


word = "card"

res = ""
mid = len(word)//2
if len(word)%2==1:

    for i in range(mid+1):
        res+="("+word[i]
    for i in range(mid+1,len(word)):
        res+=")"+word[i]
    res+=")"


else:
    for i in range(mid):
        res+="("+word[i]

    for i in range(mid,len(word)):
        res+=word[i]+")"
    
print(res)