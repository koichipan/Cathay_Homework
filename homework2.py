# This is Migo Coding Test for question2 : Shape Inheritance
# Used Python
# By Patrick Pan

from abc import  ABCMeta


class Shape(metaclass=ABCMeta):

    def getArea(self):
        pass

    def getPerimeter(self):
        pass

    def printMessage(self, string):
        print(string)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.mylength = length
        self.mywidth = width
        self.area = 0
        self.perimeter = 0

    def getArea(self):
        self.area = self.mylength * self.mywidth
        msg = 'Finding area of rectangle with length = %s and width = %s' % (self.mylength, self.mywidth)
        print(msg)
        return self.area

    def getPerimeter(self):
        self.perimeter = 2 * (self.mylength + self.mywidth)
        msg = 'Finding perimeter of rectangle with length = %s and width = %s' % (self.mylength, self.mywidth)
        print(msg)
        return self.perimeter

    def toString(self):
        msg = 'Rectangle = [length: %s, width: %s, area: %s, perimeter: %s]' % (self.mylength, self.mywidth, self.area, self.perimeter)
        return msg


class Square(Rectangle):
    def __init__(self, side):
        self.mylength = side
        self.mywidth = side
        self.side = side

    def getArea(self):
        msg = 'Finding area of square with side = %s' % self.side
        print(msg)
        return super().getArea()

    def getPerimeter(self):
        msg = 'Finding perimeter of square with side = %s' % self.side
        return super().getPerimeter()

    def toString(self):
        msg = 'Square = [side: %s, area: %s, perimeter: %s]' % (self.side, self.area, self.perimeter)
        return msg


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.area = 0
        self.perimeter = 0

    def getArea(self):
        msg = 'Finding area of circle with radius = %s' % self.radius
        print(msg)
        self.area = 3.14 * self.radius * self.radius
        return self.area

    def getPerimeter(self):
        msg = 'Finding perimeter of circle with radius = %s' % self.radius
        print(msg)
        self.perimeter = 6.28 * self.radius
        return self.perimeter

    def toString(self):
        msg = 'Circle = [radius: %s, area: %s, perimeter: %s]' % (self.radius, self.area, self.perimeter)
        return msg


if __name__ == "__main__":
    rectangle = Rectangle(2, 3)
    square = Square(2)
    circle = Circle(2)

    msg1 = str(rectangle.getArea()) + " " + str(rectangle.getPerimeter())
    msg2 = str(square.getArea()) + " " + str(square.getPerimeter())
    msg3 = str(circle.getArea()) + " " + str(circle.getPerimeter())

    Shape().printMessage(msg1)
    Shape().printMessage(msg2)
    Shape().printMessage(msg3)

    Shape().printMessage(str(rectangle.toString()))
    Shape().printMessage(str(square.toString()))
    Shape().printMessage(str(circle.toString()))

