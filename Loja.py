import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow as TelaInicialMainWindow  

def run_app():
    app = QApplication(sys.argv)
    ui = TelaInicialMainWindow()
    sys.exit(app.exec_())

run_app()
