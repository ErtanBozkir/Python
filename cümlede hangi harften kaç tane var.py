liste=input("cümleyi giriniz:")
liste2=[]
for i in range(0,len(liste)):
    var=0
    for a in range(0,len(liste2)):
        if liste2[a]==liste[i]:
            var+=1
            break
    say=1
    if var==0:
        for j in range((i+1),len(liste)):
            if liste[i]==liste[j]:
                say+=1
                liste2.append(liste[i])

        print(say,liste[i])