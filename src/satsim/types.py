from dataclasses import dataclass

import numpy as np
import numpy.typing as npt

Vec3 = npt.NDArray[np.float64]  # float64 ndarray, shape (3,)


@dataclass(frozen=True)
class StateVector:
    r: Vec3  # position, km, ECI J2000
    v: Vec3  # velocity, km/s, ECI J2000


@dataclass(frozen=True)
class OrbitalElements:
    a: float  # semi-major axis, km
    e: float  # eccentricity
    i: float  # inclination, rad
    raan: float  # right ascension of ascending node, rad
    argp: float  # argument of periapsis, rad
    nu: float  # true anomaly, rad
