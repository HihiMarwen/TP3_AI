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

dfs.prof(mat,mat)
if mat.result:
    print("Solution Trouvée\n Cout = ",mat.cout)
else:
    print("La solution est encore loin",mat.cout)