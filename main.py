import copy
import numpy as np
class taquin :
    def __init__(self,n):
        self.n=n
        self.list=[]
        self.matrice=[[]]
        self.matrice_final=[[]]
        self.cout=0
        self.niv=0

    def mat_final(self,n):
        self.matrice_final=copy.deepcopy(self.matrice)

        #construire une liste contenant des entiers random et unique
        list_random = []
        while len(list_random) < n*n:
        #This checks to see if there are duplicate numbers
            r = np.random.randint(0,n*n)
            if r not in list_random :
                list_random.append(r)
        list_random.sort()

        for i in range(0,n):
            self.matrice_final[n-i-1]=list_random[-n:]
            for j in range(0,n):
                list_random.pop()
        return(self.matrice_final)
        
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
                self.matrice[n-i-1]=list_random[-n:]
                for j in range(0,n):
                    list_random.pop()
               
        return(self.matrice)
                            
    def trans(self,i,j,token): #win bch yemchi
        
        if token!="null":
            fils=copy.deepcopy(self.matrice)
            if token=="up":
                fils[i-1][j]=copy.deepcopy(self.matrice[i][j])
            
            elif token=="down":
                fils[i+1][j]=copy.deepcopy(self.matrice[i][j])

            elif token=="right":
                fils[i][j+1]=copy.deepcopy(self.matrice[i][j])

            elif token=="left":
                fils[i][j-1]=copy.deepcopy(self.matrice[i][j])
            
            fils[i][j]=0
        return fils

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
         
    def verif_final(self,matrice):
        for i in range(0,self.n):
            for j in range(0,self.n):
                
                if matrice[i][j]!=self.matrice_final[i][j]:
                    return False
        return True
        
    
    def make_list(self,matrice):
        
        for i in range(0,self.n):
            for j in range(0,self.n):
                token=matrice.verif_mvt(self.matrice,i,j)
                
                if token!="null":
                    matrice.list.append(self.trans(i,j,token))
        return(matrice)
        
    def arbre(self,matrice):
        if self.verif_final(matrice.matrice)==False and self.cout<100:
            matrice=matrice.make_list(matrice)
            for i in range(0,len(matrice.list)):
                self.cout+=1
                matrice.niv+=1
                verif=self.arbre(matrice.list[i])
               
                return True
                
        else : return(True)        
                

size=int(input("saisir la taille : "))
mat=taquin(size)
mat.const_random_mat(size)
print("Taquin Initial: \n ",mat.matrice)
mat.mat_final(size)
print("Taquin final: \n ",mat.matrice_final)

mat.arbre(mat)
if mat.cout >= 100:
    print("solution pas trouvée")
else:
    print("Solution Trouvée\n Cout = ",mat.cout)

'''mat.make_list()
print("Les cas possibles")
for i in range(0,len(mat.list)):
    print(mat.list[i])
    print("********")'''

