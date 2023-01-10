EMPTY = "-"
PAWN = "PEON"
ROOK = "TORRE"
KNIGHT = "CABALLO"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

board[4][2] = KNIGHT
board[3][4] = PAWN

print(board)

# el primer [] es la fila y el segundo [] es la columna
