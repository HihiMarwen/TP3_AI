from taquin import taquin
arbre_niv=[]
def prof(taq,mat,x):
    print("niv : ",mat.niv)
    arbre_niv.append(mat)
    print(arbre_niv[-1].matrice)
    if not mat.verif_final():
        if mat.niv<=x:
            
            taq.result=False
            mat.fils=mat.make_fils()
            '''for i in range(len(mat.fils)):
                print(i)
                print(mat.fils[i].matrice)'''
            
            for i in range(len(mat.fils)): 
                taq.cout+=1
                mat.fils[i].niv=mat.niv+1
                prof(taq,mat.fils[i],x)
                if taq.result:
                    break
        
    else : taq.result=True
    
    