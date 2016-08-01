# -*- coding: utf-8 -*-
from pip._vendor.distlib.compat import raw_input

while 1:
    num = raw_input("Escribe un numero entero: ")
    if num.isdigit():
        num = int(num)
    break
