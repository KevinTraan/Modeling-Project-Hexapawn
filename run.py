from nnf import Var
from lib204 import Encoding
from nnf import NNF, true, false
from nnf.operators import iff

"""The following two functions were given explicitly by the professor
"""
def implication(l, r):
    return l.negate() | r

def neg(f):
    return f.negate()

"""returns a logical statement that is that equivalent to the following english statement:
'only one of the variables can be true, and one of the variables must be true'
"""
def xor14(a, b, c, d, e, f, g, h, i, j, k, l, m, n):
    conA = (a & ~b & ~c & ~d & ~e & ~f & ~g & ~h & ~i & ~j & ~k & ~l & ~m & ~n)
    conB = (~a & b & ~c & ~d & ~e & ~f & ~g & ~h & ~i & ~j & ~k & ~l & ~m & ~n)
    conC = (~a & ~b & c & ~d & ~e & ~f & ~g & ~h & ~i & ~j & ~k & ~l & ~m & ~n)
    conD = (~a & ~b & ~c & d & ~e & ~f & ~g & ~h & ~i & ~j & ~k & ~l & ~m & ~n)
    conE = (~a & ~b & ~c & ~d & e & ~f & ~g & ~h & ~i & ~j & ~k & ~l & ~m & ~n)
    conF = (~a & ~b & ~c & ~d & ~e & f & ~g & ~h & ~i & ~j & ~k & ~l & ~m & ~n)
    conG = (~a & ~b & ~c & ~d & ~e & ~f & g & ~h & ~i & ~j & ~k & ~l & ~m & ~n)
    conH = (~a & ~b & ~c & ~d & ~e & ~f & ~g & h & ~i & ~j & ~k & ~l & ~m & ~n)
    conI = (~a & ~b & ~c & ~d & ~e & ~f & ~g & ~h & i & ~j & ~k & ~l & ~m & ~n)
    conJ = (~a & ~b & ~c & ~d & ~e & ~f & ~g & ~h & ~i & j & ~k & ~l & ~m & ~n)
    conK = (~a & ~b & ~c & ~d & ~e & ~f & ~g & ~h & ~i & ~j & k & ~l & ~m & ~n)
    conL = (~a & ~b & ~c & ~d & ~e & ~f & ~g & ~h & ~i & ~j & ~k & l & ~m & ~n)
    conM = (~a & ~b & ~c & ~d & ~e & ~f & ~g & ~h & ~i & ~j & ~k & ~l & m & ~n)
    conN = (~a & ~b & ~c & ~d & ~e & ~f & ~g & ~h & ~i & ~j & ~k & ~l & ~m & n)
    return conA | conB | conC | conD | conE | conF | conG | conH | conI | conJ | conK | conL | conM | conN

NNF.__rshift__ = implication
NNF.__invert__ = neg

"""Counts and returns the number of white pawns on the given board
"""
def count_white_pawns(board):
    counter = 0
    for i in range(3):
        for j in range(3):
            if(board[i][j] == 'w'):
                counter += 1
    return counter

"""Counts and returns the number of black pawns on the given board
"""
def count_black_pawns(board):
    counter = 0
    for i in range(3):
        for j in range(3):
            if(board[i][j] == 'b'):
                counter += 1
    return counter

"""Counts and returns the number of black pawns that are currently blocked (cannot move) by white pawns
"""
def count_black_pawns_blocked_by_white(board):
    counter = 0
    for i in range(3):
        for j in range(3):
            if((board[i][j] == 'b') and (board[i+1][j] == 'w')):
                counter += 1
    return counter

"""Counts and returns the number of black pawns that are currently blocked (cannot move) by black pawns
"""
def count_black_pawns_blocked_by_black(board):
    counter = 0
    for i in range(3):
        for j in range(3):
            if((board[i][j] == 'b') and (board[i+1][j] == 'b')):
                counter += 1
    return counter

"""Counts and returns the number of black pawns that are currently blocked (cannot move) in total
"""
def count_black_pawns_blocked(board):
    counter = 0
    for i in range(3):
        for j in range(3):
            if((board[i][j] == 'b') and (board[i+1][j] in ('w' or 'b'))):
                counter += 1
    return counter

