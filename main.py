
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
                self.matrice[i]=list_random[-n:]
                for j in range(0,n):
                    list_random.pop()
               
        return(self.matrice)
                            
    def trans(matrice,i,j,token): #win bch yemchi
        if token!="null":
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
        if i>0 and matrice[i-1][j]==0:
            return("up")
        elif i+1<self.n and matrice[i+1][j]==0 :
            return("down")
        elif j+1<self.n and matrice[i][j+1]==0 :
            return("right")
        elif j>0 and matrice[i][j-1]==0:
            return("left")
        else :
            return("null")
         
    def verif_final(self):

        if self.matrice==self.matrice_final:
            return True
        else : return False
        
    
    def make_list(self):
        i=j=0
        while i in range(0,self.n):
            while j in range(0,self.n):
                token=self.verif_mvt(self.matrice,i,j)
                if token!="null":
                    self.list.append(self.trans(i,j,token))
        
    def arbre(self):
        i=j=0
        while self.verif_final()==False:
            
                    return
                
                
                

size=int(input("saisir la taille : "))
mat=taquin(size)
mat.const_random_mat(size)
print(mat.matrice)

