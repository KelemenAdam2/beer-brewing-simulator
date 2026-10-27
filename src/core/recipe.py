try:
    from src.core.calculator import BrewCalculator as Bc
except ModuleNotFoundError:
    from calculator import BrewCalculator as Bc

class Recipe:
    def __init__(self):
        # Ingredients
        self.malts = []
        self.hops = []
        self.yeast = None
        self.batch_size = 0.0

        # Final values
        self.og = 1.000
        self.fg = 1.000
        self.srm = 0.0
        self.abv = 0.0
        self.ibu = 0.0

        self.update_final()

    def reset(self):
        self.malts = []
        self.hops = []
        self.yeast = None
        self.batch_size = 0.0

        self.og = 1.000
        self.fg = 1.000
        self.srm = 0.0
        self.abv = 0.0
        self.ibu = 0.0

        self.update_final()

    def add_malt(self, malt, weight):
        self.malts.append((malt, weight))
        self.update_final()

    def add_hop(self, hop, weight, time):
        self.hops.append((hop, weight, time))
        self.update_final()

    def add_yeast(self, yeast):
        self.yeast = yeast
        self.update_final()

    def remove_yeast(self):
        self.yeast = None
        self.update_final()

    def add_water(self, volume):
        self.batch_size += volume
        self.update_final()

    def set_water(self, volume):
        self.batch_size = volume
        self.update_final()

    def update_final(self):
        if self.batch_size <= 0:
            return

        if self.malts:
            self.og = Bc.calc_og_many(self.batch_size, self.malts)
            self.srm = Bc.calc_srm(malts=self.malts)
        else:
            self.og = 1.000
            self.srm = 0.0

        if self.yeast and self.og > 1.0:
            self.fg = Bc.calc_fg(self.og, self.yeast)
            self.abv = Bc.calc_abv(self.og, self.fg)
        else:
            self.fg = self.og
            self.abv = 0.0

        if self.hops and self.og > 1.0:
            self.ibu = Bc.calc_ibu(self.batch_size, self.og, self.hops)
        else:
            self.ibu = 0.0
