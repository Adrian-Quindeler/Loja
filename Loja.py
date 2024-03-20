import sys
from PyQt5.QtWidgets import QApplication
from TelaInicial import * 

def run_app():
    app = QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())

run_app()