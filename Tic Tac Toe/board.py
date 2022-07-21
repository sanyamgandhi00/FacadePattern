from cell import Cell

class Board:
    def __init__(self):
        l = []
        for i in range(3):
            ll = []
            for j in range(3):
                ll.append(Cell())
            l.append(ll)
        
        self.cells = l 


    def rowCrossed(board):
        for i in range(3):
            if (board[i][0].mark == board[i][1].mark and board[i][1].mark == board[i][2].mark and board[i][0].mark != '-'):
                return True 
        return False 

    def columnCrossed(board):
        for i in range(3) :
            if (board[0][i].mark == board[1][i].mark and board[1][i].mark == board[2][i].mark and board[0][i].mark != '-') :
                return True , board[0][i].mark
        return False

    def diagonalCrossed(self):
        board = self.board
        if (board[0][0].mark == board[1][1].mark and  board[1][1].mark == board[2][2].mark and board[0][0].mark != '-'):
            return True 
        if (board[0][2].mark == board[1][1].mark and board[1][1].mark == board[2][0].mark and board[0][2].mark != '-'):
            return True 
        return False 
    
    def resultAnalyzer(self):
        cnt  = 0 
        for  i in range(3):
            for j in range(3) :
                if(self.board[i][j].mark!='-'):
                    cnt+=1 
        rowCheck = self.rowCrossed(self.board)
        colCheck = self.columnCrossed(self.board)
        diagCheck = self.diagonalCrossed(self.board)

        if rowCheck :
            return "End"
        if colCheck :
            return "End" 
        if diagCheck:
            return "End"

        if cnt == 9 : 
            return "Draw"
        
        return "Continue"



    def printBoard(self):
        l = []
        for i in range(3):
            for j in range(3):
                print(self.board[i][j].mark , end = " ")
                l.append(self.board[i][j].mark)
            print()
        return l 


board1 = Board()

# board1.board[0][0].mark = 'X'

# board1.board[0][1].mark = 'X'

# board1.board[0][2].mark = 'X'

board1.printBoard()

print(board1.resultAnalyzer()[0])









