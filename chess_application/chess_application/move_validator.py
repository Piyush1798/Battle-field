from pawn_validate import pawn_validator,rook_validator,bishop_validator,king_validator,knight_validator,queen_validator


class move_validator:
    def validate(matrix,i,j):
        if matrix[i][j][0]=="p":
            obj=pawn_validator(matrix,i,j)
            return obj.validate()
        if matrix[i][j][0]=="r":
            obj=rook_validator(matrix,i,j)
            return obj.validate()
        if matrix[i][j][0]=="b":
            obj=bishop_validator(matrix,i,j)
            return obj.validate()
        if matrix[i][j][0]=="k" and matrix[i][j][1]=="t":
            obj=knight_validator(matrix,i,j)
            return obj.validate()
        if matrix[i][j][0]=="k":
            obj=king_validator(matrix,i,j)
            return obj.validate()
        
        if matrix[i][j][0]=="q":
            obj=queen_validator(matrix,i,j)
            return obj.validate()



    
        


