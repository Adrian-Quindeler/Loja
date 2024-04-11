from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5 import QtGui
import locale

class CreateMany:

    def __init__(self) -> None:
        self.total_price = 0
    
    def label(self, parent, text, leftDistance, topDistance, width, height, style):
        label = QLabel(parent)
        label.setWordWrap(True)
        label.setText(text)
        label.move(leftDistance, topDistance)
        label.resize(width, height)
        label.setStyleSheet(style)
        label.show()

        return label

    def image(self, parent, leftDistance, topDistance, path, width=100, height=100):
        image = QLabel(parent)
        image.move(leftDistance, topDistance)
        image.resize(width, height)
        image.setPixmap(QtGui.QPixmap(path))
        return image

    def button(self, parent, text, leftDistance, topDistance, width, height, style):
        button = QPushButton(text, parent)
        button.move(leftDistance, topDistance)
        button.resize(width, height)
        button.setStyleSheet(style)
        button.show()
        return button

    def itemToAdd(self, parent, leftDistance, topDistance, path, description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."):
        self.image(parent, leftDistance, topDistance, path)
        self.label(parent, description, leftDistance + 110, topDistance, 190, 100,
                                "QLabel {font: bold; font-size: 14px; color: black; padding: 0 0 0 0}")
        add_to_cart = self.button(parent, "+", leftDistance + 90, topDistance + 90, 25, 25, 
                            'QPushButton {background-color:#000540; color: white; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}')
        return add_to_cart

    def itemToRemove(self, product):
        product.setText('-')
        product.setStyleSheet('QPushButton {background-color:#D40000; color: white; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}')
        product.show()
        return product

    def newItemInCart(self, parent, leftDistance, topDistance, path, quantity, price):
        image = self.image(parent, leftDistance, topDistance, path)
        image.show()

        preco = self.formatar_moeda(price)
        valor = self.formatar_moeda(price*quantity)
        self.label(parent,     preco, leftDistance + 65, topDistance+20,  90, 20, "QLabel {font-size: 14px; color: black;}")
        self.label(parent, "total: ", leftDistance + 65, topDistance+50,  30, 10, "QLabel {font-size: 12px; color: black;}")
        
        priceLabel = self.label(parent,     valor, leftDistance + 65, topDistance+60, 105, 12, "QLabel {font-size: 10px; color: black;}")
        quantityLabel = self.label(parent, str(quantity), leftDistance + 50, topDistance + 70, 20, 20,("QLabel {font: bold; font-size: 24; border-radius: 10px; background: black; color: white;  padding: 0 0 2px 3px}"))
        return[priceLabel, quantityLabel]

    def updateItemInCart(self, priceLabel, quantityLabel, price, quantity):
        valor = self.formatar_moeda(price*quantity)
        priceLabel.setText(str(valor))
        if(quantity <= 9):
            quantityLabel.setText(str(quantity))
        else:
            quantityLabel.resize(25, 25)
            quantityLabel.setStyleSheet("QLabel {font: bold; font-size: 24; border-radius: 12px; background: black; color: white;  padding: 0 0 2px 3px}")
            quantityLabel.setText(str(quantity))
            
    def calcularTotal(self, price, quantity):
        self.total_price = 0
        for key in quantity.keys():
            for k in price.keys():
                if(str(key) == str(k)):
                    self.total_price += (price[k] * quantity[key])
                    break
    
    def newTotal(self, parent, price, quantity):
        self.calcularTotal(price, quantity)
        valor = self.formatar_moeda(self.total_price)
        self.label(parent,      " ", 1070, 580, 150,100, "QLabel {background: white}")
        self.label(parent,"total: ", 1070, 580,  80, 20, "QLabel {font: bold; font-size: 18px; color: black;}")
        priceLabel = self.label(parent, valor, 1070, 610, 180, 20, "QLabel {background: white; font: bold; font-size: 15px; color: black;}")
        return priceLabel

    def updateTotal(self, price, quantity, priceLabel):
        self.calcularTotal(price, quantity)
        valor = self.formatar_moeda(self.total_price)
        priceLabel.setText(str(valor))

    def formatar_moeda(self, valor):
        return locale.currency(valor, grouping=True)

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
