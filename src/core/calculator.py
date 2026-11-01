from src.core.model import Yeast
import math

class BrewCalculator:

    # Calculates the Original Gravity for a single malt based on the given batch size
    @staticmethod
    def calc_og_single(batch_size, malt_weight, potential):
        if batch_size <= 0:
            return 0
        kgpl_to_lbpgal = 0.12
        efficiency = 0.70
        # OG = PPG/1000 * Efficiency(%) * Weight(KG) / BatchSize(L) / (Conversion value from kg/L to lb/gal)
        og = (potential - 1) * efficiency * malt_weight / batch_size / kgpl_to_lbpgal
        return og

    # Calculates the Original Gravity for a list of malts based on the given batch size
    @staticmethod
    def calc_og_many(batch_size, malts):
        og_sum = 0
        for malt in malts:
            og_sum += BrewCalculator.calc_og_single(batch_size, malt[1], malt[0].potential)
        return og_sum + 1

    # Calculates the final SRM color value for a list of malts based on each malt's weight
    @staticmethod
    def calc_srm(malts):
        weight_sum = 0
        srm_sum = 0
        for malt in malts:
            weight_sum += malt[1]
            srm_sum += malt[0].color * malt[1]
        if weight_sum <= 0:
            return 0
        final_srm = srm_sum / weight_sum
        return final_srm

    # Calculates the Final Gravity based on the Original Gravity and the Yeast's Attenuation
    @staticmethod
    def calc_fg(og, yeast):
        if not yeast or yeast.attenuation is None:
            return og
        fg = 1 + (og - 1) * (1 - yeast.attenuation)
        return fg

    # Calculates the Alcohol By Volume based on the Original Gravity and the Final Gravity
    @staticmethod
    def calc_abv(og, fg):
        abv = (og - fg) * 131.25
        return max(0.0, abv)

    # Calculates the final IBU value for a list of hops based on each hop's weight and boil time
    @staticmethod
    def calc_ibu(batch_size, og, hops):
        if batch_size <= 0:
            return 0
        ibu_sum = 0
        bigness_factor = 1.65 * (0.000125 ** (og - 1))
        for hop in hops:
            if hop[1] <= 0 or hop[2] <= 0:
                continue
            time_factor = (1 - math.exp(-0.04 * hop[2])) / 4.15
            utilization = bigness_factor * time_factor * 1.1
            ibu_sum += round(hop[1] * hop[0].alpha * utilization * 10 / batch_size, 2)
        return ibu_sum

    # Calculates current OG and SRM based on mash temperature and time
    @staticmethod
    def calc_mashing(og_start, srm_start, og_final, srm_final, time, temp):
        # Gaussian curve peaking at 67 ˚C
        k_og = 0.08 * math.exp(-((temp - 67) ** 2) / 50)

        # Linear scaling
        k_srm = 0.12 * (temp / 67)

        og_progress = 1 - math.exp(-k_og * time)
        srm_progress = 1 - math.exp(-k_srm * time)

        og_diff = (og_final - og_start)
        srm_diff = (srm_final - srm_start)

        current_og = og_start + (og_diff * og_progress)
        current_srm = srm_start + (srm_diff * srm_progress)

        return current_og, current_srm

    # Calculates current IBU, Volume and OG based on boil time and water evaporation
    @staticmethod
    def calc_boiling(ibu_start, ibu_final, og_start, water_volume, time, target_time):
        if water_volume <= 0:
            return 0.0, 0.0, og_start

        evaporation_rate_per_min = 0.10 / 60

        current_volume = water_volume * (1 - (evaporation_rate_per_min * time))

        starting_gravity_points = (og_start - 1.0) * water_volume
        current_og = 1.0 + (starting_gravity_points / current_volume)

        k_ibu = 0.04
        t_target = float(target_time)
        scale = 1.0 - math.exp(-k_ibu * t_target)
        ibu_progress = (1.0 - math.exp(-k_ibu * time)) / scale

        ibu_diff = ibu_final - ibu_start
        current_ibu = round(ibu_start + (ibu_diff * ibu_progress), 2)

        return current_ibu, current_volume, current_og

    # Calculates current FG and ABV based on fermentation time and temperature
    @staticmethod
    def calc_fermenting(og_start, fg_final, time, temp, yeast=None, fg_start=None, abv_start=None):
        if og_start <= 1.0:
            return 1.0, 0.0

        if fg_start is None:
            fg_start = og_start

        if yeast:
            mid_temp = (yeast.min_temp + yeast.max_temp) / 2.0
            temp_range = max(1.0, (yeast.max_temp - yeast.min_temp) / 2.0)
            temp_factor = math.exp(-((temp - mid_temp) ** 2) / (2 * (temp_range ** 2)))
        elif yeast:
            mid_temp = (yeast.min_temp + yeast.max_temp) / 2.0
            temp_factor = math.exp(-((temp - mid_temp) ** 2) / 50)
        else:
            temp_factor = math.exp(-((temp - 20) ** 2) / 50)

        k_ferm = 0.35 * temp_factor
        ferm_progress = 1 - math.exp(-k_ferm * max(0.0, time))

        fg_diff = max(0.0, fg_start - fg_final)
        current_fg = round(fg_start - (fg_diff * ferm_progress), 3)

        if abv_start is not None:
            current_abv = max(abv_start, round(abv_start + (fg_start - current_fg) * 131.25, 2))
        else:
            current_abv = max(0.0, round((og_start - current_fg) * 131.25, 2))

        return current_fg, current_abv
