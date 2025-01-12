from math import sqrt, cos, pi, sin, radians
from random import uniform as randfloat
from random import seed as semilla
import os
import numpy as np
from scipy.ndimage import gaussian_filter, binary_dilation
from stl import mesh
from skimage import measure
    
    
    
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
            #elif valor < epsilon1:
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
            #elif valor < epsilon1:
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
        resultado = [p for p in permutaciones2 if p[0] <= valor_x2 and abs(p[1]) <= valor_y2 and p[2] <= valor_z2]
    elif operador_menor == ">":
        resultado = [p for p in permutaciones2 if p[0] >= valor_x2 and abs(p[1]) >= valor_y2 and p[2] >= valor_z2]
    else:
        raise ValueError("Operador mayor no válido. Use '<','>'")

    # Si los resultados están vacíos, devuelve [(0, 0, 0)]
    resultado = resultado if resultado else [(0, 0, 0)]
    return resultado



    # Si los resultados están vacíos, devuelve [(0, 0, 0)]


def numerosiniciales(H,H2,nombre_variables,valor_x,valor_y,valor_z,simbolo): ##INICIAL NUMBER H = SQRT(X^2+Y^2+Z^2)
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


    variables = open("results/"+nombre_variables+".log", "a")
    random_seed = "Random Seed: "+str(2)+"\n"
    variables.write(random_seed)
    variables.close()
    n_permutaciones = calcular_con_operadores(permutaciones,valor_x,valor_y,valor_z,simbolo)
    return n_permutaciones

def hybrid_function(archivo1, value1, value2, epsilon1, epsilon2, tipo):
    with open(archivo1, "r") as archivo:
        cont_valores = 0
        values_maxmin = []
        valor_x1 = []
        datos = []
        incremental = 0

        # Leer el archivo y extraer los valores
        for val in archivo:
            cont_valores += 1
            if cont_valores == 4:
                val_atom = int(val.strip())  # Número de átomos
            if cont_valores in [6, 7, 8]:
                values_maxmin.append([float(v) for v in val.rstrip("\n").split()])
            if cont_valores < 10:
                datos.append(val)
            if cont_valores > 9:
                valor_x1.append([float(x) for x in val.rstrip("\n").split()[2:5]])  # Extraer las coordenadas x, y, z

        print("Número de átomos:", val_atom)

        # Recorrer cada átomo (líneas a partir de la línea 10)
        valor_xminmax = values_maxmin[0][1] - values_maxmin[0][0]

        vertices_validos = []
        with open("process_files/F_prime_result.dump", "w") as archivo_salida:
            # Escribir los datos iniciales al archivo de salida
            for dato in datos:
                archivo_salida.write(dato)

            # Iterar sobre cada átomo
            for i in range(val_atom):
                coordenadas = valor_x1[i]  # Extraer las coordenadas como lista de floats
                # Calcular F_prima usando value1 y value2
                #valor = lambda x: (x / valor_xminmax) if valor_xminmax != 0 else 0.5
                valor = lambda x: (x / valor_xminmax) + 1/2
                ponderacion = valor(coordenadas[0])
                F_prima = ponderacion * value1[i] + (1 - ponderacion) * value2[i]

                # Evaluar si F_prima cumple la condición para incrementar según el tipo
                cumple_condicion = False
                if tipo == 1:  # F1 = < y F2 = <
                    if F_prima > epsilon1 and F_prima > epsilon2:
                        cumple_condicion = True
                elif tipo == 2:  # F1 = > y F2 = <
                    if F_prima < epsilon1 and F_prima > epsilon2:
                        cumple_condicion = True
                elif tipo == 3:  # F1 = < y F2 = >
                    if F_prima > epsilon1 and F_prima < epsilon2:
                        cumple_condicion = True
                elif tipo == 4:  # F1 = > y F2 = >
                    if F_prima < epsilon1 and F_prima < epsilon2:
                        cumple_condicion = True

                if cumple_condicion:
                    archivo_salida.write(f"{incremental} 1 {coordenadas[0]:.3f} {coordenadas[1]:.3f} {coordenadas[2]:.3f}\n")
                    incremental += 1
                    vertices_validos.append(coordenadas)

        # Actualizar el número total de átomos en la línea correspondiente
        with open("process_files/F_prime_result.dump", "r+") as archivo_salida:
            archivo_salida_lines = archivo_salida.readlines()
            archivo_salida_lines[3] = f"{incremental}\n"
            archivo_salida.seek(0)
            archivo_salida.writelines(archivo_salida_lines)

    print("Incremental final:", incremental)

    # Generar archivo STL usando numpy-stl solo con los vértices que cumplen la condición
    if len(vertices_validos) < 4:
        print("No hay suficientes vértices válidos para generar un STL.")
        return
    vertices = np.array(vertices_validos)

    # Crear una matriz 3D que represente el volumen a partir de los puntos
    grid_size = 100  # Ajustar según la densidad de puntos deseada
    volume = np.zeros((grid_size, grid_size, grid_size), dtype=np.float32)

    # Normalizar las coordenadas a la grilla
    min_coords = np.min(vertices, axis=0)
    max_coords = np.max(vertices, axis=0)
    norm_vertices = ((vertices - min_coords) / (max_coords - min_coords) * (grid_size - 1)).astype(int)
    norm_vertices = np.clip(norm_vertices, 0, grid_size - 1)  # Asegurar que los puntos estén dentro de los límites

    # Marcar los puntos en el volumen
    for v in norm_vertices:
        volume[v[0], v[1], v[2]] = 1.0

    volume[0, :, :] = 0
    volume[-1, :, :] = 0
    volume[:, 0, :] = 0
    volume[:, -1, :] = 0
    volume[:, :, 0] = 0
    volume[:, :, -1] = 0

    # Aplicar un suavizado al volumen para hacerlo más continuo
    volume = gaussian_filter(volume, sigma=1.0)

    # Usar Marching Cubes para crear una malla a partir del volumen
    verts, faces, _, _ = measure.marching_cubes(volume, level=0.5)

    # Crear el objeto de malla STL usando numpy-stl
    nanopore_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, face in enumerate(faces):
        for j in range(3):
            nanopore_mesh.vectors[i][j] = verts[face[j]]
    # Guardar el archivo STL
    nanopore_mesh.save('results/F_prime_result.stl')
    print(".STL generado correctamente!")





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
    if permutaciones == [] or permutaciones == [(0,0,0)]:
        error = "Error in Permutations\nThere is no combination for:\n"+str(valor_permutacionesE1)+" = x^2 + y^2 + z^2"
        error = "Error in Permutations\nThere is no combination for:\n"+str(valor_permutacionesE2)+" = x^2 + y^2 + z^2"
        return ("Permutations",error)
    elif permutaciones2 == [] or permutaciones2 == [(0,0,0)]:
        error = "Error in Permutations\nThere is no combination for:\n"+str(valor_permutacionesE1)+" = x^2 + y^2 + z^2"
        error = "Error in Permutations\nThere is no combination for:\n"+str(valor_permutacionesE2)+" = x^2 + y^2 + z^2"
        return ("Permutations",error)
    else:
        try:
            if simbolo1 == "<" and simbolo2 == "<":
                try:
                    print("F1 = < ---- F2 = <")
                    type=1
                    mayor1=Formula_mayores(permutaciones,archivo1,epsilon1,fi)
                    mayor2=Formula_mayores2(permutaciones2,archivo1,epsilon2,fi1)
                    hybrid_function(archivo1, mayor1,mayor2, epsilon1, epsilon2,type)
                    #F_prima = lambda_ * mayor1 + (1 - lambda_) * mayor2

                except:
                    return("File 1","Error in File 1\nIncorrect Format")
                aleacion("file1.dump",nombre_resultante,nombre_variables)
                aleacion("file2.dump",nombre_resultante2,nombre_variables2)
                aleacion("F_prime_result.dump",'F_prime_result.dump','F_prime_result')
                
                return("Complete","The file has been created successfully.\nResults saved in the 'results' folder.")
            elif simbolo1 == ">" and simbolo2 == "<":
                try:
                    print("F1 = > ---- F2 = <")
                    type=2
                    menor1 = Formula_menores(permutaciones,archivo1,epsilon1,fi)
                    mayor2= Formula_mayores2(permutaciones2,archivo1,epsilon2,fi1)
                    hybrid_function(archivo1, menor1,mayor2, epsilon1, epsilon2,type)
                except:
                    return("File 1","Error in File 1\nIncorrect Format")
                aleacion("file1.dump",nombre_resultante,nombre_variables)
                aleacion("file2.dump",nombre_resultante2,nombre_variables2)
                aleacion("F_prime_result.dump",'F_prime_result.dump','F_prime_result')
                return("Complete","The file has been created successfully.\nResults saved in the 'results' folder.")
            elif simbolo1 == "<" and simbolo2 == ">":
                try:
                    print("F1 = < ---- F2 = >")
                    type=3
                    mayor1=Formula_mayores(permutaciones,archivo1,epsilon1,fi)
                    menor2=Formula_menores2(permutaciones2,archivo1,epsilon2,fi1)
                    hybrid_function(archivo1, mayor1,menor2, epsilon1, epsilon2,type)

                except:
                    return("File 1","Error in File 1\nIncorrect Format")
                aleacion("file1.dump",nombre_resultante,nombre_variables)
                aleacion("file2.dump",nombre_resultante2,nombre_variables2)
                aleacion("F_prime_result.dump",'F_prime_result.dump','F_prime_result')
                return("Complete","The file has been created successfully.\nResults saved in the 'results' folder.")
            elif simbolo1 == ">" and simbolo2 == ">":
                try:
                    print("F1 = > ---- F2 = >")
                    type=4
                    menor1=Formula_menores(permutaciones,archivo1,epsilon1,fi)
                    menor2=Formula_menores2(permutaciones2,archivo1,epsilon2,fi1)
                    hybrid_function(archivo1, mayor1,menor2, epsilon1, epsilon2,type)
                except:
                    return("File 1","Error in File 1\nIncorrect Format")
                aleacion("file1.dump",nombre_resultante,nombre_variables)
                aleacion("file2.dump",nombre_resultante2,nombre_variables2)
                aleacion("F_prime_result.dump",'F_prime_result.dump','F_prime_result')
                return("Complete","The file has been created successfully.\nResults saved in the 'results' folder.")
        except:
            return("Error in the Program")