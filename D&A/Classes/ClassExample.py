# class Cookie:
#     def __init__ (self, color, taste, size):
#         self.color = color
#         self.taste = taste
#         self.size = size
    
#     def get_color(self):
#         return self.color
    
#     def set_color(self,color):
#         self.color = color
    
    
# cookie_one = Cookie('red', 'chocolate', 'medium')
# print(f'Cookie ones color is {cookie_one.get_color()}')

# cookie_one.set_color('blue')
# print(f'Cookie ones color is {cookie_one.get_color()}')


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def sqSum(self):
        a = self.x ** 2
        b = self.y ** 2
        c = self.z ** 2
        sum = a + b + c
        return sum
    
        

Sum = Point(3,4,5)
Sum.a



