from dataclasses import dataclass

from satsim.types import StateVector


@dataclass
class Spacecraft:
    name: str
    mass: float  # kg
    ballistic_coefficient: float  # kg/m^2
    state: StateVector
    deployed: bool = False
    attached: bool = True
    decaying: bool = False
    parent = None
