class Figure:
    color = 'white'
    def change_color(self, new_color):
        self.color = new_color
        
        
class Oval(Figure):
    def __init__(self, w, h):
        self.width = w
        self.height = h
        

class Square(Figure):
    def __init__(self, h):
        self.height = h
        self.width = h
        

print('\n  Oval: ')        
my_oval = Oval(12, 20)
print('\tColor: ', my_oval.color)
print('\tHeight: ', my_oval.height)
print('\tWidth: ', my_oval.width)
my_oval.change_color('blue')
print('\tNew color: ', my_oval.color)

print('\n  Square: ')        
my_square = Square(15)
print('\tColor: ', my_square.color)
print('\tHeight: ', my_square.height)
print('\tWidth: ', my_square.width)
my_square.change_color('green')
print('\tNew color: ', my_square.color)