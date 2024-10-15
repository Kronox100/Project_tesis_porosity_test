from math import sqrt, cos, pi, sin, radians
from random import uniform as randfloat
from random import seed as semilla
import os
    
def Formula_mayores(qi,archivo1,epsilon1,fi):
    archivo = open(archivo1, "r")
    nuevo = open("process_files/file1.dump", "w")
    x =y=z = 0
    lineac = 0
    datos =[]
    valor_mayores1=[]
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
                valor += cos((qi[j][0]*((2*pi)/nocubico[0])*float(r[2]) + (qi[j][1]*((2*pi)/nocubico[1])*float(r[3]) + (qi[j][2]*((2*pi)/nocubico[2])*float(r[4]) + fi[j]))))#fi
            norm = sqrt(2/n)
            valor = valor * norm
            if epsilon1 < valor:
                ID += 1
                texto = f"{ID} {r[1]} {r[2]} {r[3]} {r[4]}"
                datos.append(texto)
            elif valor < epsilon1:
                valor_mayores1.append(valor)
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
    #print(len(valor2),'valor2')
    return valor_mayores1

def Formula_mayores2(qi,archivo1,epsilon1,fi):
    archivo = open(archivo1, "r")
    nuevo = open("process_files/file2.dump", "w")
    x =y=z = 0
    lineac = 0
    valor_mayores2 =[]
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
                valor += cos((qi[j][0]*((2*pi)/nocubico[0])*float(r[2]) + (qi[j][1]*((2*pi)/nocubico[1])*float(r[3]) + (qi[j][2]*((2*pi)/nocubico[2])*float(r[4]) + fi[j]))))#fi
            norm = sqrt(2/n)
            valor = valor * norm
            if epsilon1 < valor:
                ID += 1
                texto = f"{ID} {r[1]} {r[2]} {r[3]} {r[4]}"
                datos.append(texto)
            elif valor < epsilon1:
                valor_mayores2.append(valor)
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
    return valor_mayores2



def Formula_menores(qi,archivo1,epsilon1,fi):
    archivo = open(archivo1, "r")
    nuevo = open("process_files/file1.dump", "w")
    x =y=z = 0
    lineac = 0
    datos =[]
    valor_menores1 = []
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
                valor += cos((qi[j][0]*((2*pi)/nocubico[0])*float(r[2]) + (qi[j][1]*((2*pi)/nocubico[1])*float(r[3]) + (qi[j][2]*((2*pi)/nocubico[2])*float(r[4]) + fi[j]))))#fi
            norm = sqrt(2/n)
            valor = valor * norm
            if epsilon1 > valor:
                ID += 1
                texto = f"{ID} {r[1]} {r[2]} {r[3]} {r[4]}"
                datos.append(texto)
            elif  valor < epsilon1:
                valor_menores1.append(valor)
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
    return valor_menores1

def Formula_menores2(qi,archivo1,epsilon1,fi):
    archivo = open(archivo1, "r")
    nuevo = open("process_files/file2.dump", "w")
    x =y=z = 0
    lineac = 0
    datos =[]
    valor_menores2=[]
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
                valor += cos((qi[j][0]*((2*pi)/nocubico[0])*float(r[2]) + (qi[j][1]*((2*pi)/nocubico[1])*float(r[3]) + (qi[j][2]*((2*pi)/nocubico[2])*float(r[4]) + fi[j]))))#fi
            norm = sqrt(2/n)
            valor = valor * norm
            if epsilon1 > valor:
                ID += 1
                texto = f"{ID} {r[1]} {r[2]} {r[3]} {r[4]}"
                datos.append(texto)
            elif valor < epsilon1:
                valor_menores2.append(valor)
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
    return valor_menores2


           

def aleacion(archivo1, nombre_resultante, nombre_variables):
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
                    
                    # Escribir las variables en el archivo de log
                    with open("results/" + nombre_variables + ".log", "a") as variables:
                        variables.write("Total Atoms: " + str(ultimo_id) + "\n")
                        variables.write("Core File Percentage: 100.0%\n")
                        variables.write("Shell File Percentage: 0.0%\n")
                    
                    # Escribir la cantidad total de átomos en el archivo nuevo
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

def calcular_con_operadores(permutaciones2, valor_x2, valor_y2, valor_z2, operador_menor):
    # Filtra las tuplas según el operador menor
    if operador_menor == "<":
        resultado = [p for p in permutaciones2 if p[0] <= valor_x2 and p[1] <= valor_y2 and p[2] <= valor_z2]
    elif operador_menor == ">":
        resultado = [p for p in permutaciones2 if p[0] >= valor_x2 and p[1] >= valor_y2 and p[2] >= valor_z2]
    else:
        raise ValueError("Operador mayor no válido. Use '<','>'")

    # Si los resultados están vacíos, devuelve [(0, 0, 0)]
    resultado = resultado if resultado else [(0, 0, 0)]
    return resultado



    # Si los resultados están vacíos, devuelve [(0, 0, 0)]


def numerosiniciales(H,H2,nombre_variables,valor_x,valor_y,valor_z,simbolo):
    x = y = z = 0
    permutaciones=[]
    semilla(2)
    N=0
    print(valor_x, valor_y, valor_z)  # Para revisar los valores antes de procesar
    for x in range(-H2,H2+1):
        for y in range(-H2,H2+1):
            for z in range(-H2,H2+1):
                h=((x**2)+(y**2)+(z**2))
                if h==H**2:
                    N=N+1
                    permutaciones.append((x,y,z))


    variables = open("results/"+nombre_variables+"1_.log", "a")
    random_seed = "Random Seed: "+str(2)+"\n"
    variables.write(random_seed)
    variables.close()
    n_permutaciones = calcular_con_operadores(permutaciones,valor_x,valor_y,valor_z,simbolo)
    return n_permutaciones


def funcion_prueba(archivo1):             
    archivo = open(archivo1, "r")
    cont_valores=0
    values_maxmin=[]
    valor_x1 = []
    for val in archivo:
        cont_valores+= 1
        if cont_valores == 6:
            values_maxmin.append(val.rstrip("\n").split(" "))
        if cont_valores > 9:
            valor_x1.append((val.rstrip("\n").split(" ")))
    valor_l = float(values_maxmin[0][1]) -  float(values_maxmin[0][0])

    print(valor_l)
    Xmin = float(values_maxmin[0][0])
    Xmax = float(values_maxmin[0][1])
    normalized_list = F_prime(valor_x1,Xmin,Xmax,valor_l,)
    print(len(normalized_list))
    

def F_prime(x, Xmin, Xmax, l):
    normalized_list = []
    
    # Iterar sobre cada sublista de 'x'
    for item in x:
        # Normalizar los valores de las coordenadas (columnas 2, 3 y 4)
        normalized_item = [
            item[0],  # ID (sin normalización)
            item[1],  # Type (sin normalización)
            # Normalizar X
            0 if float(item[2]) <= Xmin else (
                1 if float(item[2]) >= Xmax else (float(item[2]) - Xmin) / (Xmax - Xmin)
            )
        ]
        
        # Calcular lambda
        lambda_value = abs(float(item[2]) - Xmax) if normalized_item[2] == 0 else abs(float(item[2]) - Xmin)
        
        # Aplicar la fórmula correspondiente según el valor de la normalización
        if normalized_item[2] == 0:
            # Aplicar la fórmula cuando F(x) = 0
            s_x = abs(Xmax - float(item[2])) / lambda_value if lambda_value != 0 else 0
            normalized_item.append(s_x / l)  # Dividir por l
        elif normalized_item[2] == 1:
            # Aplicar la fórmula cuando F(x) = 1
            f_x = abs(float(item[2]) - Xmin) / lambda_value if lambda_value != 0 else 0
            normalized_item.append(f_x / l)  # Dividir por l

        # Agregar el ítem normalizado a la nueva lista
        normalized_list.append(normalized_item)
    
    return normalized_list


def nocubicos(a,b,c,alpha,beta,gama):
    matriz = []
    matriz.append(a)
    matriz.append(b*sin(radians(gama)))
    matriz.append(c*(sqrt(1-(cos(radians(alpha))**2-2*(cos(radians(beta))**2)+2*(cos(radians(alpha))*cos(radians(beta))*cos(radians(gama)))))/sin(radians(gama))))
    return matriz

def crear_fi(permutaciones):
    n = len(permutaciones)
    fi = []
    for i in range(0,n):
        fi.append(randfloat(0, 2*pi))
    return fi

 
def funcion_app(archivo1, epsilon1,epsilon2, simbolo1,simbolo2, valor_permutacionesE1, valor_permutacionesE2, nombre_resultante,nombre_resultante2, nombre_variables,nombre_variables2,value_x,value_y,value_z,value_x2,value_y2,value_z2):
    if not os.path.exists("process_files"):
            os.makedirs("process_files")
    permutaciones = numerosiniciales(sqrt(valor_permutacionesE1),valor_permutacionesE1, nombre_variables,value_x,value_y,value_z,simbolo1)
    fi = crear_fi(permutaciones)
    permutaciones2 = numerosiniciales(sqrt(valor_permutacionesE2),valor_permutacionesE2, nombre_variables2,value_x2,value_y2,value_z2,simbolo2)
    fi1 = crear_fi(permutaciones2)
    if permutaciones == []:
        error = "Error in Permutations\nThere is no combination for:\n"+str(valor_permutacionesE1)+" = x^2 + y^2 + z^2"
        error = "Error in Permutations\nThere is no combination for:\n"+str(valor_permutacionesE2)+" = x^2 + y^2 + z^2"
        return ("Permutations",error)
    elif permutaciones2 == []:
        error = "Error in Permutations\nThere is no combination for:\n"+str(valor_permutacionesE1)+" = x^2 + y^2 + z^2"
        error = "Error in Permutations\nThere is no combination for:\n"+str(valor_permutacionesE2)+" = x^2 + y^2 + z^2"
        return ("Permutations",error)
    else:
        try:
            if simbolo1 == "<" and simbolo2 == "<":
                try:
                    print("F1 = < ---- F2 = <")
                    mayor1=Formula_mayores(permutaciones,archivo1,epsilon1,fi)
                    mayor2=Formula_mayores2(permutaciones2,archivo1,epsilon2,fi1)
                    funcion_prueba(archivo1)
                    #print("mayores1: ",mayor1,"mayor2: ",mayor2)
                except:
                    return("File 1","Error in File 1\nIncorrect Format")
                aleacion("file1.dump",nombre_resultante,nombre_variables)
                aleacion("file2.dump",nombre_resultante2,nombre_variables2)
                return("Complete","The file has been created successfully.\nResults saved in the 'results' folder.")
            elif simbolo1 == ">" and simbolo2 == "<":
                try:
                    print("F1 = > ---- F2 = <")
                    print(permutaciones,"datosmenores2")
                    print(permutaciones2,"datos_mayores")
                    Formula_menores(permutaciones,archivo1,epsilon1,fi)
                    Formula_mayores2(permutaciones2,archivo1,epsilon2,fi1)

                except:
                    return("File 1","Error in File 1\nIncorrect Format")
                aleacion("file1.dump",nombre_resultante,nombre_variables)
                aleacion("file2.dump",nombre_resultante2,nombre_variables2)
                return("Complete","The file has been created successfully.\nResults saved in the 'results' folder.")
            elif simbolo1 == "<" and simbolo2 == ">":
                try:
                    print("F1 = < ---- F2 = >")
                    print(permutaciones,"datosmenores2")
                    print(permutaciones2,"datos_mayores")
                    Formula_mayores(permutaciones,archivo1,epsilon1,fi)
                    Formula_menores2(permutaciones2,archivo1,epsilon2,fi1)
                except:
                    return("File 1","Error in File 1\nIncorrect Format")
                aleacion("file1.dump",nombre_resultante,nombre_variables)
                aleacion("file2.dump",nombre_resultante2,nombre_variables2)
                return("Complete","The file has been created successfully.\nResults saved in the 'results' folder.")
            elif simbolo1 == ">" and simbolo2 == ">":
                try:
                    print("F1 = > ---- F2 = >")
                    print(permutaciones,"datosmenores2")
                    print(permutaciones2,"datos_mayores")
                    Formula_menores(permutaciones,archivo1,epsilon1,fi)
                    Formula_menores2(permutaciones2,archivo1,epsilon2,fi1)
                except:
                    return("File 1","Error in File 1\nIncorrect Format")
                aleacion("file1.dump",nombre_resultante,nombre_variables)
                aleacion("file2.dump",nombre_resultante2,nombre_variables2)
                return("Complete","The file has been created successfully.\nResults saved in the 'results' folder.")
        except:
            return("Error in the Program")