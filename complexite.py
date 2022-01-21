if __name__ == '__main__':
    chaine = input("entrer une chaine : ")

    # chercher le nombre de compléxité :
    compl=""
    for i in range(len(chaine)):
        compteur=0
        for j in range(len(compl)):
            if(chaine[i] == compl[j]):
                compteur +=1
        if(compteur == 0):
            compl +=chaine[i]
    if(len(compl) <2):
        print(0)
    else:
        print(len(compl) - 2)


