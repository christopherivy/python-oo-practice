"""Python serial number generator."""
# print(serialf)


from random import randint
from math import sqrt


class SerialGenerator:

    """Machine to create unique incrementing serial numbers.


        >>> serial = SerialGenerator(start=100)

        >>> serial.generate()
        100

        >>> serial.generate()
        101

        >>> serial.generate()
        102

        >>> serial.reset()

        >>> serial.generate()
        100
    """

    def __init__(self, start=0):
        """Make a new generator, starting at start."""
        self.start = self.next = start

    def __repr__(self):
        """ show representation """
        return f"<SerialGenerator start={self.start} next = {self.next}>"

    def generate(self):
        """ return next serial """
        self.next += 1
        return self.next - 1

    def reset(self):
        """ reset number to original start """
        self.next = self.start


serial = SerialGenerator(54)
print(serial.generate())


# -------------------------------------------------------------------------------------------
# # class Triangle:
# #     # you have to use self in place of .this
# #    #  __init__ needs to be there. it is like constructor on classes
# #     def __init__(self, a, b):
# #         self.a = a
# #         self.b = b
# #     def get_hypot(self):
# #         return sqrt(self.a ** 2 + self.b ** 2)
# #     def get_area(self):
# #         return self.a * self.b / 2
# # --------------class methods------------------
# rand_num1 = randint(1, 20)
# rand_num2 = randint(1, 20)


# class Triangle:

#     """
#        A class used to represent a right triangle

#        Attributes
#        ---------------
#        a: int length of side a
#        b: int length of side b
#        """
#     # you have to use self in place of .this
#     #  __init__ needs to be there. it is like constructor on classes

#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def __repr__(self):
#         return f"Triangle(a={self.a}, b={self.b})"

#     def __str__(self):
#         return self.describe()

#     def __eq__(self, other):
#         return self.a == other.a and self.b == other.b

#     # this part of the code is a function factory
#     @classmethod
#     def random(cls):
#         """ Class method which returns Triangle with random sides """
#         # return cls(rand_num1, rand_num2)
#         print(cls)

#     def get_hypot(self):
#         """ Calcualtes Hypot (3rd side of right triangle) """
#         return sqrt(self.a ** 2 + self.b ** 2)

#     def get_area(self):
#         """ Calcualtes area of right triangle) """
#         return self.a * self.b / 2

#     # this msg is being called via super below
#     def describe(self):
#         """ returns string representing triangle """
#         return f"I am a triangle with sides: {self.a} & {self.b}."


# # --------------inheritance------------------

# class ColoredTriangle(Triangle):

#     def __init__(self, a, b, color):
#         super().__init__(a, b)
#         self.color = color

#     # super works here bcuz the ColoredTri... class has access to Triangle above

#     def describe(self):

#         #  msg is super(higher class) and the method of Triangle
#         msg = super().describe()
#         return msg + f"I am {self.color}"


# # --------------documenting instances------------------


# # --------------dunder methods------------------
# #  on lines 42 and 45


# # *********************************************************************

# # *********************************************************************

# class SerialGenerator:

#     def __init__(self, start=0):
#         self.start = self.next = start

#     def generate_num(self):
#         self.next += 1
#         return self.next + 1

#     """Machine to create unique incrementing serial numbers.


#         >>> serial = SerialGenerator(start=100)

#         >>> serial.generate()
#         100

#         >>> serial.generate()
#         101

#         >>> serial.generate()
#         102

#         >>> serial.reset()

#         >>> serial.generate()
#         100
#     """


# sg = SerialGenerator()
# print(sg.start, sg.next)
# sg.generate_num()
# print(sg.next)
