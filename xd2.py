from math import sqrt, cos, pi, sin, radians
from random import uniform as randfloat
from random import seed as semilla
import os

#permutacion 1    
def Formula_mayores_permutacion1(qi,archivo1,epsilon1,fi1):
    archivo = open(archivo1, "r")
    nuevo = open("process_files/file_permutation1.dump", "w")
    x =y=z = 0
    lineac = 0
    datos =[]
    nocubico = []
    ID = 0
    n = len(qi)
    for linea in archivo:
        lineac += 1
        valor = 0
        r = linea.split(" ")
        if lineac < 10:
            datos.append(linea)
            if lineac == 6:
                x = float(r[1].rstrip()) - float(r[0])
            elif lineac == 7:
                y = float(r[1].rstrip()) - float(r[0])
            elif lineac == 8:
                z = float(r[1].rstrip()) - float(r[0])
                nocubico = nocubicos(x,y,z,90,90,90)
        elif lineac > 9:
            for j in range(n):
                valor += cos((qi[j][0]*((2*pi)/nocubico[0])*float(r[2]) + (qi[j][1]*((2*pi)/nocubico[1])*float(r[3]) + (qi[j][2]*((2*pi)/nocubico[2])*float(r[4]) + fi1[j]))))#fi
            norm = sqrt(2/n)
            valor = valor * norm
            if epsilon1 < valor:
                ID += 1
                texto = f"{ID} {r[1]} {r[2]} {r[3]} {r[4]}"
                datos.append(texto)
    datos[3] = str(ID) + "\n"
    for i in range(0, len(datos)):
        if i<9:
            nuevo.write(datos[i])
        else:
            nuevo.write(datos[i].rstrip())
            if i != len(datos) - 1:
                nuevo.write("\n")


    archivo.close()
    nuevo.close()



#permutacion 2    
def Formula_mayores_permutacion2(qi,archivo2,epsilon2,fi2):
    archivo = open(archivo2, "r")
    nuevo = open("process_files/file_permutation2.dump", "w")
    x =y=z = 0
    lineac = 0
    datos =[]
    nocubico = []
    ID = 0
    n = len(qi)
    for linea in archivo:
        lineac += 1
        valor = 0
        r = linea.split(" ")
        if lineac < 10:
            datos.append(linea)
            if lineac == 6:
                x = float(r[1].rstrip()) - float(r[0])
            elif lineac == 7:
                y = float(r[1].rstrip()) - float(r[0])
            elif lineac == 8:
                z = float(r[1].rstrip()) - float(r[0])
                nocubico = nocubicos(x,y,z,90,90,90)
        elif lineac > 9:
            for j in range(n):
                valor += cos((qi[j][0]*((2*pi)/nocubico[0])*float(r[2]) + (qi[j][1]*((2*pi)/nocubico[1])*float(r[3]) + (qi[j][2]*((2*pi)/nocubico[2])*float(r[4]) + fi2[j]))))#fi
            norm = sqrt(2/n)
            valor = valor * norm
            if epsilon2 < valor:
                ID += 1
                texto = f"{ID} {r[1]} {r[2]} {r[3]} {r[4]}"
                datos.append(texto)
    datos[3] = str(ID) + "\n"
    for i in range(0, len(datos)):
        if i<9:
            nuevo.write(datos[i])
        else:
            nuevo.write(datos[i].rstrip())
            if i != len(datos) - 1:
                nuevo.write("\n")


    archivo.close()
    nuevo.close()


    

def Formula_menores_permutacion1(qi,archivo1,epsilon1,fi1):
    archivo = open(archivo1, "r")
    nuevo = open("process_files/file_permutation1.dump", "w")
    x =y=z = 0
    lineac = 0
    datos =[]
    nocubico = []
    ID = 0
    n = len(qi)
    for linea in archivo:
        lineac += 1
        valor = 0
        r = linea.split(" ")
        if lineac < 10:
            datos.append(linea)
            if lineac == 6:
                x = float(r[1].rstrip()) - float(r[0])
            elif lineac == 7:
                y = float(r[1].rstrip()) - float(r[0])
            elif lineac == 8:
                z = float(r[1].rstrip()) - float(r[0])
                nocubico = nocubicos(x,y,z,90,90,90)
        elif lineac > 9:
            for j in range(n):
                valor += cos((qi[j][0]*((2*pi)/nocubico[0])*float(r[2]) + (qi[j][1]*((2*pi)/nocubico[1])*float(r[3]) + (qi[j][2]*((2*pi)/nocubico[2])*float(r[4]) + fi1[j]))))#fi
            norm = sqrt(2/n)
            valor = valor * norm
            if epsilon1 > valor:
                ID += 1
                texto = f"{ID} {r[1]} {r[2]} {r[3]} {r[4]}"
                datos.append(texto)
    datos[3] = str(ID) + "\n"
    for i in range(0, len(datos)):
        if i<9:
            nuevo.write(datos[i])
        else:
            nuevo.write(datos[i].rstrip())
            if i != len(datos) - 1:
                nuevo.write("\n")


    archivo.close()
    nuevo.close() 

def Formula_menores_permutacion2(qi,archivo2,epsilon2,fi2):
    archivo = open(archivo2, "r")
    nuevo = open("process_files/file_permutation2.dump", "w")
    x =y=z = 0
    lineac = 0
    datos =[]
    nocubico = []
    ID = 0
    n = len(qi)
    for linea in archivo:
        lineac += 1
        valor = 0
        r = linea.split(" ")
        if lineac < 10:
            datos.append(linea)
            if lineac == 6:
                x = float(r[1].rstrip()) - float(r[0])
            elif lineac == 7:
                y = float(r[1].rstrip()) - float(r[0])
            elif lineac == 8:
                z = float(r[1].rstrip()) - float(r[0])
                nocubico = nocubicos(x,y,z,90,90,90)
        elif lineac > 9:
            for j in range(n):
                valor += cos((qi[j][0]*((2*pi)/nocubico[0])*float(r[2]) + (qi[j][1]*((2*pi)/nocubico[1])*float(r[3]) + (qi[j][2]*((2*pi)/nocubico[2])*float(r[4]) + fi2[j]))))#fi
            norm = sqrt(2/n)
            valor = valor * norm
            if epsilon2 > valor:
                ID += 1
                texto = f"{ID} {r[1]} {r[2]} {r[3]} {r[4]}"
                datos.append(texto)
    datos[3] = str(ID) + "\n"
    for i in range(0, len(datos)):
        if i<9:
            nuevo.write(datos[i])
        else:
            nuevo.write(datos[i].rstrip())
            if i != len(datos) - 1:
                nuevo.write("\n")


    archivo.close()
    nuevo.close()

def aleacion1(archivo1, nombre_resultante, nombre_variables):
    with open("process_files/" + archivo1, "r") as archivo1:
        with open("results/" + nombre_resultante, "w") as nuevo:
            contador1 = 0
            tipo = 0
            final_primer_archivo = False  # Bandera para indicar el final del primer archivo
            cantidad_archivo1 = 0
            ultimo_id = 0

            for linea in archivo1:
                contador1 += 1
                if contador1 == 4:
                    # Leer la cantidad de átomos en el archivo
                    cantidad_archivo1 = int(linea)
                    ultimo_id = cantidad_archivo1

                    with open("results/" + nombre_variables + ".log", "a") as variables:
                        variables.write("Total Atoms: " + str(ultimo_id) + "\n")
                        variables.write("Core File Percentage: 100.0%\n")
                        variables.write("Shell File Percentage: 0.0%\n")

                    nuevo.write(str(cantidad_archivo1) + "\n")

                if contador1 <= 9 and contador1 != 4:
                    # Procesar las líneas antes de la línea 9
                    if contador1 in (6, 7, 8):
                        caja1 = linea.split()
                        caja_mayor = caja1[0] + " " + caja1[1]
                        nuevo.write(caja_mayor + "\n")
                    else:
                        nuevo.write(linea)

                if contador1 > 9:
                    # Procesar las líneas a partir de la línea 10
                    valores = linea.split()
                    tipo_actual = int(valores[1])
                    if tipo_actual > tipo:
                        tipo = tipo_actual
                    nuevo.write(linea)

                if contador1 == 9:
                    # Marcar el final del archivo para el procesado adicional
                    final_primer_archivo = True

            if final_primer_archivo:
                nuevo.write("\n")

def aleacion2(archivo2, nombre_resultante2, nombre_variables2):
    with open("process_files/" + archivo2, "r") as archivo1:
        with open("results/" + nombre_resultante2, "w") as nuevo:
            contador1 = 0
            tipo = 0
            final_primer_archivo = False  # Bandera para indicar el final del primer archivo
            cantidad_archivo1 = 0
            ultimo_id = 0

            for linea in archivo1:
                contador1 += 1
                if contador1 == 4:
                    # Leer la cantidad de átomos en el archivo
                    cantidad_archivo1 = int(linea)
                    ultimo_id = cantidad_archivo1

                    with open("results/" + nombre_variables2 + ".log", "a") as variables:
                        variables.write("Total Atoms: " + str(ultimo_id) + "\n")
                        variables.write("Core File Percentage: 100.0%\n")
                        variables.write("Shell File Percentage: 0.0%\n")

                    nuevo.write(str(cantidad_archivo1) + "\n")

                if contador1 <= 9 and contador1 != 4:
                    # Procesar las líneas antes de la línea 9
                    if contador1 in (6, 7, 8):
                        caja1 = linea.split()
                        caja_mayor = caja1[0] + " " + caja1[1]
                        nuevo.write(caja_mayor + "\n")
                    else:
                        nuevo.write(linea)

                if contador1 > 9:
                    # Procesar las líneas a partir de la línea 10
                    valores = linea.split()
                    tipo_actual = int(valores[1])
                    if tipo_actual > tipo:
                        tipo = tipo_actual
                    nuevo.write(linea)

                if contador1 == 9:
                    # Marcar el final del archivo para el procesado adicional
                    final_primer_archivo = True

            if final_primer_archivo:
                nuevo.write("\n")

def func_calculos1(permutaciones1, valor_x1, valor_y1, valor_z1):
        return permutaciones1[0] >= valor_x1 and permutaciones1[1] >= valor_y1 and permutaciones1[2] >= valor_z1

def func_calculos2(permutaciones1, valor_x1, valor_y1, valor_z1):
        return permutaciones1[0] >= valor_x1 and permutaciones1[1] >= valor_y1 and permutaciones1[2] >= valor_z1

def numerosiniciales1(H,H2,nombre_variables1,valor_x1,valor_y1,valor_z1):
    x = y = z = 0
    permutaciones=[]
    semilla(2)
    N=0
    print(valor_x1, valor_y1, valor_z1)  # Para revisar los valores antes de procesar
    for x in range(-H2,H2+1):
        for y in range(-H2,H2+1):
            for z in range(-H2,H2+1):
                h=((x**2)+(y**2)+(z**2))
                if h==H**2:
                    N=N+1
                    permutaciones.append((x,y,z))


    variables = open("results/"+nombre_variables1+".log", "a")
    random_seed = "Random Seed: "+str(2)+"\n"
    variables.write(random_seed)
    variables.close()
    n_permutaciones = list(filter(lambda tup: func_calculos1(tup,valor_x1,valor_y1,valor_z1),permutaciones))
    print("LAVOLA", n_permutaciones)
    return n_permutaciones



def numerosiniciales2(H,H2,nombre_variables2,valor_x2,valor_y2,valor_z2):
    x = y = z = 0
    permutaciones=[]
    semilla(2)
    N=0
    print(valor_x2, valor_y2, valor_z2)  # Para revisar los valores antes de procesar
    for x in range(-H2,H2+1):
        for y in range(-H2,H2+1):
            for z in range(-H2,H2+1):
                h=((x**2)+(y**2)+(z**2))
                if h==H**2:
                    N=N+1
                    permutaciones.append((x,y,z))


    variables = open("results/"+nombre_variables2+".log", "a")
    random_seed = "Random Seed: "+str(2)+"\n"
    variables.write(random_seed)
    variables.close()
    n_permutaciones = list(filter(lambda tup: func_calculos2(tup,valor_x2,valor_y2,valor_z2),permutaciones))
    return n_permutaciones

#funcion no cubica                                                                                                                                
def nocubicos(a,b,c,alpha,beta,gama):
    matriz = []
    matriz.append(a)
    matriz.append(b*sin(radians(gama)))
    matriz.append(c*(sqrt(1-(cos(radians(alpha))**2-2*(cos(radians(beta))**2)+2*(cos(radians(alpha))*cos(radians(beta))*cos(radians(gama)))))/sin(radians(gama))))
    return matriz


#para permutacion 1
def crear_fi1(nueva_lista1):
    n = len(nueva_lista1)
    fi1 = []
    for i in range(0,n):
        fi1.append(randfloat(0, 2*pi))
    return fi1


def crear_fi2(nueva_lista1):
    n = len(nueva_lista1)
    fi1 = []
    for i in range(0,n):
        fi1.append(randfloat(0, 2*pi))
    return fi1




#deberia de estar adaptado
def funcion_app(archivo1, epsilon1,epsilon2, simbolo1,simbolo2, valor_permutaciones1,valor_permutaciones2,nombre_resultante, nombre_variables,nombre_resultante2, nombre_variables2,valor_x1,valor_y1,valor_z1,valor_x2,valor_y2,valor_z2):
    if not os.path.exists("process_files"):
            os.makedirs("process_files")
    permutaciones1 = numerosiniciales1(sqrt(valor_permutaciones1),valor_permutaciones1, nombre_variables, valor_x1, valor_y1, valor_z1)
    permutaciones2 = numerosiniciales1(sqrt(valor_permutaciones2),valor_permutaciones2, nombre_variables2, valor_x2, valor_y2, valor_z2)
    fi1 = crear_fi1(permutaciones1)
    fi2 = crear_fi1(permutaciones2)
    if permutaciones1 == []:
        error = "Error in Permutations\nThere is no combination for:\n"+str(valor_permutaciones1)+" = x^2 + y^2 + z^2"
        return ("Permutations",error)
    elif permutaciones2 == []:
        error = "Error in Permutations\nThere is no combination for:\n"+str(valor_permutaciones2)+" = x^2 + y^2 + z^2"
        return ("Permutations",error)
    else:
        try:
            if simbolo1 == "<" and simbolo2 == "<":
                try: 
                    print(simbolo1,"SIMBOLO1")
                    print(simbolo2,"SIMBOLO2")
                    print(permutaciones1)
                    print(permutaciones2)
                    Formula_mayores_permutacion1(permutaciones1,archivo1,epsilon1,fi1)                
                    Formula_mayores_permutacion2(permutaciones2,archivo1,epsilon2,fi1)                
                except:
                    return("File 1","Error in File 1\nIncorrect Format")
                aleacion1("file_permutation1.dump",nombre_resultante,nombre_variables)
                aleacion2("file_permutation2.dump",nombre_resultante2,nombre_variables2)
                return("Complete","The file has been created successfully.\nResults saved in the 'results' folder.")

            elif simbolo1 == "<" and simbolo2 == ">":
                try:
                    Formula_mayores_permutacion1(permutaciones1,archivo1,epsilon1,fi1)
                    Formula_menores_permutacion2(permutaciones2,archivo1,epsilon2,fi1)
                except:
                    return("File 1","Error in File 1\nIncorrect Format")
                aleacion1("file_permutation1.dump",nombre_resultante,nombre_variables)
                aleacion2("file_permutation2.dump",nombre_resultante2,nombre_variables2)
                return("Complete","The file has been created successfully.\nResults saved in the 'results' folder.")

            elif simbolo1 == ">" and simbolo2 == "<":
                try:
                    Formula_menores_permutacion1(permutaciones1,archivo1,epsilon1,fi1)
                    Formula_mayores_permutacion2(permutaciones2,archivo1,epsilon2,fi1)
                except:
                    return("File 1","Error in File 1\nIncorrect Format")
                
                aleacion1("file_permutation1.dump",nombre_resultante,nombre_variables)
                aleacion2("file_permutation2.dump",nombre_resultante2,nombre_variables2)
                return("Complete","The file has been created successfully.\nResults saved in the 'results' folder.")

            elif simbolo1 == ">" and simbolo2 == ">":
                try:
                    Formula_menores_permutacion1(permutaciones1,archivo1,epsilon1,fi1)
                    Formula_menores_permutacion2(permutaciones2,archivo1,epsilon2,fi1)
                except:
                    return("File 1","Error in File 1\nIncorrect Format")
                aleacion1("file_permutation1.dump",nombre_resultante,nombre_variables)
                aleacion2("file_permutation2.dump",nombre_resultante2,nombre_variables2)
                return("Complete","The file has been created successfully.\nResults saved in the 'results' folder.")
        except:
            return("Error in the Program")
    
    

    