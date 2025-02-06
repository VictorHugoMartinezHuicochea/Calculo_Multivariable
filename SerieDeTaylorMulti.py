#Escuela Superior de Fisico y Matematicas
#Licenciatura En Matematica Algoritmica
#Cualculo Multivareable
#Series de Taylor En Dos Variables
#Profesor: Jorge Aguilar Guzman
#Equipo:
    #Brandon Alexis Trejo Cortes
    #Victor Hugo Martinez Huicochea


import math
import sympy

def Comb(n,r,a,b):
    for i in range(0, n+1):
        if i!=0:
            print("+")
        k=n-i
        print(math.comb(n, k),"*{",sympy.diff(r,x,i,y,k),"}*([x-",a,"]**",i,")([y-",b,"]**",k,")")



if __name__ == "__main__":
    print("Bienvenido a la Serie de Taylor para dos variables \n Por favor digite su funcion")
    x,y=sympy.symbols('x y')
    func_str = input("Favor de insertar su funcion:  \n IMPORTANTE: Cuando multiplique escriba el signo * (Ejemplo: xy = x*y)\n Cuando escriba una potencia escribir ** (Ejemplo: e^(xy)=e**(x*y)\n El seno escribirlo como sin() y coseno escribirlo como cos()\nFuncion:")
    try:
        r = sympy.sympify(func_str)
    except:
        print("Error al evaluar la función.")
        exit(1)
    
    #Ejemplos de muestra
    # r=sympy.exp(y**2+x**2)
    # r=x*(y**4)
    print("Ok, su función es:")
    print(r)
    print("Por favor digite la cantidad de derivaciones a hacer")
    n=(int(input()))
    print("Por favor digite la coordenadas sobre las que se regira el entorno de la función en:")
    a=(float(input("X:" )))
    b=(float(input("Y:" )))
    
    print("Ok, la serie de Taylor es expresado en polinomos es: \n")
    print(r)
    for i in range(1,n+1):
        print("+1/",math.factorial(i),"*[")
        Comb(i,r,a,b)
        print("]")
