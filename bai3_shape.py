import math

class shape:
    def area(self):
        raise NotImplementedError('Hãy định nghĩa hàm này ở các lớp con')

    def perimeter(self):
        raise NotImplementedError('Hãy định nghĩa hàm này ở các lớp con')

    @property
    def describe(self):
        name = type(self).__name__
        if self.area() is None or self.perimeter() is None:
             return f'{name} Giá Trị Không Hợp Lệ'
        else:
            return f'{name}: S = {self.area():.2f}, P = {self.perimeter():.2f}'

class Circle(shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r**2

    def perimeter(self):
        return 2 * math.pi * self.r

class Rectangle(shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h  
    
    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

class Triangle(shape):
    def __init__(self, a, b, c, p = 0):
        self.a = a
        self.b = b
        self.c = c  
        self.p = p
    def area(self):
        self.p = (self.a + self.b + self.c) / 2
        return math.sqrt(self.p * ((self.p - self.a) * (self.p - self. b) * (self.p - self.c)))

    def perimeter(self):
        return self.p

#phần mở rộng
class Square(Rectangle):
    def __init__(self, w, h):
          super().__init__(w, h)

    def check(self):
        if self.w != self.h:
            return False
        return True
        
    def area(self):
        if self.check() is False:
            return None
        
        return self.w * self.h

    def perimeter(self):
         if self.check() is False:
            return None
         
         return (self.w + self.h) * 2
            
shapes = [
     Circle(2),
     Rectangle(3,4),
     Triangle(3,4,5),
     Square(5,5)
]

for i in shapes:
    print(i.describe)

value_shapes = [i for i in shapes if i.area() is not None]
    
tong = sum(i.area() for i in value_shapes)
print(f'Tổng diện tích các hình: {tong:.2f}')
lst = sorted(value_shapes, key=lambda s: s.area())
print([i.describe for i in lst])