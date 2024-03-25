import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QMainWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ProductList = []
        self.Quantity = {"pc":0, "teclado":0, "mouse":0, "monitor":0, "mousepad":0, "processador":0,
                        "ssd":0, "cooler" :0, "item1":0,   "item2":0}
        self.windowHeight = 800
        self.windowWidth = 1680
        self.title = "Adrian's & Adrian's LTDA."
        self.createAllItems()
        self.createButtons()
        self.loadWindow()

    def loadWindow(self):
        self.setGeometry(0, 100, self.windowWidth, self.windowHeight)
        self.setWindowTitle(self.title)
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop: 0 #000540, stop: 1 #1bdeb4);
            }
        """)
        self.show()


    def createButtons(self):

        home = self.createButton("Eletronic Paradise", 1350, 10, 320, 80,
                                'QPushButton {background-color:#000540; border-radius: 40px; font:bold; font-size:30px; color: white}')

        viewProductDetails = self.createButton("Ver as especificações", 600, 20, 170, 30,
                                'QPushButton {background-color:#000540; border-radius: 40px; font:bold; font-size:14px; color: white}')

        removeFromCart = self.createButton("Remover do carrinho", 1100, 20, 160, 30,
                                'QPushButton {background-color:#000540; border-radius: 40px; font:bold; font-size:14; color: white}')

        welcomeLabel = self.createLabel("Seja bem vindo!", 10, 10, 400, 80,
                                "QLabel {font: bold; font-size: 45px; color: black;  padding: 10px}")
        
        viewProductDetails.clicked.connect(self.on_view_product_details_clicked)
        removeFromCart.clicked.connect(self.on_remove_from_cart_clicked)
    
    def createAllItems(self):  
        pc = self.createItem(10,  170, "imagens/Medias/pc_m.jpg", "PC gamer completo de última geração")
        teclado = self.createItem(340, 170, "imagens/Medias/teclado_m.jpg")
        mouse = self.createItem(670, 170, "imagens/Medias/mouse_m.jpg")
        monitor = self.createItem(1010, 170, "imagens/Medias/monitor_m.jpg")
        mousepad = self.createItem(1350, 170, "imagens/Medias/mousepad_m.jpg")
        processador = self.createItem(10, 380, "imagens/Medias/processador_m.jpg")
        ssd = self.createItem(340,  380, "imagens/Medias/ssd_m.jpg")
        cooler = self.createItem(670, 380, "imagens/Medias/cooler_m.jpg")
        item1 = self.createItem(1010, 380, "imagens/Medias/pc_m.jpg")
        item2 = self.createItem(1350, 380, "imagens/Medias/pc_m.jpg")

        pc.clicked.connect(lambda: self.on_add_to_cart_clicked('pc'))
        teclado.clicked.connect(lambda: self.on_add_to_cart_clicked('teclado'))
        mouse.clicked.connect(lambda: self.on_add_to_cart_clicked('mouse'))
        monitor.clicked.connect(lambda: self.on_add_to_cart_clicked('monitor'))
        mousepad.clicked.connect(lambda: self.on_add_to_cart_clicked('mousepad'))
        processador.clicked.connect(lambda: self.on_add_to_cart_clicked('processador'))
        ssd.clicked.connect(lambda: self.on_add_to_cart_clicked('ssd'))
        cooler.clicked.connect(lambda: self.on_add_to_cart_clicked('cooler'))
        item1.clicked.connect(lambda: self.on_add_to_cart_clicked('item1'))
        item2.clicked.connect(lambda: self.on_add_to_cart_clicked('item2'))

    def createImage(self, leftDistance, topDistance, path, width = 150, height = 150):
        image = QLabel(self)
        image.move(leftDistance, topDistance)
        image.resize(width, height)
        image.setPixmap(QtGui.QPixmap(path))
        return image

    def createLabel(self, text, leftDistance, topDistance, width, height, style):
        label = QLabel(self)
        label.setWordWrap(True)
        label.setText(text)
        label.move(leftDistance, topDistance)
        label.resize(width, height)
        label.setStyleSheet(style)

    def createButton(self, text, leftDistance, topDistance, width, height, style):
        button = QPushButton(text, self)
        button.move(leftDistance, topDistance)
        button.resize(width, height)
        button.setStyleSheet(style)
        return button
    
    def createItem(self, leftDistance, topDistance, path, description = "PC gamer de última geração"):
        image = self.createImage(leftDistance, topDistance, path)
        label = self.createLabel(description, leftDistance+135, topDistance-50, 200, 150,
                                "QLabel {font: bold; font-size: 18px; color: black; padding: 10px}")
        addToCart = self.createButton("+", leftDistance+135, topDistance+135, 25, 25,
                            'QPushButton {background-color:#000540; color: white; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0;}')
        return addToCart

    def on_home_clicked(self):
        Loja.run_app

    def on_view_product_details_clicked(self):
        print("Botão 'Ver as especificações' clicado.")

    def on_add_to_cart_clicked(self, produto):
        if(len(self.ProductList) == 0):
            background = QLabel(self)
            background.move(10, 580)
            background.resize(1660, 200)
            background.setStyleSheet("QLabel {font: bold; font-size: 45px; color: black; background: white; border-radius: 25px; padding: 10px}")
            finalizePurchase = self.createButton("Finalizar Compra", 1440, 725, 225, 50,
                                'QPushButton {background-color:#000540; border-radius: 20px; font:bold; font-size:22px; color: white}')
            background.show()
            finalizePurchase.show()

        self.ProductList.append(produto)

        finalizePurchase.clicked.connect(self.on_finalize_purchase_clicked)
        

    def on_remove_from_cart_clicked(self):
        print("Botão 'Remover produto do carrinho' clicado.")

    def on_finalize_purchase_clicked(self):
        print("Botão 'Finalizar Compra' clicado.")
