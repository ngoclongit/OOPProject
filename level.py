from characters import Pig
from polygon import Polygon


class Level():
    def __init__(self, pigs, columns, beams, space):
        self.pigs = pigs
        self.columns = columns
        self.beams = beams
        self.space = space
        self.number = 0
        self.number_of_birds = 4
        # lower limit
        self.one_star = 30000
        self.two_star = 40000
        self.three_star = 60000
        self.bool_space = False



    def build_0(self):
        """level 0"""
        pig1 = Pig(980, 100, self.space)
        pig2 = Pig(985, 182, self.space)
        self.pigs.append(pig1)
        self.pigs.append(pig2)
        p = (950, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1010, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (980, 150)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (950, 200)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1010, 200)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (980, 240)
        self.beams.append(Polygon(p, 85, 20, self.space))
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8
        self.one_star = 30000
        self.two_star = 40000
        self.three_star = 60000

    def build_1(self):
        """level 1"""
        pig = Pig(1000, 100, self.space)
        self.pigs.append(pig)
        p = (900, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (850, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (850, 150)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1050, 150)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1105, 210)
        self.beams.append(Polygon(p, 85, 20, self.space))
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8

    def build_2(self):
        """level 2"""
        pig1 = Pig(880, 180, self.space)
        self.pigs.append(pig1)
        pig2 = Pig(1000, 230, self.space)
        self.pigs.append(pig2)
        p = (880, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (880, 150)
        self.beams.append(Polygon(p, 85, 20, self.space))
        p = (1000, 80)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1000, 180)
        self.columns.append(Polygon(p, 20, 85, self.space))
        p = (1000, 210)
        self.beams.append(Polygon(p, 85, 20, self.space))
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8

    