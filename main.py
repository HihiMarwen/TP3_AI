class taquin :
    def __init__(self):

        self.matrice=[[0,1,2],[3,4,5],[6,7,8]]
        #self=[[]]
        n=3
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
                matrice[i+1][j]=matrice[i][j]
            
            elif token=="down":
                matrice[i-1][j]=matrice[i][j]

            elif token=="right":
                matrice[i][j+1]=matrice[i][j]

            elif token=="left":
                matrice[i][j-1]=matrice[i][j]
            
            matrice[i][j]=0


    def verif_mvt(matrice,i,j): #verif anehi l case l fergha
        if matrice[i-1][j]==0 and i>0:
            return("up")
        elif matrice[i+1][j]==0 and :
            return("down")
        elif matrice[i][j+1]==0:
            return("right")
        elif matrice[i][j-1]==0:
            return("left")
        else :
            return("none")


mat=taquin()
mat.matrice[2]
print(mat.matrice[2][1])