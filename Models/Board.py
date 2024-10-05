

import random

class Board:
    def __init__(self):
        self.size=100
        self.snake_position={}
        self.ladder_position={}

    def set_snake_position(self):
        while len(self.snake_position)!=5:
            position_start=random.randint(5,98)
            position_end=random.randint(5,position_start-1)
            if position_start not in self.snake_position.keys():
                self.snake_position[position_start]=position_end


    def set_ladder_position(self):
        while len(self.ladder_position)!=7:
            position_start=random.randint(5,70)
            position_end=random.randint(position_start+5,98)
            if position_start not in self.snake_position.keys() and position_start not in self.ladder_position.keys():
                self.ladder_position[position_start]=position_end

    def get_snake_position(self):
        return self.snake_position

    def get_ladder_position(self):
        return self.ladder_position
