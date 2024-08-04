
matn = "Salom bollar ishlar qalay ? Hali imtihon tugamadimi? "


start= 0
end = 0
i = 0
count = 0
while True:
    if matn[i] =='h' or matn[i]=='H' and count==0:
        start = i
        count+=1
    elif matn[i] =='h' or matn[i]=='H'  and count==1:
        end = i
        break
    i+=1




natija =[]
natija.append(matn)
natija.append(matn[start+1:end]*2)
natija.append(matn[end:])
print(" ".join(natija))
