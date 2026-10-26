from src.core.model import Yeast
import math


class BrewCalculator:

    # Calculates the Original Gravity for a single malt based on the given batch size
    @staticmethod
    def calc_og_single(self, batch_size, malt_weight, potential):
        kgpl_to_lbpgal = 0.12
        efficiency = 0.70
        # OG = PPG/1000 * Efficiency(%) * Weight(KG) / BatchSize(L) / (Conversion value from kg/L to lb/gal)
        og = (potential - 1) * efficiency * malt_weight / batch_size / kgpl_to_lbpgal
        return og

    # Calculates the Original Gravity for a list of malts based on the given batch size
    @staticmethod
    def calc_og_many(self, batch_size, malts):
        og_sum = 0
        for malt in malts:
            og_sum += self.calc_og_single(batch_size, malt[1], malt[0].potential)
        return og_sum + 1

    # Calculates the final SRM color value for a list of malts based on each malt's weight
    @staticmethod
    def calc_srm(self, malts):
        weight_sum = 0
        srm_sum = 0
        for malt in malts:
            weight_sum += malt[1]
            srm_sum += malt[0].color * malt[1]
        final_srm = srm_sum/ weight_sum
        return final_srm

    # Calculates the Final Gravity based on the Original Gravity and the Yeast's Attenuation
    @staticmethod
    def calc_fg(self, og, yeast):
        fg = (og - 1) * (1 - yeast.attenuation)
        return fg

    # Calculates the Alcohol By Volume based on the Original Gravity and the Final Gravity
    @staticmethod
    def calc_abv(self, og, fg):
        abv = (og - fg) * 131.25
        return abv

    # Calculates the final IBU value for a list of hops based on each hop's weight and boil time
    @staticmethod
    def calc_ibu(self, batch_size, og, hops):
        ibu_sum = 0
        bigness_factor = 1.65 * (0.000125 ** (og - 1))
        for hop in hops:
            if hop[1] <= 0 or hop[2] <= 0:
                continue
            time_factor = (1 - math.exp(-0.04 * hop[2])) / 4.15
            utilization = bigness_factor * time_factor * 1.1
            ibu_sum += round(hop[1] * hop[0].alpha * utilization * 10 / batch_size,2)
        return ibu_sum


