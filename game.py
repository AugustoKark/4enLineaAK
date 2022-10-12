from exception import *


class Cuatroenlinea():
    row1 = 0    

    def __init__( self):

        self.jugada = 0
        self.player = 0
        self.win = 'No'
        self.col = 0
        self.board = [['-' for _ in range(8)] for _ in range(8)] 
        self.row = 0
        self.token = ''
           
    def set(self, col, letter):
        self.jugada += 1             
        row1 = self.row
        if col > 7:
            
            self.jugada -= 1
            self.col = 0
            self.letter= '-'
            return ExceedTableException()

        if self.jugada== 64:
            return DrawException()


            
        for i in range(8):
            if self.board[i][col] == '-':
                row1 += 1
            else:
                row1 += 0
            
        if row1 == 0:
            self.jugada -= 1
            return MaxFichasException()
        
                
        
        if self.jugada == 1:
            self.token = letter
        
        if self.jugada % 2 == 0:
           self.player = 'Player B'
           
        else:
            self.player = 'Player A'

        if self.jugada %2==0 and self.token == letter: 
            self.jugada -= 1
            raise   SamePlayerException 
            

        if self.win =='Yes':
            raise GameOverException()
        
        
            

        self.board[row1-1][col] = letter
        self.verify_hor(letter)
        self.verify_ver(letter)
        self.verify_incl1()
        self.verify_incl2()
        #self.vertical(letter)

   


        
    
        
    def verify_hor(self,letter):

        for roww in range (8):
            for column in range (5):

                
                if self.board[roww][column] == self.board[roww][column+1] == self.board[roww][column+2] == self.board[roww][column+3]  == 'X':
                    self.win ='Yes'
                
                if self.board[roww][column] == self.board[roww][column+1] == self.board[roww][column+2] == self.board[roww][column+3]  == '0':
                    self.win ='Yes'
    
    #def vertical(self,letter):
    #    for column in range (8):
    #        for roww in range (6):
    #            if self.board[roww][column-1] == self.board[roww+1][column-1] == self.board[roww+2][column-1] == self.board[roww+3][column-1]  == 'X':
    #                self.win ='Yes'

#                if self.board[roww][column] == self.board[roww+1][column] == self.board[roww+2][column] == self.board[roww+3][column]  == '0':
#                    self.win ='Yes'


    def verify_ver(self,letter):
        for column in range (8):
            for roww in range (5):
            
                if self.board[roww][column-1] == self.board[roww+1][column-1] == self.board[roww+2][column-1] == self.board[roww+3][column-1]  == 'X':
                    self.win ='Yes'
                
                if self.board[roww][column-1] == self.board[roww+1][column-1] == self.board[roww+2][column-1] == self.board[roww+3][column-1]  == '0':
                    self.win ='Yes'

    def verify_incl1(self):
        for roww in range (5):
            for column in range (8):
                
                
               
                if self.board[roww][column] == self.board[roww+1][column-1] == self.board[roww+2][column-2] == self.board[roww+3][column-3]  == 'X':
                    self.win ='Yes'
                
                if self.board[roww][column] == self.board[roww+1][column-1] == self.board[roww+2][column-2] == self.board[roww+3][column-3]  == '0':
                    self.win ='Yes' 
        
    def verify_incl2(self):
        for roww in range (5):
            for column in range (5):

                if self.board[roww][column] == self.board[roww+1][column+1] == self.board[roww+2][column+2] == self.board[roww+3][column+3]  == 'X':
                    self.win ='Yes' 

                if self.board[roww][column] == self.board[roww+1][column+1] == self.board[roww+2][column+2] == self.board[roww+3][column+3]  == '0':
                    self.win ='Yes'

        

