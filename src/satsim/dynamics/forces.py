import numpy as np

from satsim.environment.earth import Environment
from satsim.types import StateVector, Vec3


def accel_2body(state: StateVector, t: np.float64, env: Environment) -> Vec3:
    # pulls toward Earth center; a = -mu/r^3 * r (r^3 folds in the unit vector)
    r_mag = np.linalg.norm(state.r)
    return -env.mu / r_mag**3 * state.r


def accel_j2(state: StateVector, t: np.float64, env: Environment) -> Vec3:
    # Earth bulges at the equator; J2 corrects for the asymmetry
    r = state.r
    r_mag = np.linalg.norm(r)
    x, y, z = r
    factor = -1.5 * env.J2 * env.mu * env.R_e**2 / r_mag**5
    z2 = (z / r_mag) ** 2  # sin^2 of latitude
    return np.array(
        [
            factor * x * (1.0 - 5.0 * z2),
            factor * y * (1.0 - 5.0 * z2),
            factor * z * (3.0 - 5.0 * z2),
        ]
    )


def gravity(state: StateVector, t: np.float64, env: Environment) -> Vec3:
    # total gravity: two-body + J2 perturbation
    return accel_2body(state, t, env) + accel_j2(state, t, env)
