board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

user = ["😆", "💩"]
current_user = 0

end = False

def print_board():
    print("{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}".format(*board))

def check_win():
    return same(board[0:3]) or same(board[3:6]) or same(board[6:9]) or same(board[::3]) or same(board[1::3]) or same(board[2::3]) or same(board[::4]) or same(board[2:7:2])

def same(row):
    return all(x == row[0] for x in row)

while(not end):
    print_board()
    index = int(input("You are {}\ninput the index of the board:\n".format(user[current_user])))
    if type(board[index]) is int:
        board[index] = user[current_user]
        if check_win():
            print("{} has won!".format(user[current_user]))
            print_board()
            end = True
        else:
            current_user = 1 if current_user == 0 else 0
    else:
        print("Wrong index please try again")
