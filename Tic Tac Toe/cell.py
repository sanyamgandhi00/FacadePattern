

class Cell:
    def __init__(self):
        self.mark = '-' 

    def isMarked(self) -> bool :
        if self.mark == 'X' or self.mark =='O' :
            return True
        return False 


