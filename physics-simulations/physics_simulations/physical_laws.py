import logging
NEWTON_G_CONST = 6.67430e-11


logger = logging.getLogger(__name__)

def newton_law_of_gravitation(mass1: float, mass2: float, distance: float, G: float = NEWTON_G_CONST) -> float:
    """
    Calculates the force of attraction between two masses in Newtons.
    Masses are assumed to be in kilograms and distance in meters.
    """
    try:
        if any([mass1 <= 0, mass2 <= 0, distance <= 0]):
            raise ValueError(f"Masses and distance must be positive. Masses: {mass1}, {mass2}. Distance: {distance}")
        return G * (mass1 * mass2) / (abs(distance) ** 2)
    except ValueError as e:
        logger.error(e)
        raise
        
        
        