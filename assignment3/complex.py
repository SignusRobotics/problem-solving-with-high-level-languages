#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


class Complex:
    """class Complex containing the rules how to handle calculation for a complex number.

    A complex number contains 2 parts, a + b*i, where a is the real number and b is the imaginary number. a can be 0.

    Args:
        a (int/float): the real part of the complex number.
        b (int/float): the imaginary part of the complex number. Default value = 0.0.

    """

    def __init__(self, a, b=0.0):

        self.a = a
        self.b = b

    # Assignment 3.3

    def conjugate(self):
        """Return conjugate of the complex number a+ib

        """
        return Complex(self.a, -self.b)

    def modulus(self):
        """Find the modulus of the complex number.

        """
        sqr_length = (self.a**2) + (self.b**2)
        length = math.sqrt(sqr_length)
        return length

    def __add__(self, other):
        """Addition between the complex number and another.

        Converts int and builtin complex function to Complex().

        Args:
            other (Complex, int/float or builtin function complex): Could be a Complex() object, int/float or a builtin complex object.

        """
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif isinstance(other, complex):
            other = Complex(other.real, other.imag)
        new_a = self.a + other.a
        new_b = self.b + other.b
        return Complex(new_a, new_b)

    def __sub__(self, other):
        """Subtraction between the complex number and another.

        Converts int and builtin complex function to Complex().

        Args:
            other (Complex, int/float or builtin function complex): Could be a Complex() object, int/float or a builtin complex object.

        """
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif isinstance(other, complex):
            other = Complex(other.real, other.imag)
        new_a = self.a - other.a
        new_b = self.b - other.b
        return Complex(new_a, new_b)

    def __mul__(self, other):
        """Multiplication between the complex number and another. 

        Converts int and builtin complex function to Complex(). 

        Args: 
            other (Complex, int/float or builtin function complex): Could be a Complex() object, int/float or a builtin complex object. 

        """
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif isinstance(other, complex):
            other = Complex(other.real, other.imag)
        # if other == (int):
        #    return Complex(self.a*other, self.b)
        # else:
        new_a = (self.a * other.a) - (self.b*other.b)
        new_b = (self.a * other.b) + (other.a * self.b)
        return Complex(new_a, new_b)

    def __eq__(self, other):
        """Checks if to complex number is equal.  

        Args: 
            other (Complex, int/float or builtin function complex): Could be a Complex() object, int/float or a builtin complex object. 

        """
        if isinstance(other, complex):
            return self.a == other.real and self.b == other.imag
        return self.a == other.a and self.b == other.b

    # Assignment 3.4
    def __radd__(self, other):
        """Reverse addition between the complex number and another.

        Converts int and builtin complex function to Complex().

        Args:
            other (Complex, int/float or builtin function complex): Could be a Complex() object, int/float or a builtin complex object.

        """
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif isinstance(other, complex):
            other = Complex(other.real, other.imag)
        return self.__add__(other)

    def __rmul__(self, other):
        """Reverse multiplication between the complex number and another.

        Converts int and builtin complex function to Complex().

        Args:
            other (Complex, int/float or builtin function complex): Could be a Complex() object, int/float or a builtin complex object.

        """
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif isinstance(other, complex):
            other = Complex(other.real, other.imag)
        return self.__mul__(other)

    def __rsub__(self, other):
        """Reverse subtraction between the complex number and another.

        Converts int and builtin complex function to Complex().

        Args:
            other (Complex, int/float or builtin function complex): Could be a Complex() object, int/float or a builtin complex object.

        """
        if isinstance(other, (float, int)):
            other = Complex(other)
        elif isinstance(other, complex):
            other = Complex(other.real, other.imag)

        return other.__sub__(self)

    # Optional, possibly useful methods

    # Allows you to write `-a`

    def __neg__(self):
        pass

    # Make the `complex` function turn this into Python's version of a complex number
    def __complex__(self):
        """Pythons version of a complex number. 

        """
        return complex(self.a, self.b)
