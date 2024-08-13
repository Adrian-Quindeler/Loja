import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow as TelaInicialMainWindow  

app = QApplication(sys.argv)
ui = TelaInicialMainWindow()
sys.exit(app.exec_())
 