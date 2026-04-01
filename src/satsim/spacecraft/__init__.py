from dataclasses import dataclass

import numpy as np

from satsim.types import StateVector


@dataclass
class Spacecraft:
    name: str
    mass: np.float64  # kg
    ballistic_coefficient: np.float64  # kg/m^2
    state: StateVector
    deployed: bool = False
    attached: bool = True
    decaying: bool = False
    parent = None
