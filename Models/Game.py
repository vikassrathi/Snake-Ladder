import itertools


class Game:

    def __init__(self,players):
        self.no_of_players=len(players)
        self.players=itertools.cycle(players)
        self.mutable_players=itertools.cycle(players)
    def has_won(self):
        for i in range(self.no_of_players):
            player=next(self.mutable_players)
            if player.has_won():
                print(f'Wohooooooooo {player.get_player_name()} has won')
                return True
        return False
    def next_player(self):
        return next(self.players)


