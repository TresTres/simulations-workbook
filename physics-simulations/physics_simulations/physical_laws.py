import logging

from vector_math import Vec_3D

logger = logging.getLogger(__name__)


NEWTON_G_CONST = 6.67430e-11

def kinematic_distance(
    time: float,
    distance: Vec_3D = Vec_3D.ZERO,
    velocity: Vec_3D = Vec_3D.ZERO,
    acceleration: Vec_3D = Vec_3D.ZERO,
) -> Vec_3D:
    """
    Calculates the distance travelled using the kinematic equation:
    distance = initial_distance + initial_velocity * time + 0.5 * acceleration * time ** 2
    Time is assumed to be in seconds, the other parameters can be expressed using consistent units,
    e.g. meters, meters per second, meters per second squared.
    """
    try:
        if time < 0:
            raise ValueError(f"Time must be positive. Time: {time}")
        return distance + velocity * time + 0.5 * acceleration * time**2
    except ValueError as e:
        logger.error(e)
        raise


def newton_universal_gravitation(
    mass1: float, mass2: float, distance: Vec_3D, G: float = NEWTON_G_CONST
) -> Vec_3D:
    """
    Calculates the force of attraction between two masses in Newtons.
    Masses are assumed to be in kilograms and distances expressed in meters.
    """
    try:
        if any([mass1 <= 0, mass2 <= 0, distance.magnitude <= 0]):
            raise ValueError(f"Masses and distance magnitude must be positive. Masses: {mass1}, {mass2}, Distance: {distance}")
        return -1 * distance.unit_vector * G * (mass1 * mass2) / (distance.magnitude**2)
    except ValueError as e:
        logger.error(e)
        raise
