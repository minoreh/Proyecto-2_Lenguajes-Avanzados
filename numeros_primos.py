# -*- coding: utf-8 -*-
a=0
fin=0
while fin<2:
    print("Por favor digita un numero entero: ")
    num= input()
    if num.isdigit():
        num = int(num)
        if int(num) == 0:
            print("ERROR: el numero digitado NO debe ser CERO")
            break
        for i in range(1, num + 1):
            if (num % i == 0):
                a = a + 1
        if (a != 2):
            print(str(num) +" Tu numero No es primo")
        else:
            print(str(num) +" Tu numero Si es primo")
        pass
        if (num % 2 == 0):
            print(str(num) + " es un numero par")
            pass
        else:
            print(str(num) + " es un numero impar")
            pass

    else:
        print(">ERROR: DEBE INGRESAR UN NUMERO ENTERO")
        print(">NO DEBE INGRESAR NUMEROS NEGATIVOS O CARACTERES")
        fin=1