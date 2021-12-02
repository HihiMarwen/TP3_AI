
import numpy as np
class taquin :
    def __init__(self,n):
        self.n=n
        self.list=[]
        self.matrice=[[]]
        self.matrice_final=[[]]
        
    def const_random_mat(self,n):
        self.matrice = np.random.randint(n*n, size=(n,n))

        #construire une liste contenant des entiers random et unique
        list_random = []
        while len(list_random) < n*n:
        #This checks to see if there are duplicate numbers
            r = np.random.randint(0,n*n)
            if r not in list_random :
                list_random.append(r)

        for i in range(0,n):
                self.matrice[i]=list_random[-3:]
                list_random.pop()
                list_random.pop()
                list_random.pop()
        return(self.matrice)
                            
    def trans(matrice,i,j,token): #win bch yemchi
        if token!="none":
            if token=="up":
                matrice[i-1][j]=matrice[i][j]
            
            elif token=="down":
                matrice[i+1][j]=matrice[i][j]

            elif token=="right":
                matrice[i][j+1]=matrice[i][j]

            elif token=="left":
                matrice[i][j-1]=matrice[i][j]
            
            matrice[i][j]=0

    def verif_mvt(self,matrice,i,j): #verif anehi l case l fergha
        if matrice[i-1][j]==0 and i>0:
            return("up")
        elif matrice[i+1][j]==0 and i+1<self.n:
            return("down")
        elif matrice[i][j+1]==0 and j+1<self.n:
            return("right")
        elif matrice[i][j-1]==0and j>0:
            return("left")
        else :
            return("none")
         
    def verif_final(self):

        if self==self.etat_final:
            return True
        else : return False
        
    

size=int(input("saisir la taille : "))
mat=taquin(size)
mat.const_random_mat(size)
print(mat.matrice)

