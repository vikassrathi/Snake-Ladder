from Models.Player import Player


class PlayerController:

    def __init__(self):
        self.last_three_moves = [0, 0, 0]




    def update_player_position(self,player,board,dicevalue):
        self.last_three_moves.pop(0)
        self.last_three_moves.append(dicevalue)

        if self.last_three_moves==[6,6,6]:
            player.set_player_position(0)
            player.set_player_born(False)
            return
        new_pos=player.get_player_position()+dicevalue
        if new_pos>100:
            return
        else:
            if new_pos in board.get_snake_position():
                print(f'{player.get_player_name()} has caught by snake its current position was {new_pos}')
                new_pos=board.snake_position[new_pos]
                print(f'{player.get_player_name()} has caught by snake its new position is {new_pos}')
            elif new_pos in board.get_ladder_position():
                print(f'{player.get_player_name()} has climb up the ladder its current position was {new_pos}')
                new_pos=board.ladder_position[new_pos]
                print(f'{player.get_player_name()} has climb up the ladder its new position is {new_pos}')
        player.set_player_position(new_pos)


    def print_position(self,player):
        print(f'{player.get_player_name()} has now position at {player.get_player_position()}')
    