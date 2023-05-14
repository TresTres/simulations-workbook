import pytest

from physics_simulations import vector_math as vm

class TestVectorMath:
        
    
    def test_vector_direction(self):
        assert vm.Vec_3D.UP == vm.Vec_3D(0, 1, 0)
        assert vm.Vec_3D.DOWN == vm.Vec_3D(0, -1, 0)
        assert vm.Vec_3D.LEFT == vm.Vec_3D(-1, 0, 0)
        assert vm.Vec_3D.RIGHT == vm.Vec_3D(1, 0, 0)
        assert vm.Vec_3D.FORWARD == vm.Vec_3D(0, 0, 1)
        assert vm.Vec_3D.BACKWARD == vm.Vec_3D(0, 0, -1)
        assert vm.Vec_3D.ZERO == vm.Vec_3D(0, 0, 0)
        
    def test_vector_properties(self):
        vec = vm.Vec_3D(2, 3, 6)
        assert vec.magnitude == 7
        assert vec.unit_vector == vm.Vec_3D(2/7, 3/7, 6/7)


    def test_vector_ops(self):
        assert vm.Vec_3D.RIGHT + vm.Vec_3D.LEFT == vm.Vec_3D.ZERO
        assert vm.Vec_3D.RIGHT - vm.Vec_3D.RIGHT == vm.Vec_3D.ZERO
        assert -vm.Vec_3D.UP == vm.Vec_3D.DOWN
        assert vm.Vec_3D.RIGHT * 2 == vm.Vec_3D(2, 0, 0)
        assert 2 * vm.Vec_3D.RIGHT == vm.Vec_3D(2, 0, 0)
        assert vm.Vec_3D.RIGHT / 2 == vm.Vec_3D(0.5, 0, 0)
        assert [*vm.Vec_3D.RIGHT._data] == [1, 0, 0]
        
    def test_vector_illegal_ops(self):
        with pytest.raises(TypeError):
            vm.Vec_3D.RIGHT + 1
        with pytest.raises(TypeError):
            vm.Vec_3D.RIGHT - 1
        with pytest.raises(TypeError):
            vm.Vec_3D.RIGHT * vm.Vec_3D.RIGHT
        with pytest.raises(TypeError):
            vm.Vec_3D.RIGHT / vm.Vec_3D.RIGHT
        with pytest.raises(TypeError):
            3 / vm.Vec_3D.RIGHT

