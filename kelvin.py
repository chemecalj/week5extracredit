#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This program will calculate the temperatures of K to F, K to C, and C to F"""

def kel_fah_cel(kelvin, multi=1.8, subtract_a=459.67, subtract_b=273.15, addition=32):
    """This function provides all my values for my arguments.

    Args:
    kelvin (int): Random value used to make all calulations.
    multi (int): Value used in formauls for K to F and K to C. Default 1.8
    subtract_a (int): Value used in formula for K to F. Default: 459.67
    subtract_b (int): Value used in formula K to C. Default: 273.15
    addition (int): Value used in formaula for C to F. Default: 32

    Returns:
    int: Returns the values of the temperature calculations.

    Examples:
    >>> kel_fah_cel(300)
    ('80.33', '26.85', '80.33')

    >>> kel_fah_cel(350)
    ('170.33', '76.85', '170.33')

    >>> kel_fah_cel(400)
    ('260.33', '126.85', '260.33')
    
    """
            
    kel_fah = (kelvin * multi - subtract_a)
    kel_cel = (kelvin - subtract_b)
    cel_fah = (kel_cel * multi + addition)
    return format(kel_fah, '2.2f'), format(kel_cel, '2.2f'), format(cel_fah, '2.2f')
