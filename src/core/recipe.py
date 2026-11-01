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
        self.current_water = 0.0

        # Final values
        self.og = 1.000
        self.fg = 1.000
        self.srm = 0.0
        self.abv = 0.0
        self.ibu = 0.0

        # Values at given time
        self.time = 0.0
        self.temp = 0.0
        self.current_og = 1.000
        self.current_fg = 1.000
        self.current_srm = 0.0
        self.current_abv = 0.0
        self.current_ibu = 0.0
        self.current_co2 = 0.0

        # Timeline history data
        self.mashing_history = {0.0:(0.0,0.0,1.0,0.0)}
        self.boiling_history = {0.0:(0.0,0.0)}
        self.fermenting_history = {0.0:(0.0,1.0,0.0,0.0)}

        self.update_final_mashing()
        self.update_final_boiling()
        self.update_final_fermenting()

    def reset(self):
        self.malts = []
        self.hops = []
        self.yeast = None
        self.current_water = 0.0

        self.og = 1.000
        self.fg = 1.000
        self.srm = 0.0
        self.abv = 0.0
        self.ibu = 0.0

        self.time = 0.0
        self.temp = 0.0
        self.current_og = 1.000
        self.current_fg = 1.000
        self.current_srm = 0.0
        self.current_abv = 0.0
        self.current_ibu = 0.0
        self.current_co2 = 0.0

        self.update_final_mashing()
        self.update_final_boiling()
        self.update_final_fermenting()

    def add_malt(self, malt, weight):
        self.malts.append((malt, weight))
        self.update_final_mashing()
        self.add_mashing_history()

    def add_hop(self, hop, weight, time):
        self.hops.append((hop, weight, time))
        self.update_final_boiling()
        self.add_boiling_history()

    def add_yeast(self, yeast):
        self.yeast = yeast
        self.update_final_fermenting()
        self.add_fermenting_history()

    def set_water(self, volume, stage):
        self.current_water = volume
        if stage == 0:
            if self.current_water > 0 and self.malts and self.mashing_history.keys():
                for t in list(self.mashing_history):
                    if t >= self.time:
                        self.mashing_history.pop(t)
                self.add_mashing_history()

                history_time = max((t for t in self.mashing_history if t <= self.time), default=0.0)

                self.current_og, self.current_srm = Bc.calc_mashing(self.mashing_history[history_time][2],
                                                                    self.mashing_history[history_time][3],
                                                                    self.og, self.srm, self.time - history_time,
                                                                    self.mashing_history[history_time][0])
                self.update_final_mashing()

        elif stage == 1:
            if self.current_water > 0 and self.hops and self.boiling_history.keys():
                for t in list(self.boiling_history):
                    if t >= self.time:
                        self.boiling_history.pop(t)
                self.add_boiling_history()

            history_time = max((t for t in self.boiling_history if t <= self.time), default=0.0)

            self.current_ibu, self.current_water, self.current_og = Bc.calc_boiling(self.boiling_history[history_time][1], self.ibu, self.og, self.boiling_history[history_time][0],self.time - history_time)

            self.update_final_boiling()
        elif stage == 2:
            self.current_water = volume

            self.update_final_fermenting()

    def set_temp(self, temp, stage):
        self.temp = temp
        if stage == 0:
            if self.current_water > 0 and self.malts and self.mashing_history.keys():
                for t in list(self.mashing_history):
                    if t >= self.time:
                        self.mashing_history.pop(t)
                self.add_mashing_history()
        elif stage == 2:
            pass

    def set_time(self, time):
        self.time = time

    def add_mashing_history(self):
        if self.time in self.mashing_history.keys():
            self.mashing_history.update({self.time : (self.temp, self.current_water, self.current_og, self.current_srm)})
        else:
            self.mashing_history.setdefault(self.time, (self.temp, self.current_water, self.current_og, self.current_srm))

    def add_boiling_history(self):
        if self.time in self.boiling_history.keys():
            self.boiling_history.update({self.time: (self.current_water, self.current_ibu)})
        else:
            self.boiling_history.setdefault(self.time, (self.current_water, self.current_ibu))

    def add_fermenting_history(self):
        if self.time in self.boiling_history.keys():
            self.fermenting_history.update({self.time: (self.temp, self.current_fg, self.current_abv, self.current_co2)})
        else:
            self.fermenting_history.setdefault(self.time, (self.temp, self.current_fg, self.current_abv, self.current_co2))

    def update_final_mashing(self):
        if self.current_water <= 0:
            return

        if self.malts:
            self.og = Bc.calc_og_many(self.current_water, self.malts)
            self.srm = Bc.calc_srm(malts=self.malts)
        else:
            self.og = 1.000
            self.srm = 0.0

    def update_final_fermenting(self):
        if self.current_water <= 0:
            return

        if self.yeast and self.og > 1.0:
            self.fg = Bc.calc_fg(self.og, self.yeast)
            self.abv = Bc.calc_abv(self.og, self.fg)
        else:
            self.fg = self.og
            self.abv = 0.0

    def update_final_boiling(self):
        if self.current_water <= 0:
            return

        if self.hops and self.og > 1.0:
            self.ibu = Bc.calc_ibu(self.current_water, self.og, self.hops)
        else:
            self.ibu = 0.0

    def update_mashing(self):
        if self.current_water > 0 and self.malts:
            history_time = max((t for t in self.mashing_history if t <= self.time), default=0.0)
            self.current_water = self.mashing_history[history_time][1]
            self.temp = self.mashing_history[history_time][0]
            self.update_final_mashing()

            self.current_og, self.current_srm = Bc.calc_mashing(self.mashing_history[history_time][2],
                                                                self.mashing_history[history_time][3],
                                                                self.og, self.srm, self.time - history_time,
                                                                self.mashing_history[history_time][0])

    def update_boiling(self):
        if self.current_water > 0 and self.hops:
            history_time = max((t for t in self.boiling_history if t <= self.time), default=0.0)

            self.current_ibu, self.current_water, self.current_og = Bc.calc_boiling(self.boiling_history[history_time][1], self.ibu, self.og, self.boiling_history[history_time][0], self.time - history_time)

    def update_fermenting(self):
        pass