        with open("process_files/F_prime_result.dump", "w") as archivo_salida:
            # Escribir los datos iniciales al archivo de salida
            for dato in datos:
                archivo_salida.write(dato)

            # Iterar sobre cada átomo
            for i in range(val_atom):
                coordenadas = valor_x1[i]  # Extraer las coordenadas como lista de floats
                # Calcular F_prima usando una lambda
                valor = lambda x: (x / valor_xminmax) + 1 / 2
                F_prima = valor(coordenadas[0]) * value1[i] + (1 - valor(coordenadas[0])) * value2[i]

                # Evaluar si F_prima cumple la condición para incrementar según el tipo
                if tipo == 1:  # F1 = < y F2 = <
                    if F_prima > epsilon1 and F_prima > epsilon2:
                        archivo_salida.write(f"{incremental} 1 {coordenadas[2]:.3f} {coordenadas[1]:.3f} {coordenadas[0]:.3f}\n")
                        incremental += 1
                elif tipo == 2:  # F1 = > y F2 = <
                    if F_prima < epsilon1 and F_prima > epsilon2:
                        archivo_salida.write(f"{incremental} 1 {coordenadas[2]:.3f} {coordenadas[1]:.3f} {coordenadas[0]:.3f}\n")
                        incremental += 1
                elif tipo == 3:  # F1 = < y F2 = >
                    if F_prima > epsilon1 and F_prima < epsilon2:
                        archivo_salida.write(f"{incremental} 1 {coordenadas[2]:.3f} {coordenadas[1]:.3f} {coordenadas[0]:.3f}\n")
                        incremental += 1
                elif tipo == 4:  # F1 = > y F2 = >
                    if F_prima < epsilon1 and F_prima < epsilon2:
                        archivo_salida.write(f"{incremental} 1 {coordenadas[2]:.3f} {coordenadas[1]:.3f} {coordenadas[0]:.3f}\n")
                        incremental += 1

        # Actualizar el número total de átomos en la línea correspondiente
        with open("process_files/F_prime_result.dump", "r+") as archivo_salida:
            archivo_salida_lines = archivo_salida.readlines()
            archivo_salida_lines[3] = f"{incremental - 1}\n"
            archivo_salida.seek(0)
            archivo_salida.writelines(archivo_salida_lines)

    print("Incremental final:", incremental - 1)
    # Generar archivo GCODE
    with open("results/F_prime_result.gcode", "w") as gcode_salida:
        gcode_salida.write("; GCODE generado a partir de F_prime_result.dump\n")
        gcode_salida.write("G28 ; Home all axes\n")  # Llevar todos los ejes a origen
        gcode_salida.write("G1 Z0.3 F7200 ; Levantar boquilla a 0.3mm\n")

        for i in range(val_atom):
            coordenada_x = valor_x1[i]

            # Calcular F_prima usando la misma lógica
            valor = lambda x: (x / valor_xminmax) + 1 / 2
            F_prima = valor(coordenada_x[0]) * value1[i] + (1 - valor(coordenada_x[0])) * value2[i]

            # Generar movimiento GCODE basado en la condición del tipo
            if tipo == 1 and F_prima > epsilon1 and F_prima > epsilon2:
                gcode_salida.write(f"G1 X{coordenada_x[2]:.3f} Y0.000 Z0.300 F1500 ; Mover a X{coordenada_x[2]:.3f}\n")
            elif tipo == 2 and F_prima < epsilon1 and F_prima > epsilon2:
                gcode_salida.write(f"G1 X{coordenada_x[2]:.3f} Y0.000 Z0.300 F1500 ; Mover a X{coordenada_x[2]:.3f}\n")
            elif tipo == 3 and F_prima > epsilon1 and F_prima < epsilon2:
                gcode_salida.write(f"G1 X{coordenada_x[2]:.3f} Y0.000 Z0.300 F1500 ; Mover a X{coordenada_x[2]:.3f}\n")
            elif tipo == 4 and F_prima < epsilon1 and F_prima < epsilon2:
                gcode_salida.write(f"G1 X{coordenada_x[2]:.3f} Y0.000 Z0.300 F1500 ; Mover a X{coordenada_x[2]:.3f}\n")

        gcode_salida.write("M104 S0 ; Apagar extrusor\n")
        gcode_salida.write("M140 S0 ; Apagar cama caliente\n")
        gcode_salida.write("G28 X0 Y0 ; Home X Y\n")
        gcode_salida.write("M84 ; Desactivar motores\n")

        print(".Gcode Ok!")