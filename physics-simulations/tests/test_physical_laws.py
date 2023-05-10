import pytest
import physics_simulations.physical_laws as pl


class TestPhysicalLaws:
    def test_kinematic_distance(self):
        assert pl.kinematic_distance(0) == 0
        assert pl.kinematic_distance(1, 0, 0, 0) == 0
        assert pl.kinematic_distance(1, 1, 0, 0) == 1
        assert pl.kinematic_distance(1, 0, 1, 0) == 1
        assert pl.kinematic_distance(1, 0, 0, 1) == 0.5
        assert pl.kinematic_distance(1, 10, 20, 30) == 45
        with pytest.raises(ValueError):
            pl.kinematic_distance(-1, 0, 0, 0)

    def test_newton_gravitation(self):
        assert pl.newton_universal_gravitation(1, 1, 1) == pl.NEWTON_G_CONST
        assert pl.newton_universal_gravitation(20, 10, 2) == pl.NEWTON_G_CONST * 50
        with pytest.raises(ValueError):
            pl.newton_universal_gravitation(0, 1, 1)
