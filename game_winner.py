#Two players are playing a game where white or black pieces are represented by a string, colors.
#The game rules are as follows:
#• Wendy moves first and then they take alternate turns.
# • With each move, Wendy may remove a white piece that has adjacent white pieces on both sides.
# • Likewise, with each move, Bob may remove any black piece that has adjacent black pieces on both sides.
# • After a piece is removed, the string is reduced in size by one piece. For instance, removing 'Y' from 'XYZ' results in 'XZ'.
# • When a player can no longer move, they have lost the game.


def gameWinner(colors):
    wendy = 0
    bob = 0

    for i in range(1, len(colors)-1):
        if colors[i] == "w" and colors[i-1] == "w" and colors[i+1] == "w":
            wendy+=1
        elif colors[i] == "b" and colors[i-1] == "b" and colors[i+1] == "b":
            bob+=1
    
    if wendy > bob:
        print("Wendy")
    elif wendy == bob :
        print("tie")
    else:
        print("Bob")






colors = "wbb"
gameWinner(colors)