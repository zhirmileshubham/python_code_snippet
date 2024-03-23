'''
Calculate Area of rectangle
'''

class Rectangle:
    def __init__(self, len, wed):
        self.len = len
        self.wid = wid
        
    def area(self):
        return self.len * self.wid
    

len = float(input('Enter length of the rectangle :'))
wid = float(input("Enter width of the rectangle :"))

rectangle_area = Rectangle(len, wid)

print("Area of rectangle is", rectangle_area.area())