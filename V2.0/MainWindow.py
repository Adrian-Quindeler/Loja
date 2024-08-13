from CreateOne import *
from CreateMany import *
from Constants import *
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeAttributes()
        self.createHeader()
        CreateMany.firstScreen(self)
        CreateMany.itemsToAdd(self)
        self.loadWindow()

    def initializeAttributes(self):
        self.createMany = CreateMany()
        self.createOne = CreateOne()
        self.leftDistance = -140
        self.topDistance = 500
        self.all = []
        self.labels = {}
        self.quantity = {}
        self.position = {}
        self.price = PRECOS_PRODUTOS

    def loadWindow(self):
        self.setGeometry(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setWindowTitle("Adrian's & Adrian's LTDA.")
        self.setStyleSheet("QMainWindow {background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop: 0 #617DED, stop: 1 #61EDD7); }")
        self.show()

    def createHeader(self):
        self.createOne.label(self, "Electronic Paradise", 870, 0, 500, 80, "QLabel {font: bold; font-size: 38px; color: black;  padding: 10px}")
        self.createOne.label(self, "Seja bem-vindo!", 0, 0, 405, 80, "QLabel {font: bold; font-size: 38px; color: black;  padding: 10px}")

        addToCart = self.createOne.button(self, "Adicionar ao carrinho", 360, 22, 170, 30, BUTTON_STYLE)
        viewProductDetails = self.createOne.button(self, "Ver as especificações", 540, 22, 160, 30, BUTTON_STYLE)
        removeFromCart = self.createOne.button(self, "Remover do carrinho", 710, 22, 160, 30, BUTTON_STYLE)
    
        viewProductDetails.clicked.connect(lambda: CreateMany.itemDetails(self))
        removeFromCart.clicked.connect(lambda: CreateMany.itemsToRemove(self))
        addToCart.clicked.connect(lambda: CreateMany.itemsToAdd(self))

    def onAddToCartClicked(self, product):
        self.all.append(product)
        self.AddToCart(product)

    def isInDict(self, produto, dict):
        for key in dict.keys():
            if(produto == key):
               return True
        return False

    def AddToCart(self, product):
        if len(self.quantity) == 0:
            self.createOne.label(self, " ", 10, 505, 1260, 200, "QLabel {font: bold; font-size: 45px; background: white; border-radius: 25px; padding: 10px}")
            self.labels["total"] = self.createOne.newTotal(self, self.price, self.quantity)
        finalizePurchase = self.createOne.button(self, "Finalizar Compra", 1065, 520, 160, 30, BUTTON_STYLE)
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

    def productDetails(self, product, description1, description2):
        self.clearScreen()
        self.createOne.detailsScreem(self, product, description1, description2)
        button = self.createOne.button(self, "Voltar", 1100, 650, 120, 30, BUTTON_STYLE)
        button.clicked.connect(self.restoreScreen)

    def restoreScreen(self):
        self.clearScreen()
        self.clearCartDisplay()
        self.createHeader()
        CreateMany.firstScreen(self)
        CreateMany.itemsToAdd(self)
        for item in self.all:
            self.AddToCart(item)

    def onFinalizePurchaseClicked(self):
        self.clearScreen()
        self.createOne.label(self, "Obrigado por comprar na Electronic paradise, em parceria com Adrian's & Adrian's. Volte Sempre!", 200, 300, 850, 100, "QLabel {font: bold; font-size: 35px; color: black; background: white; border-radius: 25px; padding: 10px}")
        QTimer.singleShot(7000, self.close)