from CreateOne import *
from CreateMany import *
from PyQt5.QtWidgets import QMainWindow, QWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.createMany = CreateMany()
        self.createOne = CreateOne()
        self.leftDistance = -140
        self.topDistance = 500
        self.all = []
        self.labels= {}
        self.quantity = {}
        self.position = {}
        self.price = {"pc":6500.69, "teclado":180.50, "mouse":65.5, "monitor":680.10, "mousepad":59.99, "processador":4000.75, "ssd":450.20, "cooler" :30.15, "placaVideo":1900.30, "fone":60.96, "ram":50.00, "gabinete":50.50}
        self.createHeader()
        CreateMany.firstScreen(self)
        CreateMany.itemsToAdd(self)
        self.loadWindow()

    def loadWindow(self):
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle("Adrian's & Adrian's LTDA.")
        self.setStyleSheet("QMainWindow {background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop: 0 #493AE0, stop: 1 #51CFE0); }")
        self.show()

    def createHeader(self):
        self.createOne.label(self, "Eletronic Paradise", 950, 10, 320, 50, 'QLabel {background-color:#000540; border-radius: 16px; font:bold; font-size:30px; color: white; padding: 0 0 0 15px}')
        self.createOne.label(self, "Seja bem vindo!",     0,  0, 400, 60, "QLabel {font: bold; font-size: 45px; color: black;  padding: 10px}")

        addToCart = self.createOne.button         (self, "Adicionar ao carrinho", 415, 22, 170, 30, 'QPushButton {background-color:#000540; border-radius: 15; font:bold; font-size:14px; color: white}')
        viewProductDetails = self.createOne.button(self, "Ver as especificações", 600, 22, 160, 30, 'QPushButton {background-color:#000540; border-radius: 15; font:bold; font-size:14px; color: white}')
        removeFromCart = self.createOne.button    (self, "Remover do carrinho",   780, 22, 160, 30, 'QPushButton {background-color:#000540; border-radius: 15; font:bold; font-size:14px; color: white}')
    
        viewProductDetails.clicked.connect(lambda: CreateMany.itemDetails(self))
        removeFromCart.clicked.connect(lambda: CreateMany.itemsToRemove(self))
        addToCart.clicked.connect(lambda: CreateMany.itemsToAdd(self))

    def onAddToCartClicked(self, product):
        self.all.append(product)
        self.AddToCart(product)

    def AddToCart(self, product):
        if len(self.quantity) == 0:
            self.createOne.label(self, " ", 10, 505, 1260, 200, "QLabel {font: bold; font-size: 45px; background: white; border-radius: 25px; padding: 10px}")
            self.labels["total"] = self.createOne.newTotal(self, self.price, self.quantity)
        finalizePurchase = self.createOne.button(self, "Finalizar Compra", 1065, 510, 200, 45, 'QPushButton {background-color:#000540; border-radius: 20px; font:bold; font-size:22px; color: white}')
        finalizePurchase.show()

        if(self.isInDict(product, self.quantity)):
            self.quantity[product] += 1
        else:
            self.quantity[product] = 1

        path = (f"imagens/Pequenas/{product}_p.jpg")
        if(self.leftDistance > 800):
            self.leftDistance = -140
            self.topDistance = 590
            
        if(self.isInDict(product, self.position)):
            self.createOne.updateItemInCart(self.labels[product][0], self.labels[product][1], self.price[product], self.quantity[product])
        else:
            self.leftDistance += 170
            self.position[product] = [self.leftDistance, self.topDistance]
            self.labels[product] = self.createOne.newItemInCart(self, self.position[product][0], self.position[product][1], path, self.quantity[product], self.price[product])

        self.createOne.updateTotal(self.price, self.quantity, self.labels["total"])
        finalizePurchase.clicked.connect(self.onFinalizePurchaseClicked)
    
    def removeFromCart(self, product):
        if(product in self.all):
            self.clearCartDisplay()
            self.all.remove(product)
            for item in self.all:
                self.AddToCart(item)
        if(len(self.all) == 0 ):
            self.createOne.label(self, " ", 10, 505, 1260, 200, "QLabel {font: bold; font-size: 45px; background: white; border-radius: 25px; padding: 10px}")
            self.labels["total"] = self.createOne.newTotal(self, self.price, self.quantity)
            CreateMany.itemsToAdd(self)

    def clearCartDisplay(self):
        self.leftDistance = -140
        self.topDistance = 500
        self.labels = {}
        self.quantity = {}
        self.position = {}
    
    def clearScreen(self):
        for widget in self.findChildren(QWidget):
            widget.deleteLater()
    
    def restoreScreen(self):
        self.clearScreen()
        self.clearCartDisplay()
        self.createHeader()
        CreateMany.firstScreen(self)
        CreateMany.itemsToAdd(self)
        for item in self.all:
            self.AddToCart(item)

    def productDetails(self, product, description1, description2):
        self.clearScreen()
        self.createOne.detailsScreem(self, product, description1, description2)
        button = self.createOne.button(self, "Voltar", 1100, 650, 120, 40, 'QPushButton {background-color:#000540; border-radius: 20px; font:bold; font-size:24px; color: white}')
        button.clicked.connect(self.restoreScreen)

    def onFinalizePurchaseClicked(self, produto):
        print("A")
    
    def isInDict(self, produto, dict):
        for key in dict.keys():
            if(produto == key):
               return True
        return False
