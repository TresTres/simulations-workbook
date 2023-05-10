import logging

NEWTON_G_CONST = 6.67430e-11


logger = logging.getLogger(__name__)


def kinematic_distance(
    time: float, distance: float = 0, velocity: float = 0, acceleration: float = 0
) -> float:
    """
    Calculates the distance travelled using the kinematic equation:
    distance = initial_distance + initial_velocity * time + 0.5 * acceleration * time ** 2
    Time is assumed to be in seconds, the other parameters can be expressed using consistent units,
    e.g. meters, meters per second, meters per second squared.
    """
    try:
        if any([time < 0, distance < 0]):
            raise ValueError(
                f"Time and distance must be positive. Time: {time}, distance: {distance}"
            )
        return distance + velocity * time + 0.5 * acceleration * time**2
    except ValueError as e:
        logger.error(e)
        raise


def newton_universal_gravitation(
    mass1: float, mass2: float, distance: float, G: float = NEWTON_G_CONST
) -> float:
    """
    Calculates the force of attraction between two masses in Newtons.
    Masses are assumed to be in kilograms and distance in meters.
    """
    try:
        if any([mass1 <= 0, mass2 <= 0, distance <= 0]):
            raise ValueError(
                f"Masses and distance must be positive. Masses: {mass1}, {mass2}. Distance: {distance}"
            )
        return G * (mass1 * mass2) / (abs(distance) ** 2)
    except ValueError as e:
        logger.error(e)
        raise
