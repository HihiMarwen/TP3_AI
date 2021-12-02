class taquin :
    def __init__(self,n):

        self.etat_final=[[0,1,2],[3,4,5],[6,7,8]]
        self=[[0,1,2],[3,4,5],[6,7,8]]
        #self=[[]]
        self.n=n
        i=j=x=0
        '''while i<n:
            while j < n:
                x+=1
                self[i][j]=x
                j+=1
            i+=1'''
    
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


    def verif_mvt(self,i,j): #verif anehi l case l fergha
        if self[i-1][j]==0 and i>0:
            return("up")
        elif self[i+1][j]==0 and i+1<self.n:
            return("down")
        elif self[i][j+1]==0 and j+1<self.n:
            return("right")
        elif self[i][j-1]==0and j>0:
            return("left")
        else :
            return("none")
        
        
    def verif_final(self):
        if self==self.etat_final:
            return True
        else : return False
        
    


mat=taquin(input("saisir la taille : "))
mat.matrice[2]
print(mat.matrice[2][1])