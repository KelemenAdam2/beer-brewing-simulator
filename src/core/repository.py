import json
from pathlib import Path
from src.core.model import Hop, Malt, Yeast

class Repository:
    def __init__(self):
        data_dir = Path(__file__).resolve().parent.parent / "data"
        self.hop_path = data_dir / "hop.json"
        self.malt_path = data_dir / "malt.json"
        self.yeast_path = data_dir / "yeast.json"

        self.hops = []
        self.malts = []
        self.yeasts = []

        self._load_data()

    def _load_data(self):
        with open(self.hop_path, 'r', encoding='utf-8') as file:
            for item in json.load(file):
                self.hops.append(Hop(
                    name=item.get("Hop", item.get("name", "")),
                    origin=item.get("Origin", item.get("origin", "")),
                    type=item.get("Type", item.get("type", "")),
                    alpha=float(item.get("Alpha", item.get("alpha", 0))),
                    beta=float(item.get("Beta", item.get("beta", 0)))
                ))

        with open(self.malt_path, 'r', encoding='utf-8') as file:
            for item in json.load(file):
                self.malts.append(Malt(
                    name=item.get("Grain", item.get("name", "")),
                    origin=item.get("Origin", item.get("origin", "")),
                    color=float(item.get("Color", item.get("color", 0))),
                    potential=float(item.get("Potential", item.get("potential", 0)))
                ))

        with open(self.yeast_path, 'r', encoding='utf-8') as file:
            for item in json.load(file):
                self.yeasts.append(Yeast(
                    name=item.get("Name", item.get("name", "")),
                    lab=item.get("Lab", item.get("lab", "")),
                    type=item.get("Type", item.get("type", "")),
                    form=item.get("Form", item.get("form", "")),
                    min_temp=int(item.get("MinTemp", item.get("min_temp", 0))),
                    max_temp=int(item.get("MaxTemp", item.get("max_temp", 0))),
                    attenuation=float(item.get("Attenuation", item.get("attenuation", 0))),
                    flocculation=item.get("Flocculation", item.get("flocculation", ""))
                ))

    def get_hops(self):
        return self.hops

    def get_malts(self):
        return self.malts

    def get_yeasts(self):
        return self.yeasts
