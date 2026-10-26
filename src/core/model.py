from dataclasses import dataclass

@dataclass()
class Hop:
    name : str
    origin : str
    type : str
    alpha : float
    beta : float

@dataclass()
class Malt:
    name : str
    origin: str
    color : float
    potential : float

@dataclass()
class Yeast:
    name : str
    lab : str
    type: str
    form : str
    min_temp: int
    max_temp: int
    attenuation : float
    flocculation : str
