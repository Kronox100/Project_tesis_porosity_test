import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QFileDialog, QFrame, QProgressDialog
from PyQt6.QtCore import Qt, QThread, pyqtSignal
import Soyarslan_no_cubico as Soyarslan_no_cubico

class MyThread(QThread):
    resultado_signal = pyqtSignal(tuple)

    def __init__(self, archivo1, epsilon1,epsilon2, simbolo1,simbolo2 , valor_permutacionesE1,valor_permutacionesE2,
                 nombre_resultante,nombre_resultante2,nombre_variables,nombre_variables2,value_x,value_y,
                 value_z,value_x2,value_y2,value_z2,ax, nx, ay, ny, az, nz, ax2, nx2, ay2, ny2, az2, nz2,
                 nx_lambda, ny_lambda, nz_lambda):
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
        #L Nuevos argumentos senoidales
        self.ax = ax
        self.nx = nx
        self.ay = ay
        self.ny = ny
        self.az = az
        self.nz = nz
        self.ax2 = ax2
        self.nx2 = nx2
        self.ay2 = ay2
        self.ny2 = ny2
        self.az2 = az2
        self.nz2 = nz2
        #L Nuevos argumentos lambda
        self.nx_lambda = nx_lambda
        self.ny_lambda = ny_lambda
        self.nz_lambda = nz_lambda


    def run(self):
        try:
            resultado = Soyarslan_no_cubico.funcion_app(
                self.archivo1, self.epsilon1, self.epsilon2,
                self.simbolo1, self.simbolo2,
                self.valor_permutacionesE1, self.valor_permutacionesE2,
                self.nombre_resultante, self.nombre_resultante2,
                self.nombre_variables, self.nombre_variables2,
                self.valor_x, self.valor_y, self.valor_z,
                self.valor_x2, self.valor_y2, self.valor_z2,
                self.ax, self.nx, self.ay, self.ny, self.az, self.nz,
                self.ax2, self.nx2, self.ay2, self.ny2, self.az2, self.nz2,
                self.nx_lambda, self.ny_lambda, self.nz_lambda
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
        # Campos senoidales para E1
        layout_senoidal1 = QHBoxLayout()
        label_ax = QLabel("Ax:")
        label_ax.setStyleSheet(letra)
        entry_ax = QLineEdit()
        entry_ax.setStyleSheet(borde_entry)
        entry_ax.setFixedSize(80, 36)

        label_nx = QLabel("nx:")
        label_nx.setStyleSheet(letra)
        entry_nx = QLineEdit()
        entry_nx.setStyleSheet(borde_entry)
        entry_nx.setFixedSize(80, 36)

        label_ay = QLabel("Ay:")
        label_ay.setStyleSheet(letra)
        entry_ay = QLineEdit()
        entry_ay.setStyleSheet(borde_entry)
        entry_ay.setFixedSize(80, 36)

        label_ny = QLabel("ny:")
        label_ny.setStyleSheet(letra)
        entry_ny = QLineEdit()
        entry_ny.setStyleSheet(borde_entry)
        entry_ny.setFixedSize(80, 36)

        label_az = QLabel("Az:")
        label_az.setStyleSheet(letra)
        entry_az = QLineEdit()
        entry_az.setStyleSheet(borde_entry)
        entry_az.setFixedSize(80, 36)

        label_nz = QLabel("nz:")
        label_nz.setStyleSheet(letra)
        entry_nz = QLineEdit()
        entry_nz.setStyleSheet(borde_entry)
        entry_nz.setFixedSize(80, 36)

        layout_senoidal1.addWidget(label_ax)
        layout_senoidal1.addWidget(entry_ax)
        layout_senoidal1.addWidget(label_nx)
        layout_senoidal1.addWidget(entry_nx)
        layout_senoidal1.addWidget(label_ay)
        layout_senoidal1.addWidget(entry_ay)
        layout_senoidal1.addWidget(label_ny)
        layout_senoidal1.addWidget(entry_ny)
        layout_senoidal1.addWidget(label_az)
        layout_senoidal1.addWidget(entry_az)
        layout_senoidal1.addWidget(label_nz)
        layout_senoidal1.addWidget(entry_nz)

        layout_seccion2.addLayout(layout_senoidal1)
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

        # Campos senoidales para E2
        layout_senoidal2 = QHBoxLayout()
        label_ax2 = QLabel("Ax:")
        label_ax2.setStyleSheet(letra)
        entry_ax2 = QLineEdit()
        entry_ax2.setStyleSheet(borde_entry)
        entry_ax2.setFixedSize(80, 36)

        label_nx2 = QLabel("nx:")
        label_nx2.setStyleSheet(letra)
        entry_nx2 = QLineEdit()
        entry_nx2.setStyleSheet(borde_entry)
        entry_nx2.setFixedSize(80, 36)

        label_ay2 = QLabel("Ay:")
        label_ay2.setStyleSheet(letra)
        entry_ay2 = QLineEdit()
        entry_ay2.setStyleSheet(borde_entry)
        entry_ay2.setFixedSize(80, 36)

        label_ny2 = QLabel("ny:")
        label_ny2.setStyleSheet(letra)
        entry_ny2 = QLineEdit()
        entry_ny2.setStyleSheet(borde_entry)
        entry_ny2.setFixedSize(80, 36)

        label_az2 = QLabel("Az:")
        label_az2.setStyleSheet(letra)
        entry_az2 = QLineEdit()
        entry_az2.setStyleSheet(borde_entry)
        entry_az2.setFixedSize(80, 36)

        label_nz2 = QLabel("nz:")
        label_nz2.setStyleSheet(letra)
        entry_nz2 = QLineEdit()
        entry_nz2.setStyleSheet(borde_entry)
        entry_nz2.setFixedSize(80, 36)

        layout_senoidal2.addWidget(label_ax2)
        layout_senoidal2.addWidget(entry_ax2)
        layout_senoidal2.addWidget(label_nx2)
        layout_senoidal2.addWidget(entry_nx2)
        layout_senoidal2.addWidget(label_ay2)
        layout_senoidal2.addWidget(entry_ay2)
        layout_senoidal2.addWidget(label_ny2)
        layout_senoidal2.addWidget(entry_ny2)
        layout_senoidal2.addWidget(label_az2)
        layout_senoidal2.addWidget(entry_az2)
        layout_senoidal2.addWidget(label_nz2)
        layout_senoidal2.addWidget(entry_nz2)

        layout_f2.addLayout(layout_senoidal2)


        layout_f2.addLayout(F2_Coords)
        layout_f2.addLayout(F2_CoordsXYZ)

        #L Parámetros de la función lambda
        layout_lambda = QHBoxLayout()
        layout_lambda.setAlignment(Qt.AlignmentFlag.AlignLeft)

        label_lambda_title = QLabel("Lambda Parameters:")
        label_lambda_title.setStyleSheet(letra)
        label_lambda_title.setFixedWidth(220)
        layout_lambda.addWidget(label_lambda_title)

        # nx
        label_nx_lambda = QLabel("nx:")
        label_nx_lambda.setStyleSheet(letra)
        entry_nx_lambda = QLineEdit()
        entry_nx_lambda.setStyleSheet(borde_entry)
        entry_nx_lambda.setFixedSize(70, 36)

        # ny
        label_ny_lambda = QLabel("ny:")
        label_ny_lambda.setStyleSheet(letra)
        entry_ny_lambda = QLineEdit()
        entry_ny_lambda.setStyleSheet(borde_entry)
        entry_ny_lambda.setFixedSize(70, 36)

        # nz
        label_nz_lambda = QLabel("nz:")
        label_nz_lambda.setStyleSheet(letra)
        entry_nz_lambda = QLineEdit()
        entry_nz_lambda.setStyleSheet(borde_entry)
        entry_nz_lambda.setFixedSize(70, 36)

        # Añadir widgets al layout
        layout_lambda.addWidget(label_nx_lambda)
        layout_lambda.addWidget(entry_nx_lambda)
        layout_lambda.addWidget(label_ny_lambda)
        layout_lambda.addWidget(entry_ny_lambda)
        layout_lambda.addWidget(label_nz_lambda)
        layout_lambda.addWidget(entry_nz_lambda)


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
        boton_confirmar.clicked.connect(lambda: self.confirmar(archivo1_entry, epsilon1_entry, E2_entry, boton_simbolo, btn_Simbolo2,
                                                               entry_permutacion, entry_2permutacion, nombre_archivo_entry,X_entry, Y_entry, Z_entry, 
                                                               X2_entry, Y2_entry, Z2_entry,entry_ax, entry_nx, entry_ay, entry_ny, entry_az, entry_nz,
                                                               entry_ax2, entry_nx2, entry_ay2, entry_ny2, entry_az2, entry_nz2,
                                                               entry_nx_lambda, entry_ny_lambda, entry_nz_lambda))
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
        #L Agregar la sección lambda al layout principal
        agregar_seccion(layout_lambda)
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

    def confirmar(self, archivo1_entry, epsilon1_entry, E2_entry, boton_simbolo, btn_Simbolo2,
              entry_permutacion, entry_2permutacion, nombre_archivo_entry,
              X_entry, Y_entry, Z_entry, X2_entry, Y2_entry, Z2_entry,
              entry_ax, entry_nx, entry_ay, entry_ny, entry_az, entry_nz,
              entry_ax2, entry_nx2, entry_ay2, entry_ny2, entry_az2, entry_nz2,
              entry_nx_lambda, entry_ny_lambda, entry_nz_lambda):
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Confirmation")
        mensaje.setText("The data is correct?")
        mensaje.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        mensaje.button(QMessageBox.StandardButton.Yes)
        mensaje.button(QMessageBox.StandardButton.No)

        reply = mensaje.exec()
        if reply == QMessageBox.StandardButton.Yes:
            print("The operation was confirmed")
            self.confirmar_operacion(archivo1_entry, epsilon1_entry, E2_entry, boton_simbolo, btn_Simbolo2,
                                     entry_permutacion, entry_2permutacion, nombre_archivo_entry,X_entry, 
                                     Y_entry, Z_entry, X2_entry, Y2_entry, Z2_entry,entry_ax, entry_nx, 
                                     entry_ay, entry_ny, entry_az, entry_nz,entry_ax2, entry_nx2, entry_ay2,
                                     entry_ny2, entry_az2, entry_nz2, entry_nx_lambda, entry_ny_lambda, entry_nz_lambda)
        else:
            print("The operation was canceled")

    def confirmar_operacion(self,archivo1_var, E1_var,E2_var, boton_simbolo_var,btn_Simbolo2_var, 
                            entry_permutacion_var, entry_2permutacion, nombre_archivo_entry,valor_x_var,
                            valor_y_var,valor_z_var,valor_x2_var,valor_y2_var,valor_z2_var,
                            entry_ax=None, entry_nx=None, entry_ay=None, entry_ny=None, entry_az=None, entry_nz=None,
                            entry_ax2=None, entry_nx2=None, entry_ay2=None, entry_ny2=None, entry_az2=None, 
                            entry_nz2=None, entry_nx_lambda=None, entry_ny_lambda=None, entry_nz_lambda=None):
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
        
        #L Validación de campos senoidales para E1
        try:
            ax = float(entry_ax.text()) if entry_ax and entry_ax.text() else 0
        except:
            QMessageBox.information(None, "Ax", "Incorrect Ax Format")
            return
        try:
            nx = int(entry_nx.text()) if entry_nx and entry_nx.text() else 0
        except:
            QMessageBox.information(None, "nx", "Incorrect nx Format")
            return
        try:
            ay = float(entry_ay.text()) if entry_ay and entry_ay.text() else 0
        except:
            QMessageBox.information(None, "Ay", "Incorrect Ay Format")
            return
        try:
            ny = int(entry_ny.text()) if entry_ny and entry_ny.text() else 0
        except:
            QMessageBox.information(None, "ny", "Incorrect ny Format")
            return
        try:
            az = float(entry_az.text()) if entry_az and entry_az.text() else 0
        except:
            QMessageBox.information(None, "Az", "Incorrect Az Format")
            return
        try:
            nz = int(entry_nz.text()) if entry_nz and entry_nz.text() else 0
        except:
            QMessageBox.information(None, "nz", "Incorrect nz Format")
            return

        #L Validación de campos senoidales para E2
        try:
            ax2 = float(entry_ax2.text()) if entry_ax2 and entry_ax2.text() else 0
        except:
            QMessageBox.information(None, "Ax2", "Incorrect Ax2 Format")
            return
        try:
            nx2 = int(entry_nx2.text()) if entry_nx2 and entry_nx2.text() else 0
        except:
            QMessageBox.information(None, "nx2", "Incorrect nx2 Format")
            return
        try:
            ay2 = float(entry_ay2.text()) if entry_ay2 and entry_ay2.text() else 0
        except:
            QMessageBox.information(None, "Ay2", "Incorrect Ay2 Format")
            return
        try:
            ny2 = int(entry_ny2.text()) if entry_ny2 and entry_ny2.text() else 0
        except:
            QMessageBox.information(None, "ny2", "Incorrect ny2 Format")
            return
        try:
            az2 = float(entry_az2.text()) if entry_az2 and entry_az2.text() else 0
        except:
            QMessageBox.information(None, "Az2", "Incorrect Az2 Format")
            return
        try:
            nz2 = int(entry_nz2.text()) if entry_nz2 and entry_nz2.text() else 0
        except:
            QMessageBox.information(None, "nz2", "Incorrect nz2 Format")
            return
        
        #L Validación de campos lambda
        try:
            nx_lambda = int(entry_nx_lambda.text()) if entry_nx_lambda and entry_nx_lambda.text() else None
        except:
            QMessageBox.information(None, "nx_lambda", "Incorrect nx_lambda Format")
            return
        try:
            ny_lambda = int(entry_ny_lambda.text()) if entry_ny_lambda and entry_ny_lambda.text() else None
        except:
            QMessageBox.information(None, "ny_lambda", "Incorrect ny_lambda Format")
            return
        try:
            nz_lambda = int(entry_nz_lambda.text()) if entry_nz_lambda and entry_nz_lambda.text() else None
        except:
            QMessageBox.information(None, "nz_lambda", "Incorrect nz_lambda Format")
            return
        print("Lambda params:", nx_lambda, ny_lambda, nz_lambda)

        #L Obtener valores senoidales para E1
        ax = float(entry_ax.text()) if entry_ax and entry_ax.text() else 0
        nx = int(entry_nx.text()) if entry_nx and entry_nx.text() else 0
        ay = float(entry_ay.text()) if entry_ay and entry_ay.text() else 0
        ny = int(entry_ny.text()) if entry_ny and entry_ny.text() else 0
        az = float(entry_az.text()) if entry_az and entry_az.text() else 0
        nz = int(entry_nz.text()) if entry_nz and entry_nz.text() else 0

        #L Obtener valores senoidales para E2
        ax2 = float(entry_ax2.text()) if entry_ax2 and entry_ax2.text() else 0
        nx2 = int(entry_nx2.text()) if entry_nx2 and entry_nx2.text() else 0
        ay2 = float(entry_ay2.text()) if entry_ay2 and entry_ay2.text() else 0
        ny2 = int(entry_ny2.text()) if entry_ny2 and entry_ny2.text() else 0
        az2 = float(entry_az2.text()) if entry_az2 and entry_az2.text() else 0
        nz2 = int(entry_nz2.text()) if entry_nz2 and entry_nz2.text() else 0

        #L Imprimir los valores capturados:
        print("Valores senoidales E1:", ax, nx, ay, ny, az, nz)
        print("Valores senoidales E2:", ax2, nx2, ay2, ny2, az2, nz2)

        QMessageBox.information(None, "Senoidales capturados",
            f"E1: {ax}, {nx}, {ay}, {ny}, {az}, {nz}\nE2: {ax2}, {nx2}, {ay2}, {ny2}, {az2}, {nz2}")

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
                                        nombre_resultante,nombre_resultante2,nombre_variables,nombre_variables2,value_x,value_y,value_z,value_x2,value_y2,value_z2,
                                        ax, nx, ay, ny, az, nz, ax2, nx2, ay2, ny2, az2, nz2, nx_lambda, ny_lambda, nz_lambda)
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
                                        nombre_resultante,nombre_resultante2,nombre_variables,nombre_variables2,value_x,value_y,value_z,value_x2,value_y2,value_z2,
                                        ax, nx, ay, ny, az, nz, ax2, nx2, ay2, ny2, az2, nz2, nx_lambda, ny_lambda, nz_lambda)
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
                                        nombre_resultante,nombre_resultante2,nombre_variables,nombre_variables2,value_x,value_y,value_z,value_x2,value_y2,value_z2,
                                        ax, nx, ay, ny, az, nz, ax2, nx2, ay2, ny2, az2, nz2, nx_lambda, ny_lambda, nz_lambda)
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
                                        nombre_resultante,nombre_resultante2,nombre_variables,nombre_variables2,value_x,value_y,value_z,value_x2,value_y2,value_z2,
                                        ax, nx, ay, ny, az, nz, ax2, nx2, ay2, ny2, az2, nz2, nx_lambda, ny_lambda, nz_lambda)
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
