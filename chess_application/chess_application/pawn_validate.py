class pawn_validator:
    def __init__(self,matrix,i,j):
        self.matrix=matrix
        self.x=i
        self.y=j
    def out_of_matrix(self,i,j):
        if i>=8 or i<0 or j>=8 or j<0:
            return False
        return True
    def is_safe(self,i,j):
        if self.out_of_matrix(i,j):
            if self.matrix[i][j]==None:
                return True
            
        return False
            
        
        return True
    def validate(self):
        i=self.x
        j=self.y
        if self.matrix[i][j]=="pw":
            return self.validate_pw()
        if self.matrix[i][j]=="pb":
            return self.validate_pb()
    def validate_pb(self):
        row=self.x
        col=self.y
        valid_path=list()
        check_mate=list()
        if row==6 :#this give us two move if pawn lie in initial stage
            for x in range(2):
                if self.is_safe(row-(x+1),col):
                    valid_path.append((row-(x+1),col))
                else:
                    break
            
        else :
            if self.is_safe(row-1,col):
                valid_path.append((row-1,col))
        if self.out_of_matrix(row-1,col-1)==True and self.matrix[row-1][col-1]!=None and self.matrix[row-1][col-1][len(self.matrix[row-1][col-1])-1]=='w':
            check_mate.append((row-1,col-1))
        if self.out_of_matrix(row-1,col+1)==True and self.matrix[row-1][col+1]!=None and self.matrix[row-1][col+1][len(self.matrix[row-1][col+1])-1]=='w':
            check_mate.append((row-1,col+1))
        return (valid_path,check_mate)
    def validate_pw(self):
        row=self.x
        col=self.y
        valid_path=list()
        check_mate=list()
        if row==1 :#this give us two move if pawn lie in initial stage
            for x in range(2):
                if self.is_safe(row+(x+1),col):
                    valid_path.append((row+(x+1),col))
                else:
                    break
            
        else:
            if self.is_safe(row+1,col):
                valid_path.append((row+1,col))
        if self.out_of_matrix(row+1,col+1)==True and self.matrix[row+1][col+1]!=None and self.matrix[row+1][col+1][len(self.matrix[row+1][col+1])-1]=='b':
            check_mate.append((row+1,col+1))
        if self.out_of_matrix(row+1,col-1)==True and self.matrix[row+1][col-1]!=None and self.matrix[row+1][col-1][len(self.matrix[row+1][col-1])-1]=='b':
            check_mate.append((row+1,col-1))
        return (valid_path,check_mate)

