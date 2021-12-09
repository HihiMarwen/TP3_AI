from taquin import taquin
import dfs
def prof_iter(mat):
    closed_mat=[]
    x=0
    while not mat.result: 
        dfs.arbre_niv.clear()
        dfs.prof(mat,mat,x)
        for i in range(dfs.arbre_niv):
            closed_mat.append(dfs.arbre_niv[i])
        x+=1
        for j in range(len(dfs.arbre_niv)):
            print(j)
            print(dfs.arbre_niv[j].matrice)
    mat=closed_mat[-1]
    mat.cout=len(closed_mat)
    print("cout = ", len(mat.cout))