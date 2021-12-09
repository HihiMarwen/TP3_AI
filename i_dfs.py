from taquin import taquin
import dfs
def prof_iter(mat):
    mat.result=False
    closed_mat=[mat]
    x=0
    while not mat.result: 
        dfs.arbre_niv.clear()
        dfs.prof(mat,mat,x)
        print("****************")
            
        for i in range(len(dfs.arbre_niv)):
            closed_mat.append(dfs.arbre_niv[i])
        x+=1
    
    mat.cout=len(closed_mat)-2
    print(mat.cout)