# 1
class Matrix:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self):
        matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        for i in range(len(self.x)):
            for j in range(len(self.y)):
                matrix[i][j] = self.x[i][j] + self.y[i][j]
                
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))
    
    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))
    
test = Matrix([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ],
    [
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
        ]
)

print(test.__add__())




# 2
class Clothes:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def coat_square(self):
        return self.width / 6.5 + 0.5
    
    def suit_square(self):
        return self.height * 2 + 0.3
    
    @property
    def total_square(self):
        return str(f'Общая площадь ткани: '
                   f' {(self.coat_square()) + (self.suit_square())}')
        

class Coat(Clothes):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.coat_square())
        
    def __str__(self):
        return f'Площадь ткани на пальто {self.square_c}'
    
class Suit(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_s = round(self.suit_square())

    def __str__(self):
        return f'Площадь ткани на костюм {self.square_s}'

coat = Coat(4, 8)
suit = Suit(6, 4)
print(coat)
print(suit)
print(coat.total_square)
print(suit.total_square)
print(suit.coat_square())
print(suit.suit_square())



# 3

lass Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Результат отрицательный')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


cells1 = Cell(10)
cells2 = Cell(6)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(12))
print(cells1.make_order(3))
print(cells1 / cells2)
