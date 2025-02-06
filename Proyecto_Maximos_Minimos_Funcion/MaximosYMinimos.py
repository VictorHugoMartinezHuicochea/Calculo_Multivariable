#Escuela Superior de Fisico y Matematicas
#Licenciatura En Matematica Algoritmica
#Calculo Multivariable
#Maximos y Minimos
#Profesor: Jorge Aguilar Guzman
#Alumno:
    #Victor Hugo Martinez Huicochea

#Importamos librerias
import sympy
import numpy
import copy

def Pos(hep):
    #Determinamos su naturaleza
    Eig=numpy.linalg.eigvals(hep)
    
    Pos=True
    
    if(Eig[0]>0):
        for i in range(0,len(Eig)):
            if(Eig[i]<0):
                Pos=False
            Punt=1
    else:
        for i in range(0,len(Eig)):
            if(Eig[i]>0):
                Pos=False
            Punt=2
    #Determinamos de que tipo es
    if(Pos==False):
        print("Es punto silla en el Punto:")
    elif(Punt==1):
        print("Es un punto minimo en el Punto:")
    elif(Punt==2):
        print("Es un punto maximo en el Punto:")
    else:
        print("Mi metodo no puede responder correctamente al punto:")

    #Damos solucion
    feval=copy.deepcopy(f)
    print("F(",end=" ")
    for i in range(0,numvar):
        print(fs[i][k],end=",")
    print(")=",end=" ")
    for i in range(0,numvar):
        feval=sympy.sympify(feval).subs(namevar[i],fs[i][k])
    print(feval,"\n\n\n")

def Det(hep):
    #Determinamos su naturaleza
    D=numpy.linalg.det(hep)
    #Determinamos que tipo de punto es
    if(D<0):
        print("Es punto silla en el Punto:")
    elif(D>0):
        if(dxx>0):
            print("Es un punto minimo en el Punto:")
        elif(dxx<1):
            print("Es un punto maximo en el Punto:")
        else:
            print("Mi metodo no puede responder correctamente")
    else:
        print("Mi metodo no puede responder correctamente al punto:")
    #Damos solucion
    feval=copy.deepcopy(f)
    print("F(",end=" ")
    for i in range(0,numvar):
        print(fs[i][k],end=",")
    print(")=",end=" ")
    for i in range(0,numvar):
        feval=sympy.sympify(feval).subs(namevar[i],fs[i][k])
    print(feval,"\n\n\n")
    
    
    
if __name__ == "__main__":
    #Dimensionamos en que R^n trabajaremos para crear las 
    print("Por favor digite su numero de variables")
    numvar=int(input())
    namevar=[]
    print("Digite el nombre de sus variables:\n")
    for i in range (0,numvar):
        print("Variable",i+1,":")
        namevar.append(input())
    
    #Los convertimos a simbolos que python pueda interpretar como variables
    for i in range (0,numvar):
        namevar[i]=sympy.symbols(namevar[i])
        
    
    
    #Pedimos la funcion
    func_str = input("Favor de insertar su funcion:  \n IMPORTANTE: Cuando multiplique escriba el signo * (Ejemplo: xy = x*y)\n Cuando escriba una potencia escribir ** (Ejemplo: e^(xy)=e**(x*y)\n El seno escribirlo como sin() y coseno escribirlo como cos()\nFuncion:\n")
    f= sympy.sympify(func_str) 

    
    grad=[]
    #Creacion Gradiente
    for i in range (0,numvar):
        g=sympy.diff(f,namevar[i],1)
        grad.append(g)
    
    #Resolvemos el gradiente
    try:
        gs=sympy.solve(grad,namevar,dict=True)
    except:
        print("Error al resolver funcion, puede que no haya respuesta o este mal el problema o el programa no abarce la solucion")
        exit(1)
    fs=[]
    for i in range (0,numvar):
        xs=[solution[namevar[i]] for solution in gs]
        fs.append(xs)
    
    
    
    
    
    #Creamos la matriz Hessiana
    hes=[]
    for i in range (0,numvar):
        hp=[]
        for j in range(0,numvar):
            g=sympy.diff(grad[i],namevar[j],1)
            hp.append(g)
        hes.append(hp)
    
    
    
    
    #Determinamos el metodo a usar
    print("Por Favor Digite Que Metodo usar:")
    print("Mediante Determinantes de la Hessiana (1) o Mediante si es Definida Positiva o Negativa(2)")
    met=int(input("Metodo:"))
    
    
    
    
    #Empezamos a Evaluar en cada punto critico dado
    print("Iniciamos Evaluacion\n")
    for k in range(0,len(fs[0])):
        hep=copy.deepcopy(hes)
        
        ###Evaluamos el hesiano en el punto critico
        for i in range (0,numvar):
            for j in range(0,numvar):
                for l in range(0,numvar):
                    hep[i][j]=sympy.sympify(hep[i][j]).subs(namevar[l],fs[l][k])
                #Guardamos para determinar si es maximo o minimo
                if(i==0 and j==0):
                    dxx=float(hep[i][j])
        
        #Lo convertimos a punto flotante para poder operar
        for i in range(0,numvar):
            for j in range(0,numvar):
                hep[i][j]=float(hep[i][j])
    
        #Determinamos su naturaleza
        if(met==1):
            print("Usted ha decidido mediante Determinantes de la Hessiana: \n Calculando...")
            Det(hep)
        elif(met==2):
            print("Usted ha decidido mediante Definida de la Hessiana: \n Calculando...")
            Pos(hep)
    print("Fin del Programa :D")