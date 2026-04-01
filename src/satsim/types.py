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
    a: np.float64  # semi-major axis, km
    e: np.float64  # eccentricity
    i: np.float64  # inclination, rad
    raan: np.float64  # right ascension of ascending node, rad
    argp: np.float64  # argument of periapsis, rad
    nu: np.float64  # true anomaly, rad
