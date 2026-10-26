import json
from pathlib import Path
from src.core.model import Hop, Malt, Yeast

class Repository:
    def __init__(self):
        self.hop_path = Path("data/hop.json")
        self.malt_path = Path("data/malt.json")
        self.yeast_path = Path("data/yeast.json")

        self.hops = []
        self.malts = []
        self.yeasts = []

        self._load_data()

    def _load_data(self):
        with open(self.hop_path, 'r') as file:
            for item in json.load(file):
                new_hop = Hop(
                    name=item["Hop"],
                    origin=item["Origin"],
                    type=item["Type"],
                    alpha=item["Alpha"],
                    beta=item["Beta"]
                )
            self.hops.append(new_hop)
        with open(self.malt_path, 'r') as file:
            for item in json.load(file):
                new_malt = Malt(
                    name=item["Hop"],
                    origin=item["Origin"],
                    color=item["Color"],
                    potential=item["Potential"],
                )
            self.malts.append(new_malt)
        with open(self.yeast_path, 'r') as file:
            for item in json.load(file):
                new_yeast = Yeast(
                    name = item["Hop"],
                    lab = item["Lab"],
                    type = item["Type"],
                    form = item["Form"],
                    min_temp = item["MinTemp"],
                    max_temp = item["MaxTemp"],
                    attenuation=item["Attenuation"],
                    flocculation=item["Flocculation"]
                )
            self.yeasts.append(new_yeast)

    def get_hops(self):
        return self.hops

    def get_malts(self):
        return self.malts

    def get_yeasts(self):
        return self.yeasts



