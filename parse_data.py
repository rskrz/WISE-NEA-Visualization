from dataclasses import dataclass
from pprint import pprint

@dataclass
class Comet():
    object: str
    epoch: int
    tp: int
    e: float
    i: float
    w: float
    node: float
    _q: float
    q: float
    p: float
    moid: float

class Data():
    def __init__(self, filename):
        self.comets = self.load_data(filename)

    # Load CSV data from {filename}
    # return: Comet objects
    def load_data(self, filename):
        with open(filename) as f:
            return [Comet(*line.split(',')[:-6]) for line in f if line]
