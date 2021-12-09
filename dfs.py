from taquin import taquin

def prof(taq,mat):
    print("********")
    print(mat.matrice)
    
    if not mat.verif_final():
        if mat.niv<4:
            print(mat.niv)
            taq.result=False
            mat.fils=mat.make_fils()
            for i in range(len(mat.fils)):
                print(mat.fils[i].matrice,i)
            
            for i in range(len(mat.fils)): 
                taq.cout+=1
                mat.fils[i].niv=mat.niv+1
                prof(taq,mat.fils[i])
                if taq.result:
                    break
        
    else : taq.result=True