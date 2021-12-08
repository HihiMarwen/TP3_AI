import copy
import numpy as np

class taquin :
    def __init__(self,n):
        self.n=n
        self.fils=[]
        self.matrice=[[]]
        self.matrice_final=self.init_final_state(n)
        self.cout=0
        self.niv=0
        self.result=True
        self.empty=(n,n)

    def init_final_state(self,n):
        self.matrice_final=np.random.randint(n*n, size=(n,n))

        #initruire une filse contenant des entiers random et unique
        fils_random = []
        while len(fils_random) < n*n:
        #This checks to see if there are duplicate numbers
            r = np.random.randint(0,n*n)
            if r not in fils_random :
                fils_random.append(r)
        fils_random.sort()

        for i in range(0,n):
            self.matrice_final[n-i-1]=fils_random[-n:]
            for j in range(0,n):
                fils_random.pop()
        return(self.matrice_final)
        
    def init_state(self,n):
        self.matrice = np.random.randint(n*n, size=(n,n))
        print("Saisir les chiffres avec l'ordre souhaité : ")
        str_values = input().split(" ")
        
        for i in range(len(str_values)):
            str_values[i]=int(str_values[i])

        for i in range(0,n):
            self.matrice[n-i-1]=str_values[-n:]
            
            for j in range(0,n):
                str_values.pop()
        
        return(self.matrice)
        
    def init_random(self,n):
        self.matrice = np.random.randint(n*n, size=(n,n))

        #initruire une filse contenant des entiers random et unique
        fils_random = []
        while len(fils_random) < n*n:
        #This checks to see if there are duplicate numbers
            r = np.random.randint(0,n*n)
            if r not in fils_random :
                fils_random.append(r)

        for i in range(0,n):
                self.matrice[n-i-1]=fils_random[-n:]
                for j in range(0,n):
                    fils_random.pop()
               
        return(self.matrice)
    
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
                                    
    def trans(self,i,j,token): #win bch yemchi    
        if token!="null":
            fils=copy.deepcopy(self)
            if token=="up":
                fils.matrice[i-1][j]=copy.deepcopy(self.matrice[i][j])
            
            elif token=="down":
                fils.matrice[i+1][j]=copy.deepcopy(self.matrice[i][j])

            elif token=="right":
                fils.matrice[i][j+1]=copy.deepcopy(self.matrice[i][j])

            elif token=="left":
                fils.matrice[i][j-1]=copy.deepcopy(self.matrice[i][j])
            
            fils.matrice[i][j]=0
        return fils

    def fill_empty(self,token,i,j):
        if token!="null":
            fils=copy.deepcopy(self)
            if token=="up":
                self.empty=(i-1,j)
                
            elif token=="down":
                self.empty=(i+1,j)
                
            elif token=="right":
                self.empty=(i,j+1)
                
            elif token=="left":
                self.empty=(i,j-1)
                
    
    def make_fils(self):
        
        for i in range(self.n):
            for j in range(self.n):
                token=self.verif_mvt(self.matrice,i,j)
                
                if token!="null" and (i,j)!=self.empty:
                    self.fils.append(self.trans(i,j,token))
                    self.fils[-1].fill_empty(token,i,j)
        return(self.fils)
    
    def verif_final(self):
        self.init_final_state(self.n)
        for i in range(0,self.n):
            for j in range(0,self.n):
                
                if self.matrice[i][j]!=self.matrice_final[i][j]:
                    return False
        return True
        
    def arbre(self,mat):
        print("********")
        print(mat.matrice)
        print(mat.verif_final())
        if mat.verif_final()==False and self.niv<100:
            self.result=False
            mat.list=mat.make_fils()
            self.niv+=1
            for i in range(len(mat.fils)):
                self.cout+=1 
                
                mat.fils[i].niv=mat.niv+1
                self.arbre(mat.fils[i])
                if self.result:
                    break
        else : self.result=True    
           
                

size=int(input("saisir la taille : "))
mat=taquin(size)
#mat.init_random(size)
mat.init_state(size)
print("Taquin Initial:")
print(mat.matrice)
print("Taquin final:")
print(mat.matrice_final)

mat.arbre(mat)
if mat.cout >= 100:
    print("solution pas trouvée",mat.cout,mat.niv)
else:
    print("Solution Trouvée\n Cout = ",mat.cout,mat.niv)
