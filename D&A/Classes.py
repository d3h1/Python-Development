class Cookie:
    def __init__ (self, color, taste, size):
        self.color = color
        self.taste = taste
        self.size = size
    
    def get_color(self):
        return self.color
    
    
cookie_one = Cookie('red', 'chocolate', 'medium')

print(f'Cookie ones color is {cookie_one.get_color()}')
