import logging

import numpy as np


logger = logging.getLogger(__name__)

class Vec_3D:
    """
    A 3D vector class building on top of numpy's array class.
    """
    
    _data: np.array
    ZERO: "Vec_3D" 
    RIGHT: "Vec_3D"
    LEFT: "Vec_3D"
    UP: "Vec_3D"
    DOWN: "Vec_3D"
    FORWARD: "Vec_3D"
    BACKWARD: "Vec_3D"
    
    
    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        self._data = np.array([x, y, z])
        
    @property
    def x(self) -> float:
        return self._data[0]
    
    @x.setter
    def x(self, value: float) -> None:
        self._data[0] = value
    
    @property
    def y(self) -> float:
        return self._data[1]
    
    @y.setter
    def y(self, value: float) -> None:
        self._data[1] = value
    
    @property
    def z(self) -> float:
        return self._data[2]
    
    @z.setter
    def z(self, value: float) -> None:
        self._data[2] = value
    
    @property 
    def magnitude(self) -> float:
        return np.linalg.norm(self._data)
    
    @property
    def unit_vector(self) -> "Vec_3D":
        return Vec_3D(*(self._data / self.magnitude))
    
    def __str__(self) -> str:
        return f"Vec_3D({self.x}, {self.y}, {self.z})"

    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Vec_3D):
            return np.allclose(self._data, other._data, rtol=1e-12, atol=1e-11)
        else:
            raise TypeError(f"Cannot compare {type(self)} and {type(other)}")
        
    def __add__(self, other) -> "Vec_3D":
        if isinstance(other, Vec_3D):
            return Vec_3D(*(self._data + other._data))
        else:
            raise TypeError(f"Cannot add {type(self)} and {type(other)}")
        
    def __sub__(self, other) -> "Vec_3D":
        if isinstance(other, Vec_3D):
            return Vec_3D(*(self._data - other._data))
        else:
            raise TypeError(f"Cannot subtract {type(self)} and {type(other)}")
    
    def __neg__(self) -> "Vec_3D":
        return Vec_3D(*(-self._data))
        
    def __mul__(self, other) -> "Vec_3D":
        if isinstance(other, (int, float)):
            return Vec_3D(*(self._data * other))
        else:
            raise TypeError(f"Cannot multiply {type(self)} and {type(other)}")
        
    def __rmul__(self, other) -> "Vec_3D":
        return self.__mul__(other)

    def __truediv__(self, other) -> "Vec_3D":
        if isinstance(other, (int, float)):
            return Vec_3D(*(self._data / other))
        else:
            raise TypeError(f"Cannot divide {type(self)} and {type(other)}")

    def __iter__(self):
        return iter(self._data)
    
    

# I don't know how to turn these into static class variables
Vec_3D.ZERO = Vec_3D(0, 0, 0)
Vec_3D.RIGHT = Vec_3D(1, 0, 0)
Vec_3D.LEFT = Vec_3D(-1, 0, 0)
Vec_3D.UP = Vec_3D(0, 1, 0)
Vec_3D.DOWN = Vec_3D(0, -1, 0)
Vec_3D.FORWARD = Vec_3D(0, 0, 1)
Vec_3D.BACKWARD = Vec_3D(0, 0, -1)