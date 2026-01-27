class point:
    def __init__(self, x, y):
        self.x= x
        self.y= y

    def coord(self):
        print(self.x)
        print(self.y)

obj= point(22, 23)
obj.coord()