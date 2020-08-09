# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 05:57:17 2020

@author: HP
"""

import random
import string

Letters = string.ascii_letters
Numbers = '0123456789'
Special_chars = '+-*&%$!#^_'
Symbols = Letters + Numbers + Special_chars

length = int(input("Enter password length:"))
password = ''.join(random.sample(Symbols,length))

print(password)