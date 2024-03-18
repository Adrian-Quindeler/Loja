import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QGridLayout, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topDistance = 100
        self.leftDistance = 100
        self.windowHeight = 800
        self.windowWidth = 1024
        self.title = "Adrian's & Adrian's LTDA."
        self.createImages()
        self.createButtons()
        self.loadWindow()

    def loadWindow(self):
        self.setGeometry(self.leftDistance, self.topDistance, self.windowWidth, self.windowHeight)
        self.setWindowTitle(self.title)
        self.show()

    def createButtons(self):

        home = QPushButton("Eletronic Paradise", self)
        home.move(20, 10)
        home.resize(300, 50)
        home.setStyleSheet('QPushButton {background-color:#5a7eb8; font:bold; font-size:28px}')

        viewProductDetails = QPushButton("Ver as especificações", self)
        viewProductDetails.move(340, 20)
        viewProductDetails.resize(170, 30)
        viewProductDetails.setStyleSheet('QPushButton {background-color:#5a7eb8; font:bold; font-size:14px}')

        addToCart = QPushButton("Adicionar ao carrinho", self)
        addToCart.move(530, 20)
        addToCart.resize(170, 30)
        addToCart.setStyleSheet('QPushButton {background-color:#5a7eb8; font:bold; font-size:14px}')

        removeFromCart = QPushButton("Remover do carrinho", self)
        removeFromCart.move(720, 20)
        removeFromCart.resize(160, 30)
        removeFromCart.setStyleSheet('QPushButton {background-color:#5a7eb8; font:bold; font-size:14px}')

        viewSelectedProducts = QPushButton("Ver Carrinho", self)
        viewSelectedProducts.move(900, 20)
        viewSelectedProducts.resize(100, 30)
        viewSelectedProducts.setStyleSheet('QPushButton {background-color:#5a7eb8; font:bold; font-size:14px}')

        finalizePurchase = QPushButton("Finalizar Compra", self)
        finalizePurchase.move(850, 700)
        finalizePurchase.resize(150, 30)
        finalizePurchase.setStyleSheet('QPushButton {background-color:#5a7eb8; font:bold; font-size:14px}')

        welcomeLabel = QLabel(self)
        welcomeLabel.setText("Seja bem vindo!")
        welcomeLabel.move(20, 100)
        welcomeLabel.resize(300, 50)
        welcomeLabel.setStyleSheet("QLabel {font: bold; font-size: 30px; background-color:#5a7eb8; color: black; border-radius: 10px; padding: 10px}")

        home.clicked.connect(self.on_home_clicked)
        viewProductDetails.clicked.connect(self.on_view_product_details_clicked)
        addToCart.clicked.connect(self.on_add_to_cart_clicked)
        removeFromCart.clicked.connect(self.on_remove_from_cart_clicked)
        viewSelectedProducts.clicked.connect(self.on_view_selected_products_clicked)
        finalizePurchase.clicked.connect(self.on_finalize_purchase_clicked)
    
    def createImages(self):        
        self.cooler = QLabel(self)
        self.cooler.move(50, 200)
        self.cooler.resize(200, 200)
        self.cooler.setPixmap(QtGui.QPixmap('imagens/cooler-p.jpg'))

        self.fonte = QLabel(self)
        self.fonte.move(250, 250)
        self.fonte.resize(200, 100)
        self.fonte.setPixmap(QtGui.QPixmap('imagens/fonte-p.png'))

        self.gabinete = QLabel(self)
        self.gabinete.move(450, 200)
        self.gabinete.resize(200, 200)
        self.gabinete.setPixmap(QtGui.QPixmap('imagens/gabinete-p.jpg'))

        self.memoria = QLabel(self)
        self.memoria.move(650, 200)
        self.memoria.resize(200, 200)
        self.memoria.setPixmap(QtGui.QPixmap('imagens/memoria-ram-p.jpg'))

        self.monitor = QLabel(self)
        self.monitor.move(850, 200)
        self.monitor.resize(200, 200)
        self.monitor.setPixmap(QtGui.QPixmap('imagens/monitor-p.jpg'))

        self.mouse = QLabel(self)
        self.mouse.move(50, 500)
        self.mouse.resize(200, 200)
        self.mouse.setPixmap(QtGui.QPixmap('imagens/mouse-p.jpg'))

        self.mousepad = QLabel(self)
        self.mousepad.move(250, 500)
        self.mousepad.resize(200, 200)
        self.mousepad.setPixmap(QtGui.QPixmap('imagens/mousepad-p.jpg'))

        self.placa = QLabel(self)
        self.placa.move(450, 500)
        self.placa.resize(200, 200)
        self.placa.setPixmap(QtGui.QPixmap('imagens/placa-p.jpg'))

        self.processador = QLabel(self)
        self.processador.move(650, 500)
        self.processador.resize(200, 200)
        self.processador.setPixmap(QtGui.QPixmap('imagens/processador-p.jpg'))

        self.ssd = QLabel(self)
        self.ssd.move(850, 500)
        self.ssd.resize(200, 200)
        self.ssd.setPixmap(QtGui.QPixmap('imagens/ssd-p.jpg'))

    def on_home_clicked(self):
        print("Botão 'HOME' clicado.")

    def on_view_product_details_clicked(self):
        print("Botão 'Ver as especificações' clicado.")

    def on_add_to_cart_clicked(self):
        print("Botão 'Adicionar produto ao carrinho' clicado.")

    def on_remove_from_cart_clicked(self):
        print("Botão 'Remover produto do carrinho' clicado.")

    def on_view_selected_products_clicked(self):
        print("Botão 'Ver produtos selecionados' clicado.")

    def on_finalize_purchase_clicked(self):
        print("Botão 'Finalizar Compra' clicado.")
