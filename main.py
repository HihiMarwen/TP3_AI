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
print("1- Largeur d'abord")
print("2- profendeur d'abord")
print("3- profendeur itérative")

choix=int(input("choix = "))

if choix == 1:
    bfs.largeur(mat)
elif choix == 2:
    dfs.prof(mat,mat)
    if mat.result:
        print("Solution Trouvée\n Cout = ",mat.cout)
    else:
        print("La solution est encore loin",mat.cout)
elif choix == 3:
    i_dfs.prof_iter(mat)