from taquin import taquin
   
def largeur(mat):
    open_mat=[mat]
    closed_mat=[mat]
    while len(open_mat)!=0:
        open_mat[0].make_fils()
        for i in range(len(open_mat[0].fils)):
            open_mat.append(open_mat[0].fils[i])
            closed_mat.append(open_mat[0].fils[i])
        
        open_mat.pop(0)
        
        if open_mat[0].verif_final():
            open_mat.clear()
            while not closed_mat[-1].verif_final():
                closed_mat.pop()
            for j in range(len(closed_mat)):
                print(j)
                print(closed_mat[j].matrice)
    mat.cout=len(closed_mat)-1