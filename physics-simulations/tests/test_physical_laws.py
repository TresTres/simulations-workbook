import math

import pytest

from physics_simulations import physical_laws as pl
from physics_simulations import vector_math as vm


class TestPhysicalLaws:
    def test_kinematic_distance(self):
        assert pl.kinematic_distance(0) == vm.Vec_3D.ZERO
        assert (
            pl.kinematic_distance(10, vm.Vec_3D.ZERO, vm.Vec_3D.ZERO, vm.Vec_3D.ZERO)
            == vm.Vec_3D.ZERO
        )
        assert pl.kinematic_distance(
            2,
            vm.Vec_3D.ZERO,
            vm.Vec_3D.RIGHT + vm.Vec_3D.UP,
            vm.Vec_3D.ZERO,
        ) == vm.Vec_3D(2, 2, 0)
        assert pl.kinematic_distance(
            1,
            vm.Vec_3D.RIGHT * 10,
            vm.Vec_3D.DOWN * 20,
            vm.Vec_3D.UP * 30,
        ) == vm.Vec_3D(10, -5, 0)
        with pytest.raises(ValueError):
            pl.kinematic_distance(-1, 0, 0, 0)

    def test_newton_gravitation(self):
        assert (
            pl.newton_universal_gravitation(1, 1, vm.Vec_3D.RIGHT)
            == -pl.NEWTON_G_CONST * vm.Vec_3D.RIGHT
        )
        assert pl.newton_universal_gravitation(
            20, 10, vm.Vec_3D(1, 1, 0)
        ) == -pl.NEWTON_G_CONST * 100 * vm.Vec_3D(1 / math.sqrt(2), 1 / math.sqrt(2), 0)
        assert pl.newton_universal_gravitation(20, 10, vm.Vec_3D.LEFT) == pl.NEWTON_G_CONST * 200 * vm.Vec_3D.RIGHT
        with pytest.raises(ValueError):
            pl.newton_universal_gravitation(0, 1, vm.Vec_3D.RIGHT)
