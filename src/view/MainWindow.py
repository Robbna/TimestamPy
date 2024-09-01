from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from src.view.components.FontSelector import FontSelector
from src.utils.utils import Utils

class MainWindow:
    def __init__(self):
        app = QApplication([])

        # Configuración inicial, servicios, fuentes, etc.
        # Asumiendo que todo esto está correcto y no afecta la demostración

        # WINDOW CONFIGURATION
        window = QWidget()
        window.setWindowTitle("TimestamPy")
        window.setFixedSize(800, 600)
        # Asumo que la función Utils.resource_path maneja correctamente las rutas a los recursos
        window.setWindowIcon(QIcon(Utils.resource_path(".\\assets\\icon.ico")))
        
        # LAYOUT PRINCIPAL
        main_layout = QVBoxLayout(window)
        
        # CONFIGURACIÓN DEL ÁREA DESPLAZABLE PARA LOS ARCHIVOS
        scroll_area = QScrollArea()  # El área desplazable
        scroll_area.setWidgetResizable(True)
        scroll_area_container = QWidget()  # Contenedor para el contenido dentro del área desplazable
        scroll_files_layout = QVBoxLayout(scroll_area_container)  # Layout para el contenedor
        
        # Añadiendo 100 QLabel al layout dentro del contenedor
        for _ in range(100):
            label = QLabel("hola")
            scroll_files_layout.addWidget(label)
        
        scroll_area.setWidget(scroll_area_container)  # Establece el contenedor como el widget del área desplazable
        main_layout.addWidget(scroll_area)  # Añade el área desplazable al layout principal
        
        # Otros componentes y configuraciones
        # Asumiendo que estos están correctamente implementados y no afectan la demostración
        fonts = [1, 2, 3]
        label = QLabel("".join(map(str, fonts)))
        a = FontSelector(text="hola", fonts=fonts, onClick=lambda fonts: print(fonts))
        main_layout.addWidget(a)
        main_layout.addWidget(label)
        
        b = QPushButton("Add 1 to fonts")
        b.clicked.connect(lambda: fonts.append("1"))
        main_layout.addWidget(b)
        
        window.setLayout(main_layout)
        window.show()

        app.exec_()

