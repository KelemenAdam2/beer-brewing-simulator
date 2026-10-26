from calculator import BrewCalculator as Bc

class Recipe:
    def __init__(self):
        # Ingredients
        self.malts = []
        self.hops = []
        self.yeast = None
        self.batch_size = 0

        # Final values
        self.og = 0
        self.fg = 0
        self.srm = 0
        self.abv = 0
        self.ibu = 0

        self.update_final()

    def add_malt(self, malt, weight):
        self.malts.append((malt,weight))
        self.update_final()

    def add_hop(self, hop, weight, time):
        self.malts.append((hop, weight, time))
        self.update_final()

    def add_yeast(self, yeast):
        self.yeast = yeast
        self.update_final()

    def add_water(self, volume):
        self.batch_size += volume
        self.update_final()

    def update_final(self):
        self.og = Bc.calc_og_many(self, self.batch_size, self.malts)
        self.srm = Bc.calc_srm(self, malts=self.malts)
        self.fg = Bc.calc_fg(self, self.og, self.yeast)
        self.abv = Bc.calc_abv(self, self.og, self.fg)
        self.ibu = Bc.calc_ibu(self, self.batch_size, self.og, self.hops)
