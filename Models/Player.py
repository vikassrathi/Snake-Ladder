


class Player:
    def __init__(self):
        self.player_id=0
        self.player_name=0
        self.player_position=0
        self.born=False


    def set_player_id(self,player_id):
        self.player_id=player_id

    def set_player_position(self,player_position):
        self.player_position=player_position
    def set_player_name(self,player_name):
        self.player_name=player_name

    def get_player_position(self):
        return self.player_position
    def get_player_name(self):
        return self.player_name
    def get_player_id(self):
        return self.player_id

    def has_won(self):
        return self.player_position == 100

    def set_player_born(self,boolean_value):
        self.born=boolean_value

    def get_player_born(self):
        return self.born
