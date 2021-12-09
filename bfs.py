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
        for j in range(len(open_mat)):
                print(j,open_mat[j].matrice)
        open_mat.pop(0)
        if open_mat[0].verif_final():
            open_mat.clear()
            while not closed_mat[-1].verif_final():
                closed_mat.pop()
            for j in range(len(closed_mat)):
                print(closed_mat[j].matrice,j)
    
    print("cout = ", len(closed_mat))
                
                
size=int(input("saisir la taille : "))
mat=taquin(size)
#mat.init_random(size)
mat.init_state(size)
print("Taquin Initial:")
print(mat.matrice)
print("Taquin final:")
print(mat.matrice_final)

largeur(mat)