import room
from player import Player

fixed_map_6x6 = [
    ["P", "B", "*", ".", ".", "*"],
    [".", "C", ".", "*", "*", "."],
    [".", "*", ".", ".", "B", "."],
    [".", ".", ".", "M", "B", "H"],
    ["H", "*", ".", "*", ".", "."],
    ["B", "C", "M", ".", ".", "T"]
]

default_map = [
    ["P", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "T"]
]

def main():
    answer = input("Welcome to the intresting maze game! Reach to the terminus within 25 steps. Are you ready?(Y/N)")
    if answer != 'Y':
        print("Coward! The game has started! Just enjoy it!")
    else:
        print("Now the game starts, enjoy it!")
    i = 1
    player = Player()
    is_win = False
    is_lose = False
    while i < 21:
        room.display_map(default_map)
        while 1:
            order = input(f"Step {i}: Choose a direction:(N/W/E/S/STATUS/GRIP)")
            if order != 'N' and order != 'S' and order != 'E' and order != 'W' and order != 'STATUS' and order != 'GRIP':
                print("Invalid direction.")
            elif order == 'N':
                if player.x == 0:
                    print("You have reached the northernmost.")
                else:
                    if player.move(player.x-1,player.y, fixed_map_6x6,default_map) == True:
                        if fixed_map_6x6[player.x][player.y] == 'T':
                            is_win = True    
                        else:
                            if player.is_out_of_health():
                                is_lose = True 
                            else:
                                fixed_map_6x6[player.x+1][player.y] = '.'
                                fixed_map_6x6[player.x][player.y] = 'P'
                                default_map[player.x+1][player.y] = '.'
                                default_map[player.x][player.y] = 'P'
                    else:
                        default_map[player.x-1][player.y] = '*'
                    break
            elif order == 'S':
                if player.x == 5:
                    print("You have reached the southernmost.")
                else:
                    if player.move(player.x+1, player.y, fixed_map_6x6,default_map) == True:
                        if fixed_map_6x6[player.x][player.y] == 'T':
                            is_win = True    
                        else:
                            if player.is_out_of_health():
                                is_lose = True 
                            else:
                                fixed_map_6x6[player.x-1][player.y] = '.'
                                fixed_map_6x6[player.x][player.y] = 'P'
                                default_map[player.x-1][player.y] = '.'
                                default_map[player.x][player.y] = 'P'
                    else:
                        default_map[player.x+1][player.y] = '*'
                    break
            elif order == 'E':
                if player.y == 5:
                    print("You have reached the easternmost.")
                else:
                    if player.move(player.x, player.y+1, fixed_map_6x6,default_map) == True:
                        if fixed_map_6x6[player.x][player.y] == 'T':
                            is_win = True    
                        else:
                            if player.is_out_of_health():
                                is_lose = True 
                            else:
                                fixed_map_6x6[player.x][player.y-1] = '.'
                                fixed_map_6x6[player.x][player.y] = 'P'
                                default_map[player.x][player.y-1] = '.'
                                default_map[player.x][player.y] = 'P'
                    else:
                        default_map[player.x][player.y+1] = '*'
                    break
            elif order == 'W':
                if player.y == 0:
                    print("You have reached the westernmost.")
                else:
                    if player.move(player.x, player.y-1, fixed_map_6x6,default_map) == True:
                        if fixed_map_6x6[player.x][player.y-1] == 'T':
                            is_win = True    
                        else:
                            if player.is_out_of_health():
                                is_lose = True 
                            else:
                                fixed_map_6x6[player.x][player.y+1] = '.'
                                fixed_map_6x6[player.x][player.y] = 'P'
                                default_map[player.x][player.y+1] = '.'
                                default_map[player.x][player.y] = 'P'
                    else:
                        default_map[player.x][player.y-1] = '*'
                    break
            elif order == 'STATUS':
                player.display_status()
            else:
                room.display_map(default_map)
        if is_lose:
            print("Game over! You lose!")
            break
        if is_win:
            print("Congradulations! You win!")
            break
        i += 1
    if i==21:
        print("Game over! You lose!")



if __name__ == '__main__':
    main()
