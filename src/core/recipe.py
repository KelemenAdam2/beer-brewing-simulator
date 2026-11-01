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

        # Potential values
        self.potential_og = 1.000
        self.potential_srm = 0.0

        # Stage results passed between stages
        self.mashing_og = 1.000
        self.mashing_srm = 0.0
        self.mashing_water = 0.0
        self.boiling_og = 1.000
        self.boiling_ibu = 0.0
        self.boiling_water = 0.0
        self.fermenting_fg = 1.000
        self.fermenting_abv = 0.0

        # Metrics values
        self.og = 1.000
        self.fg = 1.000
        self.srm = 0.0
        self.abv = 0.0
        self.ibu = 0.0

        # Values at current timeline time
        self.time = 0.0
        self.temp = 0.0
        self.current_og = 1.000
        self.current_fg = 1.000
        self.current_srm = 0.0
        self.current_abv = 0.0
        self.current_ibu = 0.0

        # Timeline history data
        self.mashing_history = {0.0: (0.0, 0.0, 1.0, 0.0)}
        self.boiling_history = {0.0: (0.0, 0.0)}
        self.fermenting_history = {0.0: (0.0, 1.0, 0.0)}

        self.update_final_mashing()
        self.update_final_boiling()
        self.update_final_fermenting()

    def reset(self):
        self.malts = []
        self.hops = []
        self.yeast = None
        self.current_water = 0.0

        self.potential_og = 1.000
        self.potential_srm = 0.0

        self.mashing_og = 1.000
        self.mashing_srm = 0.0
        self.mashing_water = 0.0
        self.boiling_og = 1.000
        self.boiling_ibu = 0.0
        self.boiling_water = 0.0
        self.fermenting_fg = 1.000
        self.fermenting_abv = 0.0

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

        self.mashing_history = {0.0: (0.0, 0.0, 1.0, 0.0)}
        self.boiling_history = {0.0: (0.0, 0.0)}
        self.fermenting_history = {0.0: (0.0, 1.0, 0.0)}

        self.update_final_mashing()
        self.update_final_boiling()
        self.update_final_fermenting()

    def add_malt(self, malt, weight):
        self.malts.append((malt, weight))
        self.update_final_mashing()
        self.update_final_boiling()
        self.update_final_fermenting()
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
        old_water = self.current_water if self.current_water > 0 else (self.mashing_water if self.mashing_water > 0 else volume)
        self.current_water = volume

        if stage == 0:
            self.update_final_mashing()
            self.update_final_boiling()
            self.update_final_fermenting()
            if self.current_water > 0 and self.malts and self.mashing_history.keys():
                for t in list(self.mashing_history):
                    if t >= self.time:
                        self.mashing_history.pop(t)
                self.add_mashing_history()

                history_time = max((t for t in self.mashing_history if t <= self.time), default=0.0)

                self.current_og, self.current_srm = Bc.calc_mashing(
                    self.mashing_history[history_time][2],
                    self.mashing_history[history_time][3],
                    self.potential_og, self.potential_srm, self.time - history_time,
                    self.mashing_history[history_time][0]
                )

        elif stage == 1:
            # Dilution calculation when adding water during boiling
            base_og = self.mashing_og if self.mashing_og > 1.0 else self.og
            old_og = self.current_og if self.current_og > 1.0 else base_og
            if old_water > 0 and volume > 0 and old_og > 1.0:
                gravity_points = (old_og - 1.0) * old_water
                self.current_og = 1.0 + (gravity_points / volume)
                self.mashing_og = self.current_og
                self.og = self.current_og

            if self.boiling_history.keys():
                for t in list(self.boiling_history):
                    if t >= self.time:
                        self.boiling_history.pop(t)
            self.add_boiling_history()

            target_time = max((h[2] for h in self.hops if len(h) > 2 and h[2] > 0), default=60.0)
            history_time = max((t for t in self.boiling_history if t <= self.time), default=0.0)
            og_start = self.mashing_og if self.mashing_og > 1.0 else self.og
            water_start = self.boiling_history[history_time][0] if self.boiling_history[history_time][0] > 0 else self.current_water
            remaining_target = max(1.0, target_time - history_time)

            self.current_ibu, self.current_water, self.current_og = Bc.calc_boiling(
                self.boiling_history[history_time][1], self.ibu, og_start, water_start, self.time - history_time, remaining_target
            )

            self.update_final_boiling()

        elif stage == 2:
            self.update_final_fermenting()

    def set_temp(self, temp, stage):
        if stage == 0:
            if self.current_water > 0 and self.malts and self.mashing_history.keys():
                self.update_mashing()
                self.temp = temp
                for t in list(self.mashing_history):
                    if t >= self.time:
                        self.mashing_history.pop(t)
                self.add_mashing_history()
                self.update_mashing()
        elif stage == 2:
            if self.fermenting_history.keys():
                self.update_fermenting()
                self.temp = temp
                for t in list(self.fermenting_history):
                    if t >= self.time:
                        self.fermenting_history.pop(t)
                self.add_fermenting_history()
                self.update_fermenting()

    def set_time(self, time):
        self.time = time

    def add_mashing_history(self):
        if self.time in self.mashing_history.keys():
            self.mashing_history.update({self.time: (self.temp, self.current_water, self.current_og, self.current_srm)})
        else:
            self.mashing_history.setdefault(self.time, (self.temp, self.current_water, self.current_og, self.current_srm))

    def add_boiling_history(self):
        water = self.current_water if self.current_water > 0 else (self.mashing_water if self.mashing_water > 0 else 20.0)
        if self.time in self.boiling_history.keys():
            self.boiling_history.update({self.time: (water, self.current_ibu)})
        else:
            self.boiling_history.setdefault(self.time, (water, self.current_ibu))

    def add_fermenting_history(self):
        temp = self.temp if self.temp > 0 else 20.0
        fg = self.current_fg if self.current_fg > 1.0 else (self.og if self.og > 1.0 else 1.0)
        abv = self.current_abv
        if self.time in self.fermenting_history.keys():
            self.fermenting_history.update({self.time: (temp, fg, abv)})
        else:
            self.fermenting_history.setdefault(self.time, (temp, fg, abv))

    def update_final_mashing(self):
        if self.current_water <= 0:
            return

        if self.malts:
            self.potential_og = Bc.calc_og_many(self.current_water, self.malts)
            self.potential_srm = Bc.calc_srm(malts=self.malts)
        else:
            self.potential_og = 1.000
            self.potential_srm = 0.0

        if self.mashing_og <= 1.0:
            self.og = self.potential_og
            self.srm = self.potential_srm

    def update_final_boiling(self):
        water = self.current_water if self.current_water > 0 else (self.mashing_water if self.mashing_water > 0 else 20.0)
        og = self.og if self.og > 1.0 else self.potential_og
        if self.hops and og > 1.0 and water > 0:
            self.ibu = Bc.calc_ibu(water, og, self.hops)
        else:
            self.ibu = 0.0

    def update_final_fermenting(self):
        og = self.og if self.og > 1.0 else self.potential_og
        if self.yeast and og > 1.0:
            self.fg = Bc.calc_fg(og, self.yeast)
            self.abv = Bc.calc_abv(og, self.fg)
        else:
            self.fg = og
            self.abv = 0.0

    def update_mashing(self):
        if self.current_water > 0 and self.malts:
            history_time = max((t for t in self.mashing_history if t <= self.time), default=0.0)
            self.current_water = self.mashing_history[history_time][1]
            self.temp = self.mashing_history[history_time][0]

            self.current_og, self.current_srm = Bc.calc_mashing(
                self.mashing_history[history_time][2],
                self.mashing_history[history_time][3],
                self.potential_og, self.potential_srm, self.time - history_time,
                self.mashing_history[history_time][0]
            )

    def update_boiling(self):
        water = self.mashing_water if self.mashing_water > 0 else self.current_water
        if water > 0 and self.hops:
            target_time = max((h[2] for h in self.hops), default=60)
            history_time = max((t for t in self.boiling_history if t <= self.time), default=0.0)
            og_start = self.mashing_og if self.mashing_og > 1.0 else self.og
            water_start = self.boiling_history[history_time][0] if self.boiling_history[history_time][0] > 0 else water
            remaining_target = max(1.0, target_time - history_time)

            self.current_ibu, self.current_water, self.current_og = Bc.calc_boiling(
                self.boiling_history[history_time][1], self.ibu, og_start, water_start, self.time - history_time, remaining_target
            )

    def update_fermenting(self):
        og_start = self.boiling_og if self.boiling_og > 1.0 else (self.mashing_og if self.mashing_og > 1.0 else self.og)
        if og_start > 1.0 and self.yeast:
            history_time = max((t for t in self.fermenting_history if t <= self.time), default=0.0)
            self.temp = self.fermenting_history[history_time][0]
            fg_start = self.fermenting_history[history_time][1]
            abv_start = self.fermenting_history[history_time][2]

            self.current_fg, self.current_abv = Bc.calc_fermenting(
                og_start, self.fg, self.time - history_time, self.temp, self.yeast,
                fg_start=fg_start, abv_start=abv_start
            )

    def stop_mashing(self):
        self.mashing_og = self.current_og
        self.mashing_srm = self.current_srm
        self.mashing_water = self.current_water
        self.og = self.mashing_og
        self.srm = self.mashing_srm
        self.update_final_boiling()
        self.update_final_fermenting()
        self.boiling_history = {0.0: (self.current_water, 0.0)}
        self.time = 0.0

    def stop_boiling(self):
        self.boiling_og = self.current_og
        self.boiling_ibu = self.current_ibu
        self.boiling_water = self.current_water
        self.og = self.boiling_og
        self.ibu = self.boiling_ibu
        self.update_final_fermenting()
        self.temp = 20.0
        self.fermenting_history = {0.0: (20.0, self.og, 0.0)}
        self.current_fg = self.og
        self.current_abv = 0.0
        self.time = 0.0

    def stop_fermenting(self):
        self.fermenting_fg = self.current_fg
        self.fermenting_abv = self.current_abv
        self.fg = self.current_fg
        self.abv = self.current_abv