"""Prints T.solve() in a sorted manner (for debug purposes)
"""
def print_sol(T):
    T = str(T)
    T = list(T.split(","))
    T[0] = " " + T[0][1::]
    T[len(T)-1] = T[len(T)-1][:-1]
    for i in range(len(T)):
        temp = T[i]
        if temp[3:5] == "00":
            print(temp)
    print()
    for i in range(len(T)):
        temp = T[i]
        if temp[3:5] == "01":
            print(temp)
    print()
    for i in range(len(T)):
        temp = T[i]
        if temp[3:5] == "02":
            print(temp)
    print()
    for i in range(len(T)):
        temp = T[i]
        if temp[3:5] == "10":
            print(temp)
    print()
    for i in range(len(T)):
        temp = T[i]
        if temp[3:5] == "11":
            print(temp)
    print()
    for i in range(len(T)):
        temp = T[i]
        if temp[3:5] == "12":
            print(temp)
    print()
    for i in range(len(T)):
        temp = T[i]
        if temp[3:5] == "20":
            print(temp)
    print()
    for i in range(len(T)):
        temp = T[i]
        if temp[3:5] == "21":
            print(temp)
    print()
    for i in range(len(T)):
        temp = T[i]
        if temp[3:5] == "22":
            print(temp)
    print()

"""Prints a formatted interpretation of the board.
"""
def show_board(board):
    for i in range(3):
        print(" | ",end="")
        for j in range(3):
            if(board[i][j] == b):
                print("b",end="")
            elif(board[i][j] == w):
                print("w",end="")
            else:
                print("o",end="")
            print(" | ",end="")
        print()
    return

# The board position: b = Black, w = White, o = empty **These variables are overwritten after the board is printed
# The "board" array below can be changed to modify the given board when debugging
b = 'b'
w = 'w'
o = 'o'
board = [
    [b,b,b],
    [o,o,o],
    [w,w,w]
]


#The following function is for user input and overwrites the board state; comment this out when you are debugging.
#Begin U\In
"""Lets the user input the board state, one square at a time
"""
def user_input_board():
    print("In the next 9 lines, the program will ask you for what pieces should go on each square.")
    print("Simply denote a black pawn as b, a white pawn as w, & an empty square as any other character.")
    print("Example: Enter top-left piece: b")
    print("This would insert a black pawn on the top-left square")
    print("")

    new_board = [
        [input("Enter top-left piece: "), input("Enter top piece: "), input("Enter top-right piece: ")],
        [input("Enter left piece: "), input("Enter centre piece: "), input("Enter right piece: ")],
        [input("Enter bottom-left piece: "), input("Enter bottom piece: "), input("Enter bottom-right piece: ")]
    ]

    return new_board
board = user_input_board()
#End U\In

#Shows board
print("     Board")
print(" -------------")
show_board(board)
print(" -------------\n")

"""These are all 2D arrays of propositional variables.  Please note that we use a (y, x) coordinate system.
w[y][x]: denotes that there is a white pawn at the given square
b[y][x]: denotes that there is a black pawn at the given square
l[y][x]: denotes that a white pawn at the given square can capture to the left
f[y][x]: denotes that a white pawn at the given square can move forwards
r[y][x]: denotes that a white pawn at the given square can capture to the right
"""
w = [
    [Var('w00'),Var('w01'),Var('w02')],
    [Var('w10'),Var('w11'),Var('w12')],
    [Var('w20'),Var('w21'),Var('w22')]]

b = [
    [Var('b00'),Var('b01'),Var('b02')],
    [Var('b10'),Var('b11'),Var('b12')],
    [Var('b20'),Var('b21'),Var('b22')]]

l = [
    [Var('l00'),Var('l01'),Var('l02')],
    [Var('l10'),Var('l11'),Var('l12')],
    [Var('l20'),Var('l21'),Var('l22')]]

f = [
    [Var('f00'),Var('f01'),Var('f02')],
    [Var('f10'),Var('f11'),Var('f12')],
    [Var('f20'),Var('f21'),Var('f22')]]

r = [
    [Var('r00'),Var('r01'),Var('r02')],
    [Var('r10'),Var('r11'),Var('r12')],
    [Var('r20'),Var('r21'),Var('r22')]]

"""Constrains the theory to have the board positions given by the user
"""
def board_to_constraint(E):
    for i in range(3):
        for j in range(3):
            if(board[i][j] == 'w'):
                E.add_constraint(w[i][j])
                E.add_constraint(~b[i][j])
            elif(board[i][j] == 'b'):
                E.add_constraint(~w[i][j])
                E.add_constraint(b[i][j])
            else:
                E.add_constraint(~w[i][j])
                E.add_constraint(~b[i][j])

# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
"""This theory finds if there is a move that white can make that will win them the game
"""
def example_theory():
    E = Encoding()
    board_to_constraint(E)
    disj = false
    #reach end of board moving forward
    disj = disj | (w[1][0] & ~b[0][0]) | (w[1][1] & ~b[0][1]) | (w[1][2] & ~b[0][2])
    #end of board by capture
    disj = disj | (w[1][0] & b[0][1]) | (w[1][1] & b[0][0]) | (w[1][1] & b[0][2]) | (w[1][2] & b[0][1])

    #1 black pawn left
    if(count_black_pawns(board) == 1):
        #win by blocking last pawn
        for j in range(3):
            disj = disj | (b[0][j] & w[2][j] & ~b[1][j] & ~w[1][j]) 
        #win by capturing last pawn
        for i in range(3):
            #left column can capture right
            disj = disj | (w[i][0] & b[i-1][1])
            #right column can capture left
            disj = disj | (w[i][2] & b[i-1][1])
            #middle column can capture left or right
            disj = disj | (w[i][1] & (b[i-1][0] | b[i-1][2]))
        
    #2 black pawns left
    if(count_black_pawns(board) == 2):
        #win by blocking both of blacks pawns
        if(count_black_pawns_blocked_by_white(board) == 1):
            for j in range(3):
                disj = disj | (b[0][j] & w[2][j] & ~b[1][j] & ~w[1][j]) 
        #win by capturing pawn into blocking last pawn
        #left
        disj = disj | (b[0][0] & b[1][0] & w[2][1])
        #right
        disj = disj | (b[0][2] & b[1][2] & w[2][1])
        #middle
        disj = disj | ((b[0][1] & b[0][1]) & (w[2][0] | w[2][2]))

    #3 black pawns left
    if(count_black_pawns(board) == 3):
    #win by blocking all three of blacks pawns
        #black pawns only blocked by white pawns
        if((count_black_pawns_blocked_by_white(board) == 2) and (count_black_pawns_blocked(board) == 2)):
            for j in range(3):
                disj = disj | (b[0][j] & w[2][j] & ~b[1][j] & ~w[1][j]) 
        #black pawns blocked by white and black pawns
        if((count_black_pawns_blocked_by_white(board) == 1) and (count_black_pawns_blocked(board) == 1)):
            for j in range(3):
                    disj = disj | (b[0][j] & w[2][j] & ~b[1][j] & ~w[1][j])
    E.add_constraint(disj)
    return E

"""This theory finds the number of moves that white can make
"""
def possible_moves_theory():
    E = Encoding()
    board_to_constraint(E)
    
    E.add_constraint(xor14(f[1][0], f[1][1], f[1][2], f[2][0], f[2][1], f[2][2], \
                           r[1][0], r[1][1], r[2][0], r[2][1], \
                           l[1][1], l[1][2], l[2][1], l[2][2]))

    for i in range(1, 3):
        for j in range(3):
            E.add_constraint((b[i-1][j] | w[i-1][j]) >> ~f[i][j])
            E.add_constraint(~w[i][j] >> ~f[i][j])
            if j > 0:
                E.add_constraint(~b[i-1][j-1] >> ~l[i][j])
                E.add_constraint(~w[i][j] >> ~l[i][j])
            if j < 2:
                E.add_constraint(~b[i-1][j+1] >> ~r[i][j])
                E.add_constraint(~w[i][j] >> ~r[i][j])
    return E

"""This returns a string that contains all and any errors with the given board
"""
def error_logger(board):
    error_message = ""
    if(count_white_pawns(board) > 3):
        error_message = error_message + \
                "- a maximum of 3 white pawns are allowed, you have " + \
                str(count_white_pawns(board)) + \
                "\n"
    
    if(count_black_pawns(board) > 3):
        error_message = error_message + \
                "- a maximum of 3 black pawns are allowed, you have " + \
                str(count_black_pawns(board)) + \
                "\n"
    
    if(board[0][0] == 'w' or board[0][1] == 'w' or board[0][2] == 'w'):
        error_message = error_message + \
                "- you are not allowed white pawns in black's first rank, you have at least one white pawn breaking this rule" + \
                "\n"
    
    if(board[2][0] == 'b' or board[2][1] == 'b' or board[2][2] == 'b'):
        error_message = error_message + \
                "- you are not allowed black pawns in white's first rank, you have at least one black pawn breaking this rule" + \
                "\n"
    
    return error_message

if __name__ == "__main__":
    error = error_logger(board)
    
    if error == "":
        T = example_theory()
        M = possible_moves_theory()

        print("Satisfiable: %s" % T.is_satisfiable())
        print("")

        print("With the given board state, there are %d moves for white." % M.count_solutions())

        if not (M.solve() == None):
            print("Here is one of the possible solutions: %s" % M.solve())
        print("")

        if(T.is_satisfiable()):
            print("White CAN win on their next move")
        else:
            print("White CANNOT win on their next move")
        print("")

        #Debugging function for example_theory()
        #print_sol(T.solve())
    else:
        print("Please resolve the following errors and rerun the program:")
        print(error)
