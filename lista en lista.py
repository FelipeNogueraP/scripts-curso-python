# v1

row = []

for i in range(8):
    row.append(WHITE_PAWN)
# esta genera error porque white_pawn no se ha definido


# v2

row = [WHITE_PAWN for i in range(8)]

# igual genera error, white_pawn no definido

# v3

squares = [x ** 2 for x in range(10)]

twos = [2 ** i for i in range(8)]

odds = [x for x in squares if x % 2 != 0]
