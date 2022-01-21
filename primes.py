if __name__ == '__main__':
    try:
        n = int(input("entrer un nombre premier : "))
        if(n<2 or n>10**7):
            n = int(input("le nombre doit etre entre 2 et 10^7 : "))
        condition =1
        while 1 :
            c=0
            for i in range(2, (n // 2) + 1):
                if (n % i == 0):
                    c +=1
            if(c==0):
                break
            else:
                n = int(input("le nombre que vous avez entrer n'est pas premier : "))


        tabNP = list()
        d=0
        for i in range(2,n-1):
            compteur = 0
            for j in range(2,i//2+1):
                if(i%j==0 ):
                    compteur +=1
            if(compteur ==0):
                tabNP.append(i)

                if(len(tabNP) > 1):
                    for k in range(len(tabNP)-1):
                        if(i + tabNP[k] == n):
                            d+=1;
                            print(str(i)+" + "+str(tabNP[k])+" = " + str(n) + "\n")
        if(d==0):
            print(-1)
    except:
        print("l'entrer doit etre un nombre entier premier !!")