from taquin import taquin
   
def largeur(mat):
    open_mat=[mat]
    closed_mat=[mat]
    while len(open_mat)!=0:
        mat=open_mat[0]
        mat.make_fils()
        for i in range(len(mat.fils)):
            open_mat.append(mat.fils[i])
            closed_mat.append(mat.fils[i])
        
        open_mat.pop(0)
        
        if open_mat[0].verif_final():
            open_mat.clear()
            while not closed_mat[-1].verif_final():
                closed_mat.pop()
            for j in range(len(closed_mat)):
                print(j)
                print(closed_mat[j].matrice)
    mat=closed_mat[-1]
    mat.cout=len(closed_mat)
    print("cout = ", mat.cout)