


if __name__ == '__main__':
    try:
        S = int(input("entrer la plus grand taille : "))

        if (S < 1 or S > 10 ** 9):
            print(" 1<= S <= 10^9")
            S = int(input("entrer la plus grand taille : "))
        X = int(input("X : "))
        if (X < 2 or X > 10 ** 9):
            print(" 2<= X <= 10^9")
            X = int(input("X : "))
        compteur = 1
        tailleP = S // X
        print(tailleP)
        while tailleP > 0:
            tailleP = tailleP // X
            compteur += 1
        print(compteur)
    except:
        print("l'entrer doit etre un nombre entier")

