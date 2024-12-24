import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFileDialog, QFrame, QProgressDialog
from PyQt6.QtCore import Qt, QThread, pyqtSignal
import Soyarslan_no_cubico as Soyarslan_no_cubico

class MyThread(QThread):
    resultado_signal = pyqtSignal(tuple)

    def __init__(self, archivo1, epsilon1,epsilon2, simbolo1,simbolo2 , valor_permutacionesE1,valor_permutacionesE2, nombre_resultante,nombre_resultante2,nombre_variables,nombre_variables2,value_x,value_y,value_z,value_x2,value_y2,value_z2):
        super().__init__()
        self.archivo1 = archivo1
        self.epsilon1 = epsilon1
        self.epsilon2 = epsilon2
        self.simbolo1 = simbolo1
        self.simbolo2 = simbolo2
        self.valor_x = value_x
        self.valor_y = value_y
        self.valor_z = value_z
        self.valor_x2 = value_x2
        self.valor_y2 = value_y2
        self.valor_z2 = value_z2
        self.valor_permutacionesE1 = valor_permutacionesE1
        self.valor_permutacionesE2 = valor_permutacionesE2
        self.nombre_resultante = nombre_resultante
        self.nombre_resultante2 = nombre_resultante2
        self.nombre_variables = nombre_variables
        self.nombre_variables2 = nombre_variables2


    def run(self):
        try:
            resultado = Soyarslan_no_cubico.funcion_app(
                self.archivo1, self.epsilon1, self.epsilon2,
                self.simbolo1, self.simbolo2,
                self.valor_permutacionesE1, self.valor_permutacionesE2,
                self.nombre_resultante, self.nombre_resultante2,
                self.nombre_variables, self.nombre_variables2,
                self.valor_x, self.valor_y, self.valor_z,
                self.valor_x2, self.valor_y2, self.valor_z2
            )
            if isinstance(resultado, tuple):  # Si ya es un tuple, úsalo directamente
                self.resultado_signal.emit(resultado)
            elif isinstance(resultado, str):  # Si es un string, envuélvelo como un mensaje de error
                self.resultado_signal.emit(("Error", resultado))
            else:
                self.resultado_signal.emit(("Error", "Unexpected result format"))
        except Exception as e:
            self.resultado_signal.emit(("Error", f"An error occurred: {str(e)}"))

       

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Nanopore Structure')
        self.layout = QVBoxLayout()
        self.setStyleSheet("background-color: #b1bbd7;")

        # Fuentes de la letra
        titulo = "font-family: Arial; font-size: 24pt; font-weight: bold;color: black;"
        sub_titulo = "font-family: Arial; font-size: 18pt;color: black;"
        letra = "font-family: Arial; font-size: 14pt;color: black;"
        letra_confirmar = "font-family: Arial; font-size: 14pt; font-weight: bold;color: black;"

        # Configuración Bordes
        borde_entry = "border: 2px solid #C0C3CC; background-color: #F1F3F9; padding: 5px; border-radius: 7.5px;font-family: Arial; font-size: 14pt;color: black;"
        botones = "QPushButton {color: white; background-color: #2759BE; padding: 5px; border-radius: 7.5px;font-family: Arial; font-size: 14pt;} QPushButton:hover {background-color: #263576; color: white;}"
        botones_confirmar = "QPushButton {color: white; background-color: #263576; padding: 5px; border-radius: 7.5px;font-family: Arial; font-size: 14pt;} QPushButton:hover {background-color: #2759BE; color: white;}"

        # Crear el layout principal
        layout_principal = QVBoxLayout(self)
        
        # Frames
        def crear_frame_contenido(layout):
            frame = QFrame()
            frame.setStyleSheet("background-color: #f1f3f9 ; padding: 10px; border-radius: 10px;")
            layout_frame = QVBoxLayout(frame)
            layout_frame.addLayout(layout)
            return frame

        # Función para agregar un frame al layout principal con el contenido y espaciado
        def agregar_seccion(layout):
            frame = crear_frame_contenido(layout)
            layout_principal.addWidget(frame)
            layout_principal.addSpacing(10)

        # Layout titulo
        layout_titulo = QHBoxLayout()
        label_Titulo = QLabel("Hybrid Nanopore Structure")
        label_Titulo.setStyleSheet(titulo)
        label_Titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_titulo.addWidget(label_Titulo)

        # Layout sub_titulo
        layout_sub_titulo = QHBoxLayout()
        label_sub_titulo = QLabel("Material Type")
        label_sub_titulo.setStyleSheet(sub_titulo)
        label_sub_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_sub_titulo.addWidget(label_sub_titulo)

        # Sección 1: Archivo 1 y Epsilon 1
        layout_seccion1 = QVBoxLayout()
        
        layout1 = QHBoxLayout()
        layout1.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label_archivo1 = QLabel("Input File:")
        label_archivo1.setStyleSheet(letra)
        label_archivo1.setFixedSize(106,36)
        archivo1_entry = QLineEdit()
        archivo1_entry.setStyleSheet(borde_entry)
        boton_explorar1 = QPushButton("Explore")
        boton_explorar1.clicked.connect(lambda: self.seleccionar_archivo(archivo1_entry))
        boton_explorar1.setStyleSheet(botones)
        boton_explorar1.setFixedSize(80,36)
        layout1.addWidget(label_archivo1)
        layout1.addWidget(archivo1_entry)
        layout1.addWidget(boton_explorar1)

        
        layout_seccion1.addLayout(layout1)

        # Sección 2: Archivo 2 y Epsilon 2, agregar X Y Z
        layout_seccion2 = QVBoxLayout()

        layout2 = QHBoxLayout()
        layout2.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label_epsilon1 = QLabel("E1:")
        label_epsilon1.setStyleSheet(letra)
        label_epsilon1.setFixedSize(52,36)
        epsilon1_entry = QLineEdit()
        epsilon1_entry.setStyleSheet(borde_entry)
        epsilon1_entry.setFixedSize(100,36)
        boton_simbolo = QPushButton("<")
        boton_simbolo.clicked.connect(lambda: self.alternar_simbolo(boton_simbolo, boton_simbolo))
        boton_simbolo.setStyleSheet(botones)
        boton_simbolo.setFixedSize(36,36)
        label_valores1 = QLabel("Values")
        label_valores1.setStyleSheet(letra)
        label_valores1.setFixedSize(81,36)
        layout2.addWidget(label_epsilon1)
        layout2.addWidget(epsilon1_entry)
        layout2.addWidget(boton_simbolo)
        layout2.addWidget(label_valores1)

        layout3 = QHBoxLayout()
        layout3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_archivo2 = QLabel("Coords:")
        label_archivo2.setStyleSheet(letra)
        label_archivo2.setFixedSize(106,36)
        archivo2_entry = QLineEdit()
        archivo2_entry.setStyleSheet(borde_entry)
        layout3.addWidget(label_archivo2)

        layout4 = QHBoxLayout()
        layout4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_X = QLabel("X:")
        label_X.setStyleSheet(letra)
        label_X.setFixedSize(52,36)
        label_Y = QLabel("Y:")
        label_Y.setStyleSheet(letra)
        label_Y.setFixedSize(52,36)
        label_Z = QLabel("Z:")
        label_Z.setStyleSheet(letra)
        label_Z.setFixedSize(52,36)
        X_entry = QLineEdit()
        X_entry.setStyleSheet(borde_entry)
        X_entry.setFixedSize(100,36)
        Y_entry = QLineEdit()
        Y_entry.setStyleSheet(borde_entry)
        Y_entry.setFixedSize(100,36)
        Z_entry = QLineEdit()
        Z_entry.setStyleSheet(borde_entry)
        Z_entry.setFixedSize(100,36)
        label_valor_epsilon1 = QLabel("E1")
        epsilon1_entry.textChanged.connect(lambda: self.actualizar_valor_epsilon1(epsilon1_entry, label_valor_epsilon1))
        label_valor_epsilon1.setStyleSheet(letra)
        label_valor_epsilon1.setFixedSize(105,36)
        layout4.addWidget(label_X)
        layout4.addWidget(X_entry)
        layout4.addWidget(label_Y)
        layout4.addWidget(Y_entry)
        layout4.addWidget(label_Z)
        layout4.addWidget(Z_entry)

        layout_seccion2.addLayout(layout2)
        layout_seccion2.addLayout(layout3)
        layout_seccion2.addLayout(layout4)

        #NUEVA FUNCION
        layout_f2 = QVBoxLayout()

        F2_layout = QHBoxLayout()
        F2_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label_E2 = QLabel("E2:")
        label_E2.setStyleSheet(letra)
        label_E2.setFixedSize(52,36)
        E2_entry = QLineEdit()
        E2_entry.setStyleSheet(borde_entry)
        E2_entry.setFixedSize(100,36)
        btn_Simbolo2 = QPushButton("<")
        btn_Simbolo2.clicked.connect(lambda: self.alternar_simbolo(btn_Simbolo2, btn_Simbolo2))
        btn_Simbolo2.setStyleSheet(botones)
        btn_Simbolo2.setFixedSize(36,36)
        label_valores1 = QLabel("Values")
        label_valores1.setStyleSheet(letra)
        label_valores1.setFixedSize(81,36)
        F2_layout.addWidget(label_E2)
        F2_layout.addWidget(E2_entry)
        F2_layout.addWidget(btn_Simbolo2)
        F2_layout.addWidget(label_valores1)

        F2_Coords = QHBoxLayout()
        F2_Coords.setAlignment(Qt.AlignmentFlag.AlignCenter)
        F2_Label_Coords = QLabel("Coords:")
        F2_Label_Coords.setStyleSheet(letra)
        F2_Label_Coords.setFixedSize(106,36)
        F2_Coords.addWidget(F2_Label_Coords)

        F2_CoordsXYZ = QHBoxLayout()
        F2_CoordsXYZ.setAlignment(Qt.AlignmentFlag.AlignCenter)
        X2_Label = QLabel("X:")
        X2_Label.setStyleSheet(letra)
        X2_Label.setFixedSize(52,36)
        Y2_Label = QLabel("Y:")
        Y2_Label.setStyleSheet(letra)
        Y2_Label.setFixedSize(52,36)
        Z2_Label = QLabel("Z:")
        Z2_Label.setStyleSheet(letra)
        Z2_Label.setFixedSize(52,36)
        X2_entry = QLineEdit()
        X2_entry.setStyleSheet(borde_entry)
        X2_entry.setFixedSize(100,36)
        Y2_entry = QLineEdit()
        Y2_entry.setStyleSheet(borde_entry)
        Y2_entry.setFixedSize(100,36)
        Z2_entry = QLineEdit()
        Z2_entry.setStyleSheet(borde_entry)
        Z2_entry.setFixedSize(100,36)
        label_valueE2 = QLabel("E2")
        E2_entry.textChanged.connect(lambda: self.actualizar_valor_epsilon2(E2_entry, label_valueE2))
        label_valueE2.setStyleSheet(letra)
        label_valueE2.setFixedSize(105,36)
        F2_CoordsXYZ.addWidget(X2_Label)
        F2_CoordsXYZ.addWidget(X2_entry)
        F2_CoordsXYZ.addWidget(Y2_Label)
        F2_CoordsXYZ.addWidget(Y2_entry)
        F2_CoordsXYZ.addWidget(Z2_Label)
        F2_CoordsXYZ.addWidget(Z2_entry)

        layout_f2.addLayout(F2_layout)
        layout_f2.addLayout(F2_Coords)
        layout_f2.addLayout(F2_CoordsXYZ)

        # Sección 3: Permutaciones y Nombre Resultado
        layout_seccion3 = QVBoxLayout()

        permut1_layout = QHBoxLayout()
        permut1_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label_permutacion = QLabel("Permutations F1:")
        label_permutacion.setStyleSheet(letra)
        label_permutacion.setFixedSize(178,36)
        entry_permutacion = QLineEdit()
        entry_permutacion.setStyleSheet(borde_entry)
        entry_permutacion.setFixedSize(100,36)

        permut2_layout = QHBoxLayout()
        permut2_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        Label_2permutacion = QLabel("Permutations F2:")
        Label_2permutacion.setStyleSheet(letra)
        Label_2permutacion.setFixedSize(178,36)
        entry_2permutacion = QLineEdit()
        entry_2permutacion.setStyleSheet(borde_entry)
        entry_2permutacion.setFixedSize(100,36)

        permut1_layout.addWidget(label_permutacion)
        permut1_layout.addWidget(entry_permutacion)
        permut2_layout.addWidget(Label_2permutacion)
        permut2_layout.addWidget(entry_2permutacion)

        layout_1stOut = QHBoxLayout()
        layout_1stOut.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label_nombre_archivo = QLabel("Output File 1 Name:")
        label_nombre_archivo.setStyleSheet(letra)
        label_nombre_archivo.setFixedSize(190,36)
        nombre_archivo_entry = QLineEdit("Result 1")
        nombre_archivo_entry.setStyleSheet(borde_entry)
        nombre_archivo_entry.setFixedSize(190,36)

        layout_2ndOut = QHBoxLayout()
        layout_2ndOut.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label2nd_Outarchivo = QLabel("Output File 2 Name:")
        label2nd_Outarchivo.setStyleSheet(letra)
        label2nd_Outarchivo.setFixedSize(190,36)
        nombre_2ndResult = QLineEdit("Result 2")
        nombre_2ndResult.setStyleSheet(borde_entry)
        nombre_2ndResult.setFixedSize(190,36)
        layout_1stOut.addWidget(label_nombre_archivo)
        layout_1stOut.addWidget(nombre_archivo_entry)
        layout_2ndOut.addWidget(label2nd_Outarchivo)
        layout_2ndOut.addWidget(nombre_2ndResult)

        layout7 = QHBoxLayout()
        boton_confirmar = QPushButton("Confirm")
        boton_confirmar.clicked.connect(lambda: self.confirmar(archivo1_entry, epsilon1_entry,E2_entry,boton_simbolo,btn_Simbolo2, entry_permutacion,entry_2permutacion, nombre_archivo_entry,X_entry, Y_entry,Z_entry,X2_entry, Y2_entry,Z2_entry))
        boton_confirmar.setStyleSheet(botones_confirmar)
        boton_confirmar.setFixedSize(98,36)
        layout7.addWidget(boton_confirmar)

        layout_seccion3.addLayout(permut1_layout)
        layout_seccion3.addLayout(permut2_layout)
        layout_seccion3.addLayout(layout_1stOut)
        layout_seccion3.addLayout(layout_2ndOut)
        layout_seccion3.addLayout(layout7)

        layout_principal.addLayout(layout_titulo)
        layout_principal.addLayout(layout_sub_titulo)
        agregar_seccion(layout_seccion1)
        agregar_seccion(layout_seccion2)
        agregar_seccion(layout_f2)
        agregar_seccion(layout_seccion3)

    def seleccionar_archivo(self, entry):
        filename, _ = QFileDialog.getOpenFileName(None, "Seleccionar archivo", "", "Todos los archivos (*);;Archivos de texto (*.txt)")
        if filename:
            entry.setText(filename)
    
    def alternar_simbolo(self, boton_simbolo, label_simbolo1):
        simbolo = boton_simbolo.text()
        nuevo_simbolo = '>' if simbolo == '<' else '<'
        boton_simbolo.setText(nuevo_simbolo)
        label_simbolo1.setText(nuevo_simbolo)
    
    def actualizar_valor_epsilon1(self,epsilon1_entry, label_valor_epsilon1):
        text = epsilon1_entry.text()
        if text:
            label_valor_epsilon1.setText(text)
        else:
            label_valor_epsilon1.setText("E1")

    def actualizar_valor_epsilon2(self,epsilon1_entry, label_valor_epsilon1):
        text = epsilon1_entry.text()
        if text:
            label_valor_epsilon1.setText(text)
        else:
            label_valor_epsilon1.setText("E2")

    def confirmar(self,archivo1_entry, epsilon1_entry,E2_entry,boton_simbolo,btn_Simbolo2, entry_permutacion,entry_2permutacion, nombre_archivo_entry,X_entry, Y_entry,Z_entry,X2_entry, Y2_entry,Z2_entry):
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Confirmation")
        mensaje.setText("The data is correct?")
        mensaje.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        mensaje.button(QMessageBox.StandardButton.Yes)
        mensaje.button(QMessageBox.StandardButton.No)

        reply = mensaje.exec()
        if reply == QMessageBox.StandardButton.Yes:
            print("The operation was confirmed")
            self.confirmar_operacion(archivo1_entry, epsilon1_entry,E2_entry,boton_simbolo,btn_Simbolo2, entry_permutacion,entry_2permutacion, nombre_archivo_entry,X_entry, Y_entry,Z_entry,X2_entry, Y2_entry,Z2_entry)
        else:
            print("The operation was canceled")

    def confirmar_operacion(self,archivo1_var, E1_var,E2_var, boton_simbolo_var,btn_Simbolo2_var, entry_permutacion_var, entry_2permutacion, nombre_archivo_entry,valor_x_var,valor_y_var,valor_z_var,valor_x2_var,valor_y2_var,valor_z2_var):
        if not os.path.exists("results"):
            os.makedirs("results")
        try:
            archivo1 = str(archivo1_var.text())
            if archivo1 == "":
                QMessageBox.information(None, "File 1", "Incorrect File 1 Format")
                return
        except:
            QMessageBox.information(None, "File 1", "Incorrect File 1 Format")
            return
        try:
            epsilon1 = float(E1_var.text())
        except:
            QMessageBox.information(None, "Epsilon 1", "Incorrect Epsilon 1 Format")
            return
        try:
            epsilon2 = float(E2_var.text())        
        except:
            QMessageBox.information(None, "Epsilon 2", "Incorrect Epsilon 2 Format")
            return
        try:
            valor_permutacionesE1 = int(entry_permutacion_var.text())
            valor_permutacionesE2 = int(entry_2permutacion.text())
        except:
            QMessageBox.information(None, "Permutations", "Incorrect Permutations Format")
            return
        try:
            value_x = float(valor_x_var.text())
        except:
            QMessageBox.information(None, "X F1", "Incorrect Coord Format")
            return
        try:
            value_x2 = float(valor_x2_var.text())
        except:
            QMessageBox.information(None, "X F2", "Incorrect Coord Format")
            return
        try:
            value_y = float(valor_y_var.text())
        except:
            QMessageBox.information(None, "Y F1", "Incorrect Coord Format")
            return
        try:
            value_y2 = float(valor_y2_var.text())
        except:
            QMessageBox.information(None, "Y F2", "Incorrect Coord Format")
            return
        try:
            value_z = float(valor_z_var.text())
        except:
            QMessageBox.information(None, "Z F1", "Incorrect Coord Format")
            return
        try:
            value_z2 = float(valor_z2_var.text())
        except:
            QMessageBox.information(None, "Z F2", "Incorrect Coord Format")
            return
        simbolo1 = str(boton_simbolo_var.text())
        simbolo2 = str(btn_Simbolo2_var.text())
        nombre_variables = str(nombre_archivo_entry.text())
        nombre_variables2 = str(nombre_archivo_entry.text())
        nombre_resultante = str(nombre_archivo_entry.text() + "_1.dump")
        nombre_resultante2 = str(nombre_archivo_entry.text() + "_2.dump")

        if simbolo1 == ">" and simbolo2 == ">":
            if epsilon1 != "" and epsilon2 != "" and value_x !="" and value_y != "" and value_z != "" and value_z2 != "" and value_y2 != "" and value_x2 != "":
                variables = open("results/"+nombre_variables+"1.log", "w")
                variables = open("results/"+nombre_variables2+"2.log", "w")
                variables.write(("Epsilon 1: " + str(epsilon1)) + "\n")
                variables.write(("Epsilon 2: " + str(epsilon2)) + "\n")
                variables.write(("Permutations 1: " + str(valor_permutacionesE1)) + "\n")
                variables.write(("Permutations 2: " + str(valor_permutacionesE2)) + "\n")
                variables.write("File 1: E1 " + str(simbolo1) + " Values \n")
                variables.write("File 2: E2 " + str(simbolo2) + " Values \n")
                variables.close()

                # Ventana Informativa
                self.ventana_procesando = QMessageBox(self)
                self.ventana_procesando.setStandardButtons(QMessageBox.StandardButton.NoButton)
                self.ventana_procesando.setText("Processing...\nPlease, Wait")
                self.ventana_procesando.setStyleSheet("background: white; font-family: Arial; font-size: 12pt; font-weight: bold;color: black;")
                self.ventana_procesando.show()

                # Proceso en otro hilo
                self.thread = MyThread(archivo1, epsilon1,epsilon2, simbolo1,simbolo2 , valor_permutacionesE1,valor_permutacionesE2, 
                                        nombre_resultante,nombre_resultante2,nombre_variables,nombre_variables2,value_x,value_y,value_z,value_x2,value_y2,value_z2)
                self.thread.resultado_signal.connect(self.show_result)
                self.thread.start()
            else:
                QMessageBox.information(None, "", "Epsilon 1, X, Y and Z must have data")
        elif simbolo1 == ">" and simbolo2 == "<":
            if epsilon1 != "" and epsilon2 != "" and value_x !="" and value_y != "" and value_z != "" and value_z2 != "" and value_y2 != "" and value_x2 != "":
                variables = open("results/"+nombre_variables+"1.log", "w")
                variables = open("results/"+nombre_variables2+"2.log", "w")
                variables.write(("Epsilon 1: " + str(epsilon1)) + "\n")
                variables.write(("Epsilon 2: " + str(epsilon2)) + "\n")
                variables.write(("Permutations 1: " + str(valor_permutacionesE1)) + "\n")
                variables.write(("Permutations 2: " + str(valor_permutacionesE2)) + "\n")
                variables.write("File 1: E1 " + str(simbolo1) + " Values \n")
                variables.write("File 2: E2 " + str(simbolo2) + " Values \n")
                variables.close()

                # Ventana Informativa
                self.ventana_procesando = QMessageBox(self)
                self.ventana_procesando.setStandardButtons(QMessageBox.StandardButton.NoButton)
                self.ventana_procesando.setText("Processing...\nPlease, Wait")
                self.ventana_procesando.setStyleSheet("background: white; font-family: Arial; font-size: 12pt; font-weight: bold;color: black;")
                self.ventana_procesando.show()

                # Proceso en otro hilo
                self.thread = MyThread(archivo1, epsilon1,epsilon2, simbolo1,simbolo2 , valor_permutacionesE1,valor_permutacionesE2, 
                                        nombre_resultante,nombre_resultante2,nombre_variables,nombre_variables2,value_x,value_y,value_z,value_x2,value_y2,value_z2)
                self.thread.resultado_signal.connect(self.show_result)
                self.thread.start()
            else:
                QMessageBox.information(None, "", "Epsilon 1, X, Y and Z must have data")
        elif simbolo1 == "<" and simbolo2 == ">":
            if epsilon1 != "" and epsilon2 != "" and value_x !="" and value_y != "" and value_z != "" and value_z2 != "" and value_y2 != "" and value_x2 != "":
                variables = open("results/"+nombre_variables+".log", "w")
                variables = open("results/"+nombre_variables2+"2.log", "w")
                variables.write(("Epsilon 1: " + str(epsilon1)) + "\n")
                variables.write(("Epsilon 2: " + str(epsilon2)) + "\n")
                variables.write(("Permutations 1: " + str(valor_permutacionesE1)) + "\n")
                variables.write(("Permutations 2: " + str(valor_permutacionesE2)) + "\n")
                variables.write("File 1: E1 " + str(simbolo1) + " Values \n")
                variables.write("File 2: E2 " + str(simbolo2) + " Values \n")
                variables.close()

                # Ventana Informativa
                self.ventana_procesando = QMessageBox(self)
                self.ventana_procesando.setStandardButtons(QMessageBox.StandardButton.NoButton)
                self.ventana_procesando.setText("Processing...\nPlease, Wait")
                self.ventana_procesando.setStyleSheet("background: white; font-family: Arial; font-size: 12pt; font-weight: bold;color: black;")
                self.ventana_procesando.show()

                # Proceso en otro hilo
                self.thread = MyThread(archivo1, epsilon1,epsilon2, simbolo1,simbolo2 , valor_permutacionesE1,valor_permutacionesE2, 
                                        nombre_resultante,nombre_resultante2,nombre_variables,nombre_variables2,value_x,value_y,value_z,value_x2,value_y2,value_z2)
                self.thread.resultado_signal.connect(self.show_result)
                self.thread.start()
            else:
                QMessageBox.information(None, "", "Epsilon 1, X, Y and Z must have data")
        elif simbolo1 == "<" and simbolo2 == "<":
            if epsilon1 != "" and epsilon2 != "" and value_x !="" and value_y != "" and value_z != "" and value_z2 != "" and value_y2 != "" and value_x2 != "":
                variables = open("results/"+nombre_variables+".log", "w")
                variables = open("results/"+nombre_variables2+"2.log", "w")
                variables.write(("Epsilon 1: " + str(epsilon1)) + "\n")
                variables.write(("Epsilon 2: " + str(epsilon2)) + "\n")
                variables.write(("Permutations 1: " + str(valor_permutacionesE1)) + "\n")
                variables.write(("Permutations 2: " + str(valor_permutacionesE2)) + "\n")
                variables.write("File 1: E1 " + str(simbolo1) + " Values \n")
                variables.write("File 2: E2 " + str(simbolo2) + " Values \n")
                variables.close()

                # Ventana Informativa
                self.ventana_procesando = QMessageBox(self)
                self.ventana_procesando.setStandardButtons(QMessageBox.StandardButton.NoButton)
                self.ventana_procesando.setText("Processing...\nPlease, Wait")
                self.ventana_procesando.setStyleSheet("background: white; font-family: Arial; font-size: 12pt; font-weight: bold;color: black;")
                self.ventana_procesando.show()

                # Proceso en otro hilo
                self.thread = MyThread(archivo1, epsilon1,epsilon2, simbolo1,simbolo2 , valor_permutacionesE1,valor_permutacionesE2, 
                                        nombre_resultante,nombre_resultante2,nombre_variables,nombre_variables2,value_x,value_y,value_z,value_x2,value_y2,value_z2)
                self.thread.resultado_signal.connect(self.show_result)
                self.thread.start()
            else:
                QMessageBox.information(None, "", "Epsilon 1, X, Y and Z must have data")

    def show_result(self, resultado):
        title, message = resultado  # Desempaquetar el tuple

        if isinstance(message, tuple):  # Manejar el caso en que message sea un tuple por error
            message = " ".join(map(str, message))  # Convertir el tuple a una cadena de texto

        self.ventana_procesando.setWindowTitle(title)
        self.ventana_procesando.setText(str(message))  # Convertir message explícitamente a string
        self.ventana_procesando.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.ventana_procesando.adjustSize()

        # Mostrar el cuadro de diálogo
        self.ventana_procesando.exec()

        # Detener el hilo si terminó
        self.thread.quit()
        self.thread.wait()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
