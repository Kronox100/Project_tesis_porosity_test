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


def Formula_menores(qi,archivo1,epsilon1,fi):
    archivo = open(archivo1, "r")
    nuevo = open("process_files/file1.dump", "w")
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
                x=0
            elif lineac == 7:
                y = float(r[1].rstrip()) - float(r[0])
            elif lineac == 8:
                z = float(r[1].rstrip()) - float(r[0])
                z=0
                nocubico = nocubicos(x,y,z,90,90,90)
        elif lineac > 9:
            for j in range(n):
                X_1 = qi[j][0]*((2*pi)/nocubico[0])*float(r[2])
                Y_1 = qi[j][1]*((2*pi)/nocubico[1])*float(r[3])
                Z_1 = qi[j][2]*((2*pi)/nocubico[2])*float(r[4])
                valor += cos(( X_1 + ( Y_1 + ( Z_1 + fi[j]))))#fi
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
def Casos_permutaciones(permutaciones, valor_x, valor_y, valor_z):
    n_data = []
    for i in permutaciones:
        x, y, z = i  # Desempaquetamos los valores de la tupla
        print("DATOS:", x, ",", y, ",", z)  # Mostrar la tupla (x, y, z)

        # Evaluar casos para X
        if x < valor_x:
            new_x = valor_x
        elif x > valor_x:
            new_x = x
        else:  # x == valor_x
            new_x = x

        # Evaluar casos para Y
        if y < valor_y:
            new_y = valor_y
        elif y > valor_y:
            new_y = y
        else:  # y == valor_y
            new_y = y

        # Evaluar casos para Z
        if z < valor_z:
            new_z = valor_z
        elif z > valor_z:
            new_z = z
        else:  # z == valor_z
            new_z = z

        # Añadimos el resultado final para esta tupla
        n_data.append((new_x, new_y, new_z))

    return n_data
           

def aleacion(archivo1, nombre_resultante, nombre_variables):
    with open("process_files/" + archivo1, "r") as archivo1:
            with open("results/" + nombre_resultante, "w") as nuevo:
                contador1 = 0
                tipo = 0
                final_primer_archivo = False # Bandera para indicar el final del primer archivo
                for linea in archivo1:
                    contador1 += 1
                    if contador1 == 4:
                        cantidad_archivo1 = int(linea)
                        ultimo_id = int(linea)
                    if contador1 == 6:
                        caja2 = linea.split()
                        break
                    variables = open("results/"+nombre_variables +".log", "a")
                    variables.write("Total Atoms: " + str(cantidad_archivo1)+"\n")
                    variables.write("Core File Percentage: "+str(cantidad_archivo1*100/cantidad_archivo1)+"\n")
                    variables.close()
                    nuevo.write(str(cantidad_archivo1) + "\n")

                    if contador1 <= 9 and contador1 != 4:
                        if contador1 in (6,7,8):
                            caja1 = linea.split()
                            if float(caja1[1]) > float(caja2[1]):
                                caja_mayor = caja1[0] + " " + caja1[1]
                                nuevo.write(caja_mayor+"\n")
                            else:
                                caja_mayor = caja2[0] + " " + caja2[1]
                                nuevo.write(caja_mayor+"\n")
                        else:
                            nuevo.write(linea)
                    if contador1 > 9:
                        if tipo < (int(linea.split()[1])):
                            tipo = (int(linea.split()[1]))
                        nuevo.write(linea)
                    if contador1 == 9:  
                        final_primer_archivo = True

                if final_primer_archivo:
                    if contador1 > 9:
                        ultimo_id += 1
                        valores = linea.split()
                        suma = int(valores[1]) + tipo
                        final = f"{ultimo_id} {suma} {' '.join(valores[2:])}"
                        nuevo.write(final + "\n")



def numerosiniciales(H,H2,nombre_variables,valor_x,valor_y,valor_z):
    x = y = z = 0
    permutaciones=[]
    semilla(2)
    N=0
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
    n_data = Casos_permutaciones(permutaciones,valor_x,valor_y,valor_z)
    
    return n_data

                                                                                                       
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

def funcion_app(archivo1,epsilon1, simbolo, valor_permutaciones,nombre_resultante, nombre_variables,valor_x,valor_y,valor_z):
    if not os.path.exists("process_files"):
            os.makedirs("process_files")
    permutaciones = numerosiniciales(sqrt(valor_permutaciones),valor_permutaciones, nombre_variables,valor_x,valor_y,valor_z)
    fi = crear_fi(permutaciones)
    if permutaciones == []:
        error = "Error in Permutations\nThere is no combination for:\n"+str(valor_permutaciones)+" = x^2 + y^2 + z^2"
        return ("Permutations",error)
    else:
        try:
            if simbolo == ">":
                try:
                    Formula_mayores(permutaciones,archivo1,epsilon1,fi)
                except:
                    return("File 1","Error in File 1\nIncorrect Format")
                aleacion("file1.dump",nombre_resultante,nombre_variables)
                return("Complete","The file has been created successfully.\nResults saved in the 'results' folder.")
            elif simbolo == "<":
                try:
                    Formula_menores(permutaciones,archivo1,epsilon1,fi)
                except:
                    return("File 1","Error in File 1\nIncorrect Format")
                aleacion("file1.dump",nombre_resultante,nombre_variables)
                return("Complete","The file has been created successfully.\nResults saved in the 'results' folder.")
        except:
            return("Error in the Program")