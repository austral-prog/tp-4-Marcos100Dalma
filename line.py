def line():
    A = input("Ingrese el coeficiente A: ")
    B = input("Ingrese el coeficiente B: ")
    X1 = input("Ingrese el coeficiente X1: ")
    X2 = input("Ingrese el coeficiente X2: ")
    A = float(A)
    B = float(B)
    X1 = float(X1)
    X2 = float(X2)
    print("El coeficiente A de su ecuación de la recta es: " + str(A))
    print("El coeficiente B de su ecuación de la recta es: " + str(B))
    print("El coeficiente X1 de su ecuación de la recta es: " + str(X1))
    print("El coeficiente X2 de su ecuación de la recta es: " + str(X2))
    print(f"""\nPara la siguiente ecuación:
\tY = {A}X + {B}""")
    Y1 = (A*X1) + B
    Y2 = (A*X2) + B
    print(f"""\nDados los siguientes puntos:
\tP1 ({X1}, {Y1})
\tP2 ({X2}, {Y2})""")
    D = ((X2 - X1)**2 + (Y2 - Y1)**2)**(1/2)    
    print()
    print("La distancia entre ellos es: " + str(float(D)))
