import numpy as np
class TicBoard:
    def __init__(self):
        self.board = np.full((3,3), -1) 
        self.val = -1
    def update(self, pos, val):
        if self.get(pos) == -1 and self.checkFilled() == False:
            self.board[pos[0]][pos[1]] = val
            return True
        else:
            return False
    def get(self, pos):
        return self.board[pos[0]][pos[1]]
    def checkFilled(self):
        for r in range(3):
            if(self.get((r,0)) != -1): 
                if((self.get((r, 0)) == self.get((r, 1)) and self.get((r, 1)) == self.get((r, 2)))): 
                    self.val = self.get((r,0))
                    return True
            if(self.get((0,r)) != -1): 
                if((self.get((0, r)) == self.get((1, r)) and self.get((1, r)) == self.get((2, r)))):
                    self.val = self.get((0,r))
                    return True
            if(self.get((1,1)) != -1):
                if((self.get((0, 0)) == self.get((1, 1)) and self.get((1, 1)) == self.get((2, 2))) or
                    (self.get((0, 2)) == self.get((1, 1)) and self.get((1, 1)) == self.get((2, 0)))):
                    self.val == self.get((1,1))
                    return True
        return False
class BigTicBoard():
    def __init__(self):
        self.board = np.ndarray((3,3), TicBoard)
        for x in range(3):
            for y in range(3):
                self.board[x][y] = TicBoard()
    def __str__(self):
        rep = ""
        for i in range(3):
            rep += "\n"
            for k in range(3):
                rep += "\n"
                for j in range(3):
                    rep += str(self.board[i][j].board[k]) + " "
        return rep
    def update(self, pos, val):
        return self.board[pos[0]][pos[1]].update(pos[2:4], val)
    def get2(self, pos):
        return self.board[pos[0]][pos[1]].get(pos[2:4])
    def get(self, pos):
        return self.board[pos[0]][pos[1]].val
class Player:
    tic = BigTicBoard()
    log = []
    def __init__(self, type):
        if(type == "x"):
            self.type = 1
        else:
            self.type = 0
    def checkWin():
        for r in range(3):
            if(Player.tic.get((r,0)) != -1): 
                if((Player.tic.get((r, 0)) == Player.tic.get((r, 1)) and Player.tic.get((r, 1)) == Player.tic.get((r, 2)))):
                    return Player.tic.get((r, 0))
            if(Player.tic.get((0,r)) != -1): 
                if((Player.tic.get((0, r)) == Player.tic.get((1, r)) and Player.tic.get((1, r)) == Player.tic.get((2, r)))):
                    return Player.tic.get()
            if(Player.tic.get((1,1)) != -1):
                if((Player.tic.get((0, 0)) == Player.tic.get((1, 1)) and Player.tic.get((1, 1)) == Player.tic.get((2, 2))) or
                    (Player.tic.get((0, 2)) == Player.tic.get((1, 1)) and Player.tic.get((1, 1)) == Player.tic.get((2, 0)))):
                    return True
        return False
    def availableMoves(self):
        moves = []
        if len(Player.log) == 0 or Player.tic.get(Player.log[-1][2:4]) != -1:
            with np.nditer(Player.tic.board, flags = ['multi_index', 'refs_ok']) as bI:
                for i in bI:
                    with np.nditer(i.tolist().board, flags = ['multi_index']) as bII:     
                        for j in bII:
                            pos = (bI.multi_index[0], bI.multi_index[1], bII.multi_index[0], bII.multi_index[1])
                            if(Player.tic.get2(pos) == -1):
                                moves.append(pos)
        elif Player.checkWin():
            pass
        else:
            pastSq = Player.log[-1][2:4]
            with np.nditer(Player.tic.board[pastSq[0]][pastSq[1]].board, flags = ['multi_index']) as sq:
                for i in sq:
                    pos = (pastSq[0], pastSq[1], sq.multi_index[0], sq.multi_index[1])
                    if(Player.tic.get2(pos) == -1):
                        moves.append(pos)
        return moves
    def move(self, pos):
        if len(Player.log) == 0 or (pos in self.availableMoves() and Player.log[-1][4] != self.type):
            Player.tic.update(pos, self.type)
            Player.log.append((pos[0],pos[1],pos[2],pos[3],self.type))
            print(Player.tic)
        else:
            print("bad move")
x = Player("x")
o = Player("o")
x.move((1, 0, 2, 1))
x.move((2,0,2,1))
print(o.availableMoves())