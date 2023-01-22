from math import sqrt


class Vec2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    
    def __add__(self, V):
        return Vec2(self.x + V.x, self.y + V.y)


    def __sub__(self, V):
        return Vec2(self.x - V.x, self.y - V.y)
    

    def __truediv__(self, a: float):
        if a == 0:
            raise Exception("ZeroDivisionError: division by zero")
        return Vec2(self.x / a, self.y / a)
    

    def __mul__(self, a: float):
        return Vec2(self.x * a, self.y * a)


    def abs(self) -> float:
        return sqrt(self.x**2 + self.y**2)


    def normalized(self):
        return self / self.abs()
