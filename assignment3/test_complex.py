#!/usr/bin/env python
# -*- coding: utf-8 -*-

from complex import *


class Test_complex:
    """Test units to confirm the different methods in Complex(). 

    The tests is suppose to verify that adding, subtracting and multiplicating two complex numbers returns
    what it’s supposed to. Modulus, conjugate and the equal method is also tested. 

    The first tests checks the different methods separately, and the last tests the methods is combined. 
    The complex numbers that is tested is varieted. Only real part, only imaginary part and combined. Testing only integer to avoid rounding errors. 
    """

    def test_add_1(self):
        """Test 1 addition"""

        z = Complex(1, 2)
        w = Complex(0, 3)
        assert z + w == Complex(1, 5)

    def test_add_2(self):
        """Test 2 addition"""

        z = Complex(1, 0)
        w = Complex(0, 3)
        assert z + w == Complex(1, 3)

    def test_add_3(self):
        """Test 3 addition"""

        z = Complex(5, 2)
        w = Complex(3, 3)
        assert z + w == Complex(8, 5)

    def test_sub_1(self):
        """Test 1 subtraction"""

        z = Complex(5, 2)
        w = Complex(3, 3)
        assert z - w == Complex(2, -1)

    def test_sub_2(self):
        """Test 2 subtraction"""

        z = Complex(0, 1)
        w = Complex(0, 10)
        assert z - w == Complex(0, -9)

    def test_sub_3(self):
        """Test 3 subtraction"""

        z = Complex(15, 0)
        w = Complex(-20, -7)
        assert z - w == Complex(35, 7)

    def test_mul_1(self):
        """Test 1 multiplication"""

        z = Complex(0, 2)
        w = Complex(2, 0)
        assert z * w == Complex(0, 4)

    def test_mul_2(self):
        """Test 2 multiplication"""

        z = Complex(0, 1)
        w = Complex(0, 10)
        assert z * w == Complex(-10, 0)

    def test_mul_3(self):
        """Test 3 multiplication"""

        z = Complex(2, 2)
        w = Complex(4, 5)
        assert z * w == Complex(-2, 18)

    def test_conjugate_1(self):
        """Test 1 conjugate"""

        z = Complex(0, 2)
        assert z.conjugate() == Complex(0, -2)

    def test_conjugate_2(self):
        """Test 2 conjugate"""

        z = Complex(15, 27)
        assert z.conjugate() == Complex(15, -27)

    def test_conjugate_3(self):
        """Test 3 conjugate"""

        z = Complex(7, 0)
        assert z.conjugate() == Complex(7, 0)

    def test_modulus_1(self):
        """Test 1 modulus"""

        z = Complex(0, 3)
        assert z.modulus() == 3

    def test_modulus_2(self):
        """Test 2 modulus"""

        z = Complex(5, 0)
        assert z.modulus() == 5

    def test_modulus_3(self):
        """Test 3 modulus"""

        z = Complex(1, 4)
        assert z.modulus() == math.sqrt(17)

    def test_eq_1(self):
        """Test 1 equal"""

        z = Complex(1, 4)
        w = Complex(4, 1)
        assert z != w

    def test_eq_2(self):
        """Test 2 equal"""

        z = Complex(0, 1)
        w = Complex(0, 1)
        assert z == w

    def test_eq_3(self):
        """Test 3 equal"""

        z = Complex(5, 5)
        w = Complex(5, 5)
        assert z == w

    def test_rsub_1(self):
        """Test 1 reverse subtracting"""

        assert 4 - Complex(3, 4) == Complex(1, -4)

    def test_rsub_2(self):
        """Test 2 reverse subtracting"""

        assert -1 - Complex(3, 4) == Complex(-4, -4)

    def test_rsub_3(self):
        """Test 3 reverse subtracting"""

        assert -2 - Complex(0, 4) == Complex(-2, -4)

    def test_rmul_1(self):
        """Test 1 reverse multiplication"""

        assert 4 * Complex(3, 4) == Complex(12, 16)

    def test_rmul_2(self):
        """Test 2 reverse multiplication"""

        assert 4 * Complex(0, 4) == Complex(0, 16)

    def test_rmul_3(self):
        """Test 3 reverse multiplication"""

        assert 4 * Complex(3, 0) == Complex(12, 0)

    def test_radd_1(self):
        """Test 1 reverse addition"""

        assert 4 + Complex(3, 4) == Complex(7, 4)

    def test_radd_2(self):
        """Test 2 reverse addition"""

        assert 4 + Complex(-3, 0) == Complex(1, 0)

    def test_radd_3(self):
        """Test 3 reverse addition"""

        assert 4 + Complex(0, 1) == Complex(4, 1)

    def test_comp_1(self):
        """Test 1 builtin complex"""

        assert complex(2, 3) == Complex(2, 3)

    def test_comp_2(self):
        """Test 2 builtin complex"""

        assert complex(0, 1) == Complex(0, 1)

    def test_comp_3(self):
        """Test 3 builtin complex"""

        assert complex(0, 0) == Complex(0, 0)

    def test_combined_1(self):
        """ Test combined methods 1"""

        assert 4 * Complex(3, 4) - 2 == Complex(10, 16)

    def test_combined_2(self):
        """ Test combined methods 2"""

        assert Complex(2, 3) + complex(2, 2) == Complex(4, 5)

    def test_combined_3(self):
        """ Test combined methods 3"""
        assert complex(2, 2) - Complex(2, 3) == Complex(0, -1)

    def test_combined_4(self):
        """ Test combined methods 4"""
        assert Complex(5, 3) * complex(4, 1) == Complex(17, 17)
