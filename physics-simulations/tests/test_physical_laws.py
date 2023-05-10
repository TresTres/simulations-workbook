import pytest
import physics_simulations.physical_laws as pl

class TestPhysicalLaws:
    
    def test_newton_law_of_gravitation(self):
        assert pl.newton_law_of_gravitation(1, 1, 1) == pl.NEWTON_G_CONST
        assert pl.newton_law_of_gravitation(20, 10, 2) == pl.NEWTON_G_CONST * 50
        with pytest.raises(ValueError):
            pl.newton_law_of_gravitation(0, 1, 1)