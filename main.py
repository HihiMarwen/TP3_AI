from taquin import taquin
import bfs
import dfs
import i_dfs


size=int(input("saisir la taille : "))
mat=taquin(size)
#mat.init_random(size)
mat.init_state(size)
print("Taquin Initial:")
print(mat.matrice)
print("Taquin final:")
print(mat.matrice_final)
print("Choisir la methode du recherche : ")

exit="no"
while exit!="yes":
    mat.cout=0
    print("1- Largeur d'abord")
    print("2- profendeur d'abord")
    print("3- profendeur itérative")
    choix=int(input("choix = "))
    if choix == 1:
        bfs.largeur(mat)
    elif choix == 2:
        x=int(input("choisir une limite de recherche : "))
        dfs.prof(mat,mat,x-1)
        if mat.result:
            print("Solution Trouvée")
        else:
            print("La solution est encore loin")
    elif choix == 3:
        i_dfs.prof_iter(mat)
        
    print("cout = ", mat.cout)

    exit=input("do you want to exit ?(type yes/no): ")