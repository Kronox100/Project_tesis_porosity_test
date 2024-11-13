def funcion_prueba(archivo1, mayor1, mayor2, epsilon1, epsilon2):
    with open(archivo1, "r") as archivo:
        cont_valores = 0
        valor_x1 = []
        f_prima_values = []
        incremental = 1
        
        # Leer el archivo y extraer los valores de X
        for val in archivo:
            cont_valores += 1
            # Almacenar los valores de X a partir de la línea 10
            if cont_valores > 9:
                valores = val.rstrip("\n").split(" ")
                if len(valores) >= 3:  # Asegurarse de que haya al menos 3 columnas (id, type, x, y, z)
                    x_val = float(valores[2])  # Obtener el valor de X
                    valor_x1.append(x_val)
        
        # Definir la función lambda para calcular el valor
        valor = lambda x: (x / 310.00) + 1/2
        
        # Aplicar la función F_prima solo a los valores de X en mayor1 y mayor2
        for i in range(len(mayor1)):
            x_mayor1 = mayor1[i][0]  # Obtener solo la coordenada X de mayor1
            x_mayor2 = mayor2[i][0]  # Obtener solo la coordenada X de mayor2
            
            # Calcular F_prima usando los valores de X de mayor1 y mayor2
            F_prima = valor(x_mayor1) * x_mayor1 + (1 - valor(x_mayor1)) * x_mayor2
            
            # Filtrar y escribir en el archivo de salida si cumple la condición
            if F_prima > epsilon1 and F_prima > epsilon2:
                with open("process_files/F_prime_result.dump", "a") as archivo_salida:
                    archivo_salida.write(f"{incremental} 1 {mayor1[i][0]:.3f} {mayor1[i][1]:.3f} {mayor1[i][2]:.3f}\n")
                incremental += 1
            else:
                # Escribir los otros átomos aunque no cumplan la condición
                with open("process_files/F_prime_result.dump", "a") as archivo_salida:
                    archivo_salida.write(f"{incremental} 1 {mayor2[i][0]:.3f} {mayor2[i][1]:.3f} {mayor2[i][2]:.3f}\n")
                incremental += 1
    
    print("Incremental final:", incremental)
    return f_prima_values