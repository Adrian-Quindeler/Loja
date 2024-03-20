import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topDistance = 100
        self.leftDistance = 100
        self.windowHeight = 800
        self.windowWidth = 1024
        self.title = "Adrian's & Adrian's LTDA."
        self.createAllItems()
        self.createButtons()
        self.loadWindow()

    def loadWindow(self):
        self.setGeometry(self.leftDistance, self.topDistance, self.windowWidth, self.windowHeight)
        self.setWindowTitle(self.title)
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop: 0 #000540, stop: 1 #1bdeb4);
            }
        """)
        self.show()


    def createButtons(self):

        home = self.createButton("Eletronic Paradise", 20, 10, 300, 50,
                                'QPushButton {background-color:#000540; font:bold; font-size:28px; color: white}')

        viewProductDetails = self.createButton("Ver as especificações", 340, 20, 170, 30,
                                'QPushButton {background-color:#000540; font:bold; font-size:14px; color: white}')

        removeFromCart = self.createButton("Remover do carrinho", 530, 20, 160, 30,
                                'QPushButton {background-color:#000540; font:bold; font-size:14px; color: white}')
        
        viewSelectedProducts = self.createButton("Ver Carrinho", 720, 20, 100, 30,
                                'QPushButton {background-color:#000540; font:bold; font-size:14px; color: white}')

        finalizePurchase = self.createButton("Finalizar Compra", 850, 700, 150, 30,
                                'QPushButton {background-color:#000540; font:bold; font-size:14px; color: white}')

        welcomeLabel = QLabel(self)
        welcomeLabel.setText("Seja bem vindo!")
        welcomeLabel.move(20, 100)
        welcomeLabel.resize(300, 50)
        welcomeLabel.setStyleSheet("QLabel {font: bold; font-size: 30px; color: white; background-color:#000540; border-radius: 10px; padding: 10px}")
        home.clicked.connect(self.on_home_clicked)
        viewProductDetails.clicked.connect(self.on_view_product_details_clicked)
        removeFromCart.clicked.connect(self.on_remove_from_cart_clicked)
        viewSelectedProducts.clicked.connect(self.on_view_selected_products_clicked)
        finalizePurchase.clicked.connect(self.on_finalize_purchase_clicked)
    
    def createAllItems(self):  
        pc = self.createItem(30,  200, "imagens/pequenas/pc_p.jpg")
        teclado = self.createItem(230, 200, "imagens/pequenas/teclado_p.jpg")
        mouse = self.createItem(430, 200, "imagens/pequenas/mouse_p.jpg")
        monitor = self.createItem(630, 200, "imagens/pequenas/monitor_p.jpg")
        mousepad = self.createItem(830, 200, "imagens/pequenas/mousepad_p.png")
        processador = self.createItem(230, 500, "imagens/pequenas/processador_p.jpg")
        ssd = self.createItem(30,  500, "imagens/pequenas/ssd_p.jpg")
        cooler = self.createItem(430, 500, "imagens/pequenas/cooler_p.jpg")
        item1 = self.createItem(630, 500, "imagens/pequenas/pc_p.jpg")
        item2 = self.createItem(830, 500, "imagens/pequenas/pc_p.jpg")

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

    def createImage(self, leftDistance, topDistance, path):
        image = QLabel(self)
        image.move(leftDistance, topDistance)
        image.resize(150, 150)
        image.setPixmap(QtGui.QPixmap(path))

    def createButton(self, text, leftDistance, topDistance, width, height, style):
        button = QPushButton(text, self)
        button.move(leftDistance, topDistance)
        button.resize(width, height)
        button.setStyleSheet(style)
        return button
    
    def createItem(self, leftDistance, topDistance, path):
        self.createImage(leftDistance, topDistance, path)
        addToCart = self.createButton("+", leftDistance+135, topDistance+135, 25, 25,
                            'QPushButton {background-color:#000540; color: white; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0;}')
        return addToCart

    def on_home_clicked(self):
        print("Botão 'HOME' clicado.")

    def on_view_product_details_clicked(self):
        print("Botão 'Ver as especificações' clicado.")

    def on_add_to_cart_clicked(self, produto):
        print(f"{produto} clicado.")

    def on_remove_from_cart_clicked(self):
        print("Botão 'Remover produto do carrinho' clicado.")

    def on_view_selected_products_clicked(self):
        print("Botão 'Ver produtos selecionados' clicado.")

    def on_finalize_purchase_clicked(self):
        print("Botão 'Finalizar Compra' clicado.")
