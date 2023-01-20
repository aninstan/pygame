class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    
    def __add__(self, v):
        return Vec2(self.x + v.x, self.y + v.y)
    

    def get_scaled(self, a):
        return Vec2(self.x * a, self.y * a)