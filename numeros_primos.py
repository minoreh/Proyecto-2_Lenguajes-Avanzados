# -*- coding: utf-8 -*-

fin=0
while fin<2:
    print("Por favor digita un numero entero: ")
    num= input()

    if num.isdigit():
        num = int(num)
        break
    else:
        print("ERROR: DEBE INGRESAR UN NUMERO ENTERO")
        fin=1