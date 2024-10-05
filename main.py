import time

from Controller.BoardController import BoardController
from Controller.GameController import GameController
from Controller.PlayerController import PlayerController
from Models.Board import Board
from Models.Game import Game
from Models.Player import Player

if __name__ == '__main__':
    gc=GameController()
    pc=PlayerController()
    bc=BoardController()
    # no_of_player=int(input('Enter Number Of Players'))
    # player_names=[name for name in input('PLayer names').split()]
    no_of_player=2
    player_names=['Player1','Player2']
    players=[]
    board = bc.set_board_object()
    bc.print_board()

    for i in range(no_of_player):
        player=Player()
        player.set_player_position(0)
        player.set_player_id(f'G00{i}')
        player.set_player_name(player_names[i])
        players.append(player)
    game=Game(players)

    while not game.has_won():
        player=game.next_player()
        gc.Play(player,board,pc)
        time.sleep(2)
