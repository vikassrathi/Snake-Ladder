from Controller.PlayerController import PlayerController
from Models.Board import Board
from Models.Dice import Dice


class GameController:

    def Play(self,player,board,pc):
        # print(player)
        dicevalue=Dice.roll()
        print('DiceRolling....',dicevalue)
        if player.get_player_born()==False and  dicevalue==1:
            player.set_player_born(True)

        if player.get_player_born()==False:
            print(f'{player.get_player_name()} Has not started yet')
        else:
            while True:
                pc.update_player_position(player,board,dicevalue)
                pc.print_position(player)
                if dicevalue!=6:
                    break
                else:
                    dicevalue=Dice.roll()