class bishop_validator:
    def __init__(self,matrix,i,j):
        self.matrix=matrix
        self.x=i
        self.y=j
    def out_of_matrix(self,i,j):
        if i>=8 or i<0 or j>=8 or j<0:
            return False
        return True
    def is_safe(self,i,j):
        if self.out_of_matrix(i,j):
            if self.matrix[i][j]==None:
                return True
            
        return False
            
        
        
    def validate(self):
        i=self.x
        j=self.y
        if self.matrix[i][j]=="bw":
            return self.validate_bw()
        if self.matrix[i][j]=="bb":
            return self.validate_bb()
    def validate_bb(self):
        row=self.x
        col=self.y
        valid_path=list()
        check_mate=list()
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i+1,j+1)==True:
                valid_path.append((i+1,j+1))
            else:
                if self.out_of_matrix(i+1,j+1)==True and self.matrix[i+1][j+1][len(self.matrix[i+1][j+1])-1]=='w':
                    check_mate.append((i+1,j+1))
                break
            i+=1
            j+=1
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i-1,j-1)==True:
                valid_path.append((i-1,j-1))
            else:
                if self.out_of_matrix(i-1,j-1)==True and self.matrix[i-1][j-1][len(self.matrix[i-1][j-1])-1]=='w':
                    check_mate.append((i-1,j-1))
                break
            i-=1
            j-=1
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i+1,j-1)==True:
                valid_path.append((i+1,j-1))
            else:
                if self.out_of_matrix(i+1,j-1)==True and self.matrix[i+1][j-1][len(self.matrix[i+1][j-1])-1]=='w':
                    check_mate.append((i+1,j-1))
                break
            i+=1
            j-=1
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i-1,j+1)==True:
                valid_path.append((i-1,j+1))
            else:
                if self.out_of_matrix(i-1,j+1)==True and self.matrix[i-1][j+1][len(self.matrix[i-1][j+1])-1]=='w':
                    check_mate.append((i-1,j+1))
                break
            i-=1
            j+=1
        return (valid_path,check_mate)
        
        
    def validate_bw(self):
        row=self.x
        col=self.y
        valid_path=list()
        check_mate=list()
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i+1,j+1)==True:
                valid_path.append((i+1,j+1))
            else:
                if self.out_of_matrix(i+1,j+1)==True and self.matrix[i+1][j+1][len(self.matrix[i+1][j+1])-1]=='b':
                    check_mate.append((i+1,j+1))
                break
            i+=1
            j+=1
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i-1,j-1)==True:
                valid_path.append((i-1,j-1))
            else:
                if self.out_of_matrix(i-1,j-1)==True and self.matrix[i-1][j-1][len(self.matrix[i-1][j-1])-1]=='b':
                    check_mate.append((i-1,j-1))
                break
            i-=1
            j-=1
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i+1,j-1)==True:
                valid_path.append((i+1,j-1))
            else:
                if self.out_of_matrix(i+1,j-1)==True and self.matrix[i+1][j-1][len(self.matrix[i+1][j-1])-1]=='b':
                    check_mate.append((i+1,j-1))
                break
            i+=1
            j-=1
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i-1,j+1)==True:
                valid_path.append((i-1,j+1))
            else:
                if self.out_of_matrix(i-1,j+1)==True and self.matrix[i-1][j+1][len(self.matrix[i-1][j+1])-1]=='b':
                    check_mate.append((i-1,j+1))
                break
            i-=1
            j+=1
        return (valid_path,check_mate)
class queen_validator:
    def __init__(self,matrix,i,j):
        self.matrix=matrix
        self.x=i
        self.y=j
    def out_of_matrix(self,i,j):
        if i>=8 or i<0 or j>=8 or j<0:
            return False
        return True
    def is_safe(self,i,j,):
        if self.out_of_matrix(i,j):
            if self.matrix[i][j]==None:
                return True
            
        return False
    def validate(self):
        i=self.x
        j=self.y
        if self.matrix[i][j]=="qw":
            return self.validate_qw()
        if self.matrix[i][j]=="qb":
            return self.validate_qb()
    def validate_qw(self):
        row=self.x
        col=self.y
        valid_path=list()
        check_mate=list()
                  
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i+1,j)==True:
                valid_path.append((i+1,j))
            else:
                if self.out_of_matrix(i+1,j)==True and self.matrix[i+1][j][len(self.matrix[i+1][j])-1]=='b':
                    check_mate.append((i+1,j))
                break
            i+=1
                  
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i-1,j)==True:
                valid_path.append((i-1,j))
            else:
                if self.out_of_matrix(i-1,j)==True and self.matrix[i-1][j][len(self.matrix[i-1][j])-1]=='b':
                    check_mate.append((i-1,j))
                break
            i-=1
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i,j-1)==True:
                valid_path.append((i,j-1))
            else:
                if self.out_of_matrix(i,j-1)==True and self.matrix[i][j-1][len(self.matrix[i][j-1])-1]=='b':
                    check_mate.append((i,j-1))
                break
            j-=1
        
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i,j+1)==True:
                valid_path.append((i,j+1))
            else:
                if self.out_of_matrix(i,j+1)==True and self.matrix[i][j+1][len(self.matrix[i][j+1])-1]=='b':
                    check_mate.append((i,j+1))
                break
            j+=1           
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i+1,j+1)==True:
                valid_path.append((i+1,j+1))
            else:
                if self.out_of_matrix(i+1,j+1)==True and self.matrix[i+1][j+1][len(self.matrix[i+1][j+1])-1]=='b':
                    check_mate.append((i+1,j+1))
                break
            i+=1
            j+=1
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i-1,j-1)==True:
                valid_path.append((i-1,j-1))
            else:
                if self.out_of_matrix(i-1,j-1)==True and self.matrix[i-1][j-1][len(self.matrix[i-1][j-1])-1]=='b':
                    check_mate.append((i-1,j-1))
                break
            i-=1
            j-=1
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i+1,j-1)==True:
                valid_path.append((i+1,j-1))
            else:
                if self.out_of_matrix(i+1,j-1)==True and self.matrix[i+1][j-1][len(self.matrix[i+1][j-1])-1]=='b':
                    check_mate.append((i+1,j-1))
                break
            i+=1
            j-=1
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i-1,j+1)==True:
                valid_path.append((i-1,j+1))
            else:
                if self.out_of_matrix(i-1,j+1)==True and self.matrix[i-1][j+1][len(self.matrix[i-1][j+1])-1]=='b':
                    check_mate.append((i-1,j+1))
                break
            i-=1
            j+=1
        return (valid_path,check_mate)
    

    def validate_qb(self):
        row=self.x
        col=self.y
        valid_path=list()
        check_mate=list()
                  
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i+1,j)==True:
                valid_path.append((i+1,j))
            else:
                if self.out_of_matrix(i+1,j)==True and self.matrix[i+1][j][len(self.matrix[i+1][j])-1]=='w':
                    check_mate.append((i+1,j))
                break
            i+=1
                  
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i-1,j)==True:
                valid_path.append((i-1,j))
            else:
                if self.out_of_matrix(i-1,j)==True and self.matrix[i-1][j][len(self.matrix[i-1][j])-1]=='w':
                    check_mate.append((i-1,j))
                break
            i-=1
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i,j-1)==True:
                valid_path.append((i,j-1))
            else:
                if self.out_of_matrix(i,j-1)==True and self.matrix[i][j-1][len(self.matrix[i][j-1])-1]=='w':
                    check_mate.append((i,j-1))
                break
            j-=1
        
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i,j+1)==True:
                valid_path.append((i,j+1))
            else:
                if self.out_of_matrix(i,j+1)==True and self.matrix[i][j+1][len(self.matrix[i][j+1])-1]=='w':
                    check_mate.append((i,j+1))
                break
            j+=1           
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i+1,j+1)==True:
                valid_path.append((i+1,j+1))
            else:
                if self.out_of_matrix(i+1,j+1)==True and self.matrix[i+1][j+1][len(self.matrix[i+1][j+1])-1]=='w':
                    check_mate.append((i+1,j+1))
                break
            i+=1
            j+=1
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i-1,j-1)==True:
                valid_path.append((i-1,j-1))
            else:
                if self.out_of_matrix(i-1,j-1)==True and self.matrix[i-1][j-1][len(self.matrix[i-1][j-1])-1]=='w':
                    check_mate.append((i-1,j-1))
                break
            i-=1
            j-=1
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i+1,j-1)==True:
                valid_path.append((i+1,j-1))
            else:
                if self.out_of_matrix(i+1,j-1)==True and self.matrix[i+1][j-1][len(self.matrix[i+1][j-1])-1]=='w':
                    check_mate.append((i+1,j-1))
                break
            i+=1
            j-=1
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i-1,j+1)==True:
                valid_path.append((i-1,j+1))
            else:
                if self.out_of_matrix(i-1,j+1)==True and self.matrix[i-1][j+1][len(self.matrix[i-1][j+1])-1]=='w':
                    check_mate.append((i-1,j+1))
                break
            i-=1
            j+=1
        return (valid_path,check_mate)
    
class rook_validator:
    def __init__(self,matrix,i,j):
        self.matrix=matrix
        self.x=i
        self.y=j
    def out_of_matrix(self,i,j):
        if i>=8 or i<0 or j>=8 or j<0:
            return False
        return True
    def is_safe(self,i,j,):
        if self.out_of_matrix(i,j):
            if self.matrix[i][j]==None:
                return True
            
        return False
    def validate(self):
        i=self.x
        j=self.y
        if self.matrix[i][j]=="rw":
            return self.validate_rw()
        if self.matrix[i][j]=="rb":
            return self.validate_rb()
    def validate_rw(self):
        row=self.x
        col=self.y
        valid_path=list()
        check_mate=list()
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i+1,j)==True:
                valid_path.append((i+1,j))
            else:
                if self.out_of_matrix(i+1,j)==True and self.matrix[i+1][j][len(self.matrix[i+1][j])-1]=='b':
                    check_mate.append((i+1,j))
                break
            i+=1
                  
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i-1,j)==True:
                valid_path.append((i-1,j))
            else:
                if self.out_of_matrix(i-1,j)==True and self.matrix[i-1][j][len(self.matrix[i-1][j])-1]=='b':
                    check_mate.append((i-1,j))
                break
            i-=1
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i,j-1)==True:
                valid_path.append((i,j-1))
            else:
                if self.out_of_matrix(i,j-1)==True and self.matrix[i][j-1][len(self.matrix[i][j-1])-1]=='b':
                    check_mate.append((i,j-1))
                break
            j-=1
        
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i,j+1)==True:
                valid_path.append((i,j+1))
            else:
                if self.out_of_matrix(i,j+1)==True and self.matrix[i][j+1][len(self.matrix[i][j+1])-1]=='b':
                    check_mate.append((i,j+1))
                break
            j+=1           
        return (valid_path,check_mate)
    
    def validate_rb(self):
        row=self.x
        col=self.y
        valid_path=list()
        check_mate=list()
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i+1,j)==True:
                valid_path.append((i+1,j))
            else:
                if self.out_of_matrix(i+1,j)==True and self.matrix[i+1][j][len(self.matrix[i+1][j])-1]=='w':
                    check_mate.append((i+1,j))
                break
            i+=1
                  
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i-1,j)==True:
                valid_path.append((i-1,j))
            else:
                if self.out_of_matrix(i-1,j)==True and self.matrix[i-1][j][len(self.matrix[i-1][j])-1]=='w':
                    check_mate.append((i-1,j))
                break
            i-=1
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i,j-1)==True:
                valid_path.append((i,j-1))
            else:
                if self.out_of_matrix(i,j-1)==True and self.matrix[i][j-1][len(self.matrix[i][j-1])-1]=='w':
                    check_mate.append((i,j-1))
                break
            j-=1
        
        i=row
        j=col
        while i<8 and i>=0 and j<8 and j>=0:
            if self.is_safe(i,j+1)==True:
                valid_path.append((i,j+1))
            else:
                if self.out_of_matrix(i,j+1)==True and self.matrix[i][j+1][len(self.matrix[i][j+1])-1]=='w':
                    check_mate.append((i,j+1))
                break
            j+=1           
        return (valid_path,check_mate)
        
       

class king_validator:
    def __init__(self,matrix,i,j):
        self.matrix=matrix
        self.x=i
        self.y=j
    def out_of_matrix(self,i,j):
        if i>=8 or i<0 or j>=8 or j<0:
            return False
        return True
    def is_safe(self,i,j,):
        if self.out_of_matrix(i,j):
            if self.matrix[i][j]==None:
                return True
            
        return False
            
        
       
    def validate(self):
        i=self.x
        j=self.y
        if self.matrix[i][j]=="kw":
            return self.validate_kw()
        if self.matrix[i][j]=="kb":
            return self.validate_kb()
    def validate_kb(self):
        row=self.x
        col=self.y
        valid_path=list()
        check_mate=list()
        #valid path
        if self.is_safe(row-1,col):#up
                valid_path.append((row-1,col))
        if self.is_safe(row-1,col-1):#diagonal left
                valid_path.append((row-1,col-1))
        if self.is_safe(row-1,col+1):#diagonal right
                valid_path.append((row-1,col+1))
        if self.is_safe(row,col-1):#left
                valid_path.append((row,col-1))
        if self.is_safe(row,col+1):#right
                valid_path.append((row,col+1))
        if self.is_safe(row+1,col+1):#diagonal lower right
                valid_path.append((row+1,col+1))
        if self.is_safe(row+1,col-1):#diagonal lower left
                valid_path.append((row+1,col-1))
        if self.is_safe(row+1,col):#down
                valid_path.append((row+1,col))
        #check_mate
        if self.out_of_matrix(row-1,col)==True and self.matrix[row-1][col]!=None and self.matrix[row-1][col][len(self.matrix[row-1][col])-1]=='w' :#up
                check_mate.append((row-1,col))
        if self.out_of_matrix(row-1,col-1)==True and self.matrix[row-1][col-1]!=None and self.matrix[row-1][col-1][len(self.matrix[row-1][col-1])-1]=='w':#diagonal left
                check_mate.append((row-1,col-1))
        if self.out_of_matrix(row-1,col+1)==True and self.matrix[row-1][col+1]!=None and self.matrix[row-1][col+1][len(self.matrix[row-1][col+1])-1]=='w':#diagonal right
                check_mate.append((row-1,col+1))
        if self.out_of_matrix(row,col-1)==True and self.matrix[row][col-1]!=None and self.matrix[row][col-1][len(self.matrix[row][col-1])-1]=='w':#left
                check_mate.append((row,col-1))
        if self.out_of_matrix(row,col+1)==True and self.matrix[row][col+1]!=None and self.matrix[row][col+1][len(self.matrix[row][col+1])-1]=='w':#right
                check_mate.append((row,col+1))
        if self.out_of_matrix(row+1,col+1)==True and self.matrix[row+1][col+1]!=None and self.matrix[row+1][col+1][len(self.matrix[row+1][col+1])-1]=='w':#diagonal lower right
                check_mate.append((row+1,col+1))
        if self.out_of_matrix(row+1,col-1)==True and self.matrix[row+1][col-1]!=None and self.matrix[row+1][col-1][len(self.matrix[row+1][col-1])-1]=='w':#diagonal lower left
                check_mate.append((row+1,col-1))
        if self.out_of_matrix(row+1,col)==True and self.matrix[row+1][col]!=None and self.matrix[row+1][col][len(self.matrix[row+1][col])-1]=='w':#down
                check_mate.append((row+1,col))
        return (valid_path,check_mate)
        
    def validate_kw(self):
        row=self.x
        col=self.y
        valid_path=list()
        check_mate=list()
        #valid path
        if self.is_safe(row-1,col):#up
                valid_path.append((row-1,col))
        if self.is_safe(row-1,col-1):#diagonal left
                valid_path.append((row-1,col-1))
        if self.is_safe(row-1,col+1):#diagonal right
                valid_path.append((row-1,col+1))
        if self.is_safe(row,col-1):#left
                valid_path.append((row,col-1))
        if self.is_safe(row,col+1):#right
                valid_path.append((row,col+1))
        if self.is_safe(row+1,col+1):#diagonal lower right
                valid_path.append((row+1,col+1))
        if self.is_safe(row+1,col-1):#diagonal lower left
                valid_path.append((row+1,col-1))
        if self.is_safe(row+1,col):#down
                valid_path.append((row+1,col))
        #check_mate
        if self.out_of_matrix(row-1,col)==True and self.matrix[row-1][col]!=None and self.matrix[row-1][col][len(self.matrix[row-1][col])-1]=='b' :#up
                check_mate.append((row-1,col))
        if self.out_of_matrix(row-1,col-1)==True and self.matrix[row-1][col-1]!=None and self.matrix[row-1][col-1][len(self.matrix[row-1][col-1])-1]=='b':#diagonal left
                check_mate.append((row-1,col-1))
        if self.out_of_matrix(row-1,col+1)==True and self.matrix[row-1][col+1]!=None and self.matrix[row-1][col+1][len(self.matrix[row-1][col+1])-1]=='b':#diagonal right
                check_mate.append((row-1,col+1))
        if self.out_of_matrix(row,col-1)==True and self.matrix[row][col-1]!=None and self.matrix[row][col-1][len(self.matrix[row][col-1])-1]=='b':#left
                check_mate.append((row,col-1))
        if self.out_of_matrix(row,col+1)==True and self.matrix[row][col+1]!=None and self.matrix[row][col+1][len(self.matrix[row][col+1])-1]=='b':#right
                check_mate.append((row,col+1))
        if self.out_of_matrix(row+1,col+1)==True and self.matrix[row+1][col+1]!=None and self.matrix[row+1][col+1][len(self.matrix[row+1][col+1])-1]=='b':#diagonal lower right
                check_mate.append((row+1,col+1))
        if self.out_of_matrix(row+1,col-1)==True and self.matrix[row+1][col-1]!=None and self.matrix[row+1][col-1][len(self.matrix[row+1][col-1])-1]=='b':#diagonal lower left
                check_mate.append((row+1,col-1))
        if self.out_of_matrix(row+1,col)==True and self.matrix[row+1][col]!=None and self.matrix[row+1][col][len(self.matrix[row+1][col])-1]=='b':#down
                check_mate.append((row+1,col))
        return (valid_path,check_mate)

class knight_validator:
    def __init__(self,matrix,i,j):
        self.matrix=matrix
        self.x=i
        self.y=j
    def out_of_matrix(self,i,j):
        if i>=8 or i<0 or j>=8 or j<0:
            return False
        return True
    def is_safe(self,i,j,):
        if self.out_of_matrix(i,j):
            if self.matrix[i][j]==None:
                return True
            
        return False
    def validate(self):
        i=self.x
        j=self.y
        if self.matrix[i][j]=="ktw":
            return self.validate_ktw()
        if self.matrix[i][j]=="ktb":
            return self.validate_ktb()
    def validate_ktb(self):
        row=self.x
        col=self.y
        valid_path=list()
        check_mate=list()
        if self.out_of_matrix(row-2,col+1)==True and self.is_safe(row-2,col+1)==True:
            print("dfs")
            valid_path.append((row-2,col+1))
        if self.out_of_matrix(row-2,col-1)==True and self.is_safe(row-2,col-1)==True:
            valid_path.append((row-2,col-1))
        if self.out_of_matrix(row-1,col+2)==True and self.is_safe(row-1,col+2)==True:
            valid_path.append((row-1,col+2))
        if self.out_of_matrix(row-1,col-2)==True and self.is_safe(row-1,col-2)==True:
            valid_path.append((row-1,col-2))
        if self.out_of_matrix(row+1,col+2)==True and self.is_safe(row+1,col+2)==True:
            valid_path.append((row+1,col+2))
        if self.out_of_matrix(row+1,col-2)==True and self.is_safe(row+1,col-2)==True:
            valid_path.append((row+1,col-2))
        if self.out_of_matrix(row+2,col+1)==True and self.is_safe(row+2,col+1)==True:
            valid_path.append((row+2,col+1))
        if self.out_of_matrix(row+2,col-1)==True and self.is_safe(row+2,col-1)==True:
            valid_path.append((row+2,col-1))
        #check mates
        if self.out_of_matrix(row-2,col+1)==True and self.matrix[row-2][col+1]!=None and self.matrix[row-2][col+1][len(self.matrix[row-2][col+1])-1]=='w' :
            check_mate.append((row-2,col+1))
        if self.out_of_matrix(row-2,col-1)==True and self.matrix[row-2][col-1]!=None and self.matrix[row-2][col-1][len(self.matrix[row-2][col-1])-1]=='w' :
            check_mate.append((row-2,col-1))
        if self.out_of_matrix(row-1,col+2)==True and self.matrix[row-1][col+2]!=None and self.matrix[row-1][col+2][len(self.matrix[row-1][col+2])-1]=='w' :
            check_mate.append((row-1,col+2))
        if self.out_of_matrix(row-1,col-2)==True and self.matrix[row-1][col-2]!=None and self.matrix[row-1][col-2][len(self.matrix[row-1][col-2])-1]=='w' :
            check_mate.append((row-1,col-2))
        if self.out_of_matrix(row+1,col+2)==True and self.matrix[row+1][col+2]!=None and self.matrix[row+1][col+2][len(self.matrix[row+1][col+2])-1]=='w' :
            check_mate.append((row+1,col+2))
        if self.out_of_matrix(row+1,col-2)==True and self.matrix[row+1][col-2]!=None and self.matrix[row+1][col-2][len(self.matrix[row+1][col-2])-1]=='w' :
            check_mate.append((row+1,col-2))
        if self.out_of_matrix(row+2,col+1)==True and self.matrix[row+2][col+1]!=None and self.matrix[row+2][col+1][len(self.matrix[row+2][col+1])-1]=='w' :
            check_mate.append((row+2,col+1))
        if self.out_of_matrix(row+2,col-1)==True and self.matrix[row+2][col-1]!=None and self.matrix[row+2][col-1][len(self.matrix[row+2][col-1])-1]=='w' :
            check_mate.append((row+2,col-1))
        return (valid_path,check_mate)
    def validate_ktw(self):
        row=self.x
        col=self.y
        valid_path=list()
        check_mate=list()
        if self.out_of_matrix(row-2,col+1)==True and self.is_safe(row-2,col+1)==True:
            valid_path.append((row-2,col+1))
        if self.out_of_matrix(row-2,col-1)==True and self.is_safe(row-2,col-1)==True:
            valid_path.append((row-2,col-1))
        if self.out_of_matrix(row-1,col+2)==True and self.is_safe(row-1,col+2)==True:
            valid_path.append((row-1,col+2))
        if self.out_of_matrix(row-1,col-2)==True and self.is_safe(row-1,col-2)==True:
            valid_path.append((row-1,col-2))
        if self.out_of_matrix(row+1,col+2)==True and self.is_safe(row+1,col+2)==True:
            valid_path.append((row+1,col+2))
        if self.out_of_matrix(row+1,col-2)==True and self.is_safe(row+1,col-2)==True:
            valid_path.append((row+1,col-2))
        if self.out_of_matrix(row+2,col+1)==True and self.is_safe(row+2,col+1)==True:
            valid_path.append((row+2,col+1))
        if self.out_of_matrix(row+2,col-1)==True and self.is_safe(row+2,col-1)==True:
            valid_path.append((row+2,col-1))
        #check mates
        if self.out_of_matrix(row-2,col+1)==True and self.matrix[row-2][col+1]!=None and self.matrix[row-2][col+1][len(self.matrix[row-2][col+1])-1]=='b' :
            check_mate.append((row-2,col+1))
        if self.out_of_matrix(row-2,col-1)==True and self.matrix[row-2][col-1]!=None and self.matrix[row-2][col-1][len(self.matrix[row-2][col-1])-1]=='b' :
            check_mate.append((row-2,col-1))
        if self.out_of_matrix(row-1,col+2)==True and self.matrix[row-1][col+2]!=None and self.matrix[row-1][col+2][len(self.matrix[row-1][col+2])-1]=='b' :
            check_mate.append((row-1,col+2))
        if self.out_of_matrix(row-1,col-2)==True and self.matrix[row-1][col-2]!=None and self.matrix[row-1][col-2][len(self.matrix[row-1][col-2])-1]=='b' :
            check_mate.append((row-1,col-2))
        if self.out_of_matrix(row+1,col+2)==True and self.matrix[row+1][col+2]!=None and self.matrix[row+1][col+2][len(self.matrix[row+1][col+2])-1]=='b' :
            check_mate.append((row+1,col+2))
        if self.out_of_matrix(row+1,col-2)==True and self.matrix[row+1][col-2]!=None and self.matrix[row+1][col-2][len(self.matrix[row+1][col-2])-1]=='b' :
            check_mate.append((row+1,col-2))
        if self.out_of_matrix(row+2,col+1)==True and self.matrix[row+2][col+1]!=None and self.matrix[row+2][col+1][len(self.matrix[row+2][col+1])-1]=='b' :
            check_mate.append((row+2,col+1))
        if self.out_of_matrix(row+2,col-1)==True and self.matrix[row+2][col-1]!=None and self.matrix[row+2][col-1][len(self.matrix[row+2][col-1])-1]=='b' :
            check_mate.append((row+2,col-1))
        return (valid_path,check_mate)
