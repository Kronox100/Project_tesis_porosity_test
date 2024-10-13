import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFileDialog, QFrame, QProgressDialog
from PyQt6.QtCore import Qt, QThread, pyqtSignal
import Project.xd2 as xd2

from PyQt6.QtCore import QThread, pyqtSignal
import Project.xd2 as xd2

class MyThread(QThread):
    resultado_signal = pyqtSignal(tuple)

    def __init__(self, archivo1,epsilon1,epsilon2, simbolo1, simbolo2, valor_permutaciones1, valor_permutaciones2, nombre_resultante,nombre_variables,nombre_resultante2,nombre_variables2,valor_x1,valor_x2,valor_y1,valor_y2,valor_z1,valor_z2):
        super().__init__()
        self.archivo1 = archivo1
        self.epsilon1 = epsilon1
        self.epsilon2 = epsilon2
        self.simbolo1 = simbolo1
        self.simbolo2 = simbolo2
        self.valor_x1 = valor_x1
        self.valor_x2 = valor_x2
        self.valor_y1 = valor_y1
        self.valor_y2 = valor_y2
        self.valor_z1 = valor_z1
        self.valor_z2 = valor_z2
        self.valor_permutaciones1 = valor_permutaciones1
        self.valor_permutaciones2 = valor_permutaciones2
        self.nombre_resultante = nombre_resultante
        self.nombre_resultante2 = nombre_resultante2
        self.nombre_variables = nombre_variables
        self.nombre_variables2 = nombre_variables2

    def run(self):
        resultado = xd2.funcion_app(self.archivo1, self.epsilon1, self.epsilon2, self.simbolo1, self.simbolo2, self.valor_permutaciones1, self.valor_permutaciones2, self.nombre_resultante, self.nombre_variables,self.nombre_resultante2, self.nombre_variables2, self.valor_x1, self.valor_x2, self.valor_y1, self.valor_y2, self.valor_z1, self.valor_z2)
        self.resultado_signal.emit(resultado)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Nanopore Structure')
        self.layout = QVBoxLayout()
        self.setStyleSheet("background-color: #D8E4FD;")

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
            frame.setStyleSheet("background-color: white; padding: 10px; border-radius: 10px;")
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
        label_Titulo = QLabel("Nanopore Structure")
        label_Titulo.setStyleSheet(titulo)
        label_Titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_titulo.addWidget(label_Titulo)

        # Layout sub_titulo
        layout_sub_titulo = QHBoxLayout()
        label_sub_titulo = QLabel("Core-Shell Type")
        label_sub_titulo.setStyleSheet(sub_titulo)
        label_sub_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_sub_titulo.addWidget(label_sub_titulo)

        # Sección 1: Archivo 1
        layout_seccion1 = QVBoxLayout()

        layout1 = QHBoxLayout()
        layout1.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label_archivo1 = QLabel("Core File:")
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

        # Sección 2: permutaciones 1 y Epsilon 1
        layout_seccion2 = QVBoxLayout()

        layout3 = QHBoxLayout()
        layout3.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label_permutaciones1 = QLabel("Permutations 1:")
        label_permutaciones1.setStyleSheet(letra)
        label_permutaciones1.setFixedSize(160,36)
        permutaciones_entry1 = QLineEdit()
        permutaciones_entry1.setStyleSheet(borde_entry)
        permutaciones_entry1.setFixedSize(100,36)
        label_epsilon1 = QLabel("E1:")
        label_epsilon1.setStyleSheet(letra)
        label_epsilon1.setFixedSize(52,36)
        epsilon1_entry = QLineEdit()
        epsilon1_entry.setStyleSheet(borde_entry)
        epsilon1_entry.setFixedSize(100,36)
        boton_simbolo1 = QPushButton("<")
        boton_simbolo1.clicked.connect(lambda: self.alternar_simbolo(boton_simbolo1))
        boton_simbolo1.setStyleSheet(botones)
        boton_simbolo1.setFixedSize(36,36)
        label_valores1 = QLabel("Values")
        label_valores1.setStyleSheet(letra)
        label_valores1.setFixedSize(81,36)

        layout4 = QHBoxLayout()
        layout4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_X_1 = QLabel("X:")
        label_X_1.setStyleSheet(letra)
        label_X_1.setFixedSize(52,36)
        label_Y_1 = QLabel("Y:")
        label_Y_1.setStyleSheet(letra)
        label_Y_1.setFixedSize(52,36)
        label_Z_1 = QLabel("Z:")
        label_Z_1.setStyleSheet(letra)
        label_Z_1.setFixedSize(52,36)
        X_entry_1 = QLineEdit()
        X_entry_1.setStyleSheet(borde_entry)
        X_entry_1.setFixedSize(100,36)
        Y_entry_1 = QLineEdit()
        Y_entry_1.setStyleSheet(borde_entry)
        Y_entry_1.setFixedSize(100,36)
        Z_entry_1 = QLineEdit()
        Z_entry_1.setStyleSheet(borde_entry)
        Z_entry_1.setFixedSize(100,36)

        layout3.addWidget(label_permutaciones1)
        layout3.addWidget(permutaciones_entry1)
        layout3.addWidget(label_epsilon1)
        layout3.addWidget(epsilon1_entry)
        layout3.addWidget(boton_simbolo1)
        layout3.addWidget(label_valores1)
        layout4.addWidget(label_X_1)
        layout4.addWidget(X_entry_1)
        layout4.addWidget(label_Y_1)
        layout4.addWidget(Y_entry_1)
        layout4.addWidget(label_Z_1)
        layout4.addWidget(Z_entry_1)

        
        layout_seccion2.addLayout(layout3)
        layout_seccion2.addLayout(layout4)        

        # Sección 3: permutaciones 2 y Epsilon 2
        layout_seccion3 = QVBoxLayout()
        layout5 = QHBoxLayout()
        layout5.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label_permutaciones2 = QLabel("Permutations 2:")
        label_permutaciones2.setStyleSheet(letra)
        label_permutaciones2.setFixedSize(160,36)
        permutaciones_entry2 = QLineEdit()
        permutaciones_entry2.setStyleSheet(borde_entry)
        permutaciones_entry2.setFixedSize(100,36)
        label_epsilon2 = QLabel("E2:")
        label_epsilon2.setStyleSheet(letra)
        label_epsilon2.setFixedSize(52,36)
        epsilon2_entry = QLineEdit()
        epsilon2_entry.setStyleSheet(borde_entry)
        epsilon2_entry.setFixedSize(100,36)
        boton_simbolo2 = QPushButton("<")
        boton_simbolo2.clicked.connect(lambda: self.alternar_simbolo(boton_simbolo2))
        boton_simbolo2.setStyleSheet(botones)
        boton_simbolo2.setFixedSize(36,36)
        label_valores1 = QLabel("Values")
        label_valores1.setStyleSheet(letra)
        label_valores1.setFixedSize(81,36)

        layout6 = QHBoxLayout()
        layout6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_X_2 = QLabel("X:")
        label_X_2.setStyleSheet(letra)
        label_X_2.setFixedSize(52,36)
        label_Y_2 = QLabel("Y:")
        label_Y_2.setStyleSheet(letra)
        label_Y_2.setFixedSize(52,36)
        label_Z_2 = QLabel("Z:")
        label_Z_2.setStyleSheet(letra)
        label_Z_2.setFixedSize(52,36)
        X_entry_2 = QLineEdit()
        X_entry_2.setStyleSheet(borde_entry)
        X_entry_2.setFixedSize(100,36)
        Y_entry_2 = QLineEdit()
        Y_entry_2.setStyleSheet(borde_entry)
        Y_entry_2.setFixedSize(100,36)
        Z_entry_2 = QLineEdit()
        Z_entry_2.setStyleSheet(borde_entry)
        Z_entry_2.setFixedSize(100,36)
        layout6.addWidget(label_X_2)
        layout6.addWidget(X_entry_2)
        layout6.addWidget(label_Y_2)
        layout6.addWidget(Y_entry_2)
        layout6.addWidget(label_Z_2)
        layout6.addWidget(Z_entry_2)

        layout5.addWidget(label_permutaciones2)
        layout5.addWidget(permutaciones_entry2)
        layout5.addWidget(label_epsilon2)
        layout5.addWidget(epsilon2_entry)
        layout5.addWidget(boton_simbolo2)
        layout5.addWidget(label_valores1)

        layout_seccion3.addLayout(layout5)
        layout_seccion3.addLayout(layout6)

        # Sección 4: Permutaciones y Nombre Resultado
        layout_seccion4 = QVBoxLayout()


        layout7 = QHBoxLayout()
        layout7.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label_nombre_archivo1 = QLabel("Output File Permutation 1 Name:")
        label_nombre_archivo1.setStyleSheet(letra)
        label_nombre_archivo1.setFixedSize(300,36)
        nombre_archivo1_entry = QLineEdit("Result1")
        nombre_archivo1_entry.setStyleSheet(borde_entry)
        nombre_archivo1_entry.setFixedSize(160,36)
        layout7.addWidget(label_nombre_archivo1)
        layout7.addWidget(nombre_archivo1_entry)

        layout8 = QHBoxLayout()
        layout8.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label_nombre_archivo2 = QLabel("Output File Permutation 2 Name:")
        label_nombre_archivo2.setStyleSheet(letra)
        label_nombre_archivo2.setFixedSize(300,36)
        nombre_archivo2_entry = QLineEdit("Result2")
        nombre_archivo2_entry.setStyleSheet(borde_entry)
        nombre_archivo2_entry.setFixedSize(160,36)
        layout8.addWidget(label_nombre_archivo2)
        layout8.addWidget(nombre_archivo2_entry)

        layout9 = QHBoxLayout()
        boton_confirmar = QPushButton("Confirm")
        boton_confirmar.clicked.connect(lambda: self.confirmar(archivo1_entry, epsilon1_entry,epsilon2_entry, boton_simbolo1,boton_simbolo2, permutaciones_entry1, permutaciones_entry2, nombre_archivo1_entry, nombre_archivo2_entry, X_entry_1, Y_entry_1, Z_entry_1, X_entry_2, Y_entry_2, Z_entry_2))
        boton_confirmar.setStyleSheet(botones_confirmar)
        boton_confirmar.setFixedSize(98,36)
        layout9.addWidget(boton_confirmar)

        layout_seccion4.addLayout(layout7)
        layout_seccion4.addLayout(layout8)
        layout_seccion4.addLayout(layout9)

        layout_principal.addLayout(layout_titulo)
        layout_principal.addLayout(layout_sub_titulo)
        agregar_seccion(layout_seccion1)
        agregar_seccion(layout_seccion2)
        agregar_seccion(layout_seccion3)
        agregar_seccion(layout_seccion4)

    def seleccionar_archivo(self, entry):
        filename, _ = QFileDialog.getOpenFileName(None, "Seleccionar archivo", "", "Todos los archivos (*);;Archivos de texto (*.txt)")
        if filename:
            entry.setText(filename)
    
    def alternar_simbolo(self, boton_simbolo):
        simbolo = boton_simbolo.text()
        nuevo_simbolo = '>' if simbolo == '<' else '<'
        boton_simbolo.setText(nuevo_simbolo)

    
    def actualizar_valor_epsilon1(self,epsilon1_entry, label_valor_epsilon1, epsilon2_entry, label_valor_epsilon2):
        text = epsilon1_entry.text()
        text1 = epsilon2_entry.text()
        if text:
            label_valor_epsilon1.setText(text)
            label_valor_epsilon2.setText(text1)
        else:
            label_valor_epsilon1.setText("E1")
            label_valor_epsilon2.setText("E2")

    def confirmar(self,archivo1_entry, epsilon1_entry,epsilon2_entry, boton_simbolo1,boton_simbolo2, permutaciones_entry1 , permutaciones_entry2, nombre_archivo1_entry, nombre_archivo2_entry,valor_x1_entry, valor_y1_entry,valor_z1_entry,valor_x2_entry, valor_y2_entry,valor_z2_entry):
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Confirmation")
        mensaje.setText("The data is correct?")
        mensaje.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        mensaje.button(QMessageBox.StandardButton.Yes)
        mensaje.button(QMessageBox.StandardButton.No)

        reply = mensaje.exec()
        if reply == QMessageBox.StandardButton.Yes:
            print("The operation was confirmed")
            self.confirmar_operacion(archivo1_entry, epsilon1_entry,epsilon2_entry, boton_simbolo1,boton_simbolo2, permutaciones_entry1, permutaciones_entry2 , nombre_archivo1_entry, nombre_archivo2_entry,valor_x1_entry, valor_y1_entry,valor_z1_entry,valor_x2_entry, valor_y2_entry,valor_z2_entry )
        else:
            print("The operation was canceled")

    def confirmar_operacion(self, archivo1_var, epsilon1_var,epsilon2_var, simbolo1_var,simbolo2_var, permutaciones_var1, permutaciones_var2, nombre_archivo1, nombre_archivo2,valor_x1_var, valor_y1_var,valor_z1_var,valor_x2_var, valor_y2_var,valor_z2_var):

        if not os.path.exists("results"):
            os.makedirs("results")
        try:
            archivo1 = str(archivo1_var.text())
            archivo2 = str(archivo1_var.text())
            if archivo1 == "":
                QMessageBox.information(None, "File 1", "Incorrect File 1 Format")
                return
        except:
            QMessageBox.information(None, "File 1", "Incorrect File 1 Format")
            return
        try:
            epsilon1 = float(epsilon1_var.text())
        except:
            QMessageBox.information(None, "Epsilon 1", "Incorrect Epsilon 1 Format")
            return
        try:
            epsilon2 = float(epsilon2_var.text())
        except:
            QMessageBox.information(None, "Epsilon 2", "Incorrect Epsilon 2 Format")
            return
        try:
            valor_permutaciones1 = int(permutaciones_var1.text())
        except:
            QMessageBox.information(None, "Permutations 1", "Incorrect Permutations Format")
            return
        try:
            valor_permutaciones2 = int(permutaciones_var2.text())
        except:
            QMessageBox.information(None, "Permutations 2", "Incorrect Permutations Format")
            return
        try:
            value_x1 = float(valor_x1_var.text())
        except:
            QMessageBox.information(None, "X 1", "Incorrect Coord Format")
            return
        try:
            value_x2 = float(valor_x2_var.text())
        except:
            QMessageBox.information(None, "X 2", "Incorrect Coord Format")
            return
        try:
            value_y1 = float(valor_y1_var.text())
        except:
            QMessageBox.information(None, "Y 1", "Incorrect Coord Format")
            return
        try:
            value_y2 = float(valor_y2_var.text())
        except:
            QMessageBox.information(None, "Y 2", "Incorrect Coord Format")
            return
        try:
            value_z1 = float(valor_z1_var.text())
        except:
            QMessageBox.information(None, "Z 1", "Incorrect Coord Format")
            return
        try:
            value_z2 = float(valor_z2_var.text())
        except:
            QMessageBox.information(None, "Z 2", "Incorrect Coord Format")
            return
        
        simbolo1 = str(simbolo1_var.text())
        simbolo2 = str(simbolo2_var.text())
        nombre_variables = str(nombre_archivo1.text()+"_pemutacion_1")
        nombre_resultante = str(nombre_archivo1.text() + "_pemutacion_1.dump")
        nombre_variables2 = str(nombre_archivo2.text()+"_pemutacion_2")
        nombre_resultante2 = str(nombre_archivo2.text() + "_pemutacion_2.dump")
        

        if simbolo1 == ">" and simbolo2 == ">":
            if epsilon1 != "" and epsilon2 != "" and value_x1 !="" and value_x2 !="" and value_y1 != "" and value_y2 !=""and value_z2 != "" and value_z2 !="":    
                
                variables = open("results/"+nombre_variables+".log", "w")
                variables.write(("Epsilon 1: " + str(epsilon1)) + "\n")
                variables.write(("Permutations 1: " + str(valor_permutaciones1)) + "\n")
                variables.close()

                variables2 = open("results/"+nombre_variables2+".log", "w")
                variables2.write(("Epsilon 2: " + str(epsilon2)) + "\n")
                variables2.write(("Permutations 2: " + str(valor_permutaciones2)) + "\n")
                variables2.close()

                variables3 = open("results/variables.txt", "w")
                variables3.write(("Epsilon 1: " + str(epsilon1)) + "\n")
                variables3.write(("Epsilon 2: " + str(epsilon2)) + "\n")
                variables3.write(("Permutations 1: " + str(valor_permutaciones1)) + "\n")
                variables3.write(("Permutations 2: " + str(valor_permutaciones2)) + "\n")
                variables3.write("File 1: E1 " + str(simbolo1) + "\n")
                variables3.write("File 2: E2 " + str(simbolo2) + "\n")

                variables3.close()

                # Ventana Informativa
                self.ventana_procesando = QMessageBox(self)
                self.ventana_procesando.setStandardButtons(QMessageBox.StandardButton.NoButton)
                self.ventana_procesando.setText("Processing...\nPlease, Wait")
                self.ventana_procesando.setStyleSheet("background: white; font-family: Arial; font-size: 12pt; font-weight: bold;color: black;")
                self.ventana_procesando.show()

                # Proceso en otro hilo
                self.thread = MyThread(archivo1, epsilon1, epsilon2, simbolo1,simbolo2, valor_permutaciones1, valor_permutaciones2, nombre_resultante,nombre_variables, nombre_resultante2,nombre_variables2,value_x1,value_x2,value_y1,value_y2,value_z1,value_z2)
                self.thread.resultado_signal.connect(self.show_result)
                self.thread.start()
            else:
                QMessageBox.information(None, "", "Epsilon 1, X1, X2, Y1, Y2, Z1 and Z2 must have data")
        elif simbolo1 == ">" and simbolo2 == "<":
            if epsilon1 != "" and epsilon2 != "" and value_x1 !="" and value_x2 !="" and value_y1 != "" and value_y2 !=""and value_z2 != "" and value_z2 !="":  
                variables = open("results/"+nombre_variables+".log", "w")
                variables.write(("Epsilon 1: " + str(epsilon1)) + "\n")
                variables.write(("Permutations 1: " + str(valor_permutaciones1)) + "\n")
                variables.close()

                variables2 = open("results/"+nombre_variables2+".log", "w")
                variables2.write(("Epsilon 2: " + str(epsilon2)) + "\n")
                variables2.write(("Permutations 2: " + str(valor_permutaciones2)) + "\n")
                variables2.close()

                variables3 = open("results/variables.txt", "w")
                variables3.write(("Epsilon 1: " + str(epsilon1)) + "\n")
                variables3.write(("Epsilon 2: " + str(epsilon2)) + "\n")
                variables3.write(("Permutations 1: " + str(valor_permutaciones1)) + "\n")
                variables3.write(("Permutations 2: " + str(valor_permutaciones2)) + "\n")
                variables3.write("File 1: E1 " + str(simbolo1) + "\n")
                variables3.write("File 2: E2 " + str(simbolo2) + "\n")

                variables3.close()

                # Ventana Informativa
                self.ventana_procesando = QMessageBox(self)
                self.ventana_procesando.setStandardButtons(QMessageBox.StandardButton.NoButton)
                self.ventana_procesando.setText("Processing...\nPlease, Wait")
                self.ventana_procesando.setStyleSheet("background: white; font-family: Arial; font-size: 12pt; font-weight: bold;color: black;")
                self.ventana_procesando.show()

                # Proceso en otro hilo
                self.thread = MyThread(archivo1, epsilon1, epsilon2, simbolo1,simbolo2, valor_permutaciones1, valor_permutaciones2, nombre_resultante,nombre_variables, nombre_resultante2,nombre_variables2,value_x1,value_x2,value_y1,value_y2,value_z1,value_z2)
                self.thread.resultado_signal.connect(self.show_result)
                self.thread.start()
            else:
                QMessageBox.information(None, "", "Epsilon 1, X1, X2, Y1, Y2, Z1 and Z2 must have data")    
        elif simbolo1 == "<" and simbolo2 == "<":
            if epsilon1 != "" and epsilon2 != "" and value_x1 !="" and value_x2 !="" and value_y1 != "" and value_y2 !=""and value_z2 != "" and value_z2 !="":  
                variables = open("results/"+nombre_variables+".log", "w")
                variables.write(("Epsilon 1: " + str(epsilon1)) + "\n")
                variables.write(("Permutations 1: " + str(valor_permutaciones1)) + "\n")
                variables.close()

                variables2 = open("results/"+nombre_variables2+".log", "w")
                variables2.write(("Epsilon 2: " + str(epsilon2)) + "\n")
                variables2.write(("Permutations 2: " + str(valor_permutaciones2)) + "\n")
                variables2.close()

                variables3 = open("results/variables.txt", "w")
                variables3.write(("Epsilon 1: " + str(epsilon1)) + "\n")
                variables3.write(("Epsilon 2: " + str(epsilon2)) + "\n")
                variables3.write(("Permutations 1: " + str(valor_permutaciones1)) + "\n")
                variables3.write(("Permutations 2: " + str(valor_permutaciones2)) + "\n")
                variables3.write("File 1: E1 " + str(simbolo1) + "\n")
                variables3.write("File 2: E2 " + str(simbolo2) + "\n")

                variables3.close()

                # Ventana Informativa
                self.ventana_procesando = QMessageBox(self)
                self.ventana_procesando.setStandardButtons(QMessageBox.StandardButton.NoButton)
                self.ventana_procesando.setText("Processing...\nPlease, Wait")
                self.ventana_procesando.setStyleSheet("background: white; font-family: Arial; font-size: 12pt; font-weight: bold;color: black;")
                self.ventana_procesando.show()

                # Proceso en otro hilo
                self.thread = MyThread(archivo1, epsilon1, epsilon2, simbolo1,simbolo2, valor_permutaciones1, valor_permutaciones2, nombre_resultante,nombre_variables, nombre_resultante2,nombre_variables2,value_x1,value_x2,value_y1,value_y2,value_z1,value_z2)
                self.thread.resultado_signal.connect(self.show_result)
                self.thread.start()
            else:
                QMessageBox.information(None, "", "Epsilon 1, X1, X2, Y1, Y2, Z1 and Z2 must have data")    
        elif simbolo1 == "<" and simbolo2 == ">":
            if epsilon1 != "" and epsilon2 != "" and value_x1 !="" and value_x2 !="" and value_y1 != "" and value_y2 !=""and value_z2 != "" and value_z2 !="":  
                variables = open("results/"+nombre_variables+".log", "w")
                variables.write(("Epsilon 1: " + str(epsilon1)) + "\n")
                variables.write(("Permutations 1: " + str(valor_permutaciones1)) + "\n")
                variables.close()

                variables2 = open("results/"+nombre_variables2+".log", "w")
                variables2.write(("Epsilon 2: " + str(epsilon2)) + "\n")
                variables2.write(("Permutations 2: " + str(valor_permutaciones2)) + "\n")
                variables2.close()

                variables3 = open("results/variables.txt", "w")
                variables3.write(("Epsilon 1: " + str(epsilon1)) + "\n")
                variables3.write(("Epsilon 2: " + str(epsilon2)) + "\n")
                variables3.write(("Permutations 1: " + str(valor_permutaciones1)) + "\n")
                variables3.write(("Permutations 2: " + str(valor_permutaciones2)) + "\n")
                variables3.write("File 1: E1 " + str(simbolo1) + "\n")
                variables3.write("File 2: E2 " + str(simbolo2) + "\n")

                variables3.close()

                # Ventana Informativa
                self.ventana_procesando = QMessageBox(self)
                self.ventana_procesando.setStandardButtons(QMessageBox.StandardButton.NoButton)
                self.ventana_procesando.setText("Processing...\nPlease, Wait")
                self.ventana_procesando.setStyleSheet("background: white; font-family: Arial; font-size: 12pt; font-weight: bold;color: black;")
                self.ventana_procesando.show()

                # Proceso en otro hilo
                self.thread = MyThread(archivo1, epsilon1, epsilon2, simbolo1,simbolo2, valor_permutaciones1, valor_permutaciones2, nombre_resultante,nombre_variables, nombre_resultante2,nombre_variables2,value_x1,value_x2,value_y1,value_y2,value_z1,value_z2)
                self.thread.resultado_signal.connect(self.show_result)
                self.thread.start()        
            else:
                QMessageBox.information(None, "", "Epsilon 1, X1, X2, Y1, Y2, Z1 and Z2 must have data")

    def show_result(self, resultado):
        self.ventana_procesando.setWindowTitle(resultado[0])
        self.ventana_procesando.setText(resultado[1])
        self.ventana_procesando.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.ventana_procesando.adjustSize()
        
        
        # Cerrar el hilo
        self.thread.quit()
        self.thread.wait()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())