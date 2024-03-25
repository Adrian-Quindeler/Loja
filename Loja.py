import sys
from PyQt5.QtWidgets import QApplication
from TelaInicial import MainWindow as TelaInicialMainWindow  # Importar a classe MainWindow de TelaInicial.py

def run_app():
    app = QApplication(sys.argv)
    ui = TelaInicialMainWindow()  # Criar uma instância da classe MainWindow do módulo TelaInicial
    sys.exit(app.exec_())


run_app()
