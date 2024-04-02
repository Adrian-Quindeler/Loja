from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5 import QtGui

class Funcoes:
    
    def createLabel(self, parent, text, leftDistance, topDistance, width, height, style):
        label = QLabel(parent)
        label.setWordWrap(True)
        label.setText(text)
        label.move(leftDistance, topDistance)
        label.resize(width, height)
        label.setStyleSheet(style)
        label.show()

    def createImage(self, parent, leftDistance, topDistance, path, width=100, height=100):
        image = QLabel(parent)
        image.move(leftDistance, topDistance)
        image.resize(width, height)
        image.setPixmap(QtGui.QPixmap(path))
        return image

    def createButton(self, parent, text, leftDistance, topDistance, width, height, style):
        button = QPushButton(text, parent)
        button.move(leftDistance, topDistance)
        button.resize(width, height)
        button.setStyleSheet(style)
        return button

    def createItemToAdd(self, parent, leftDistance, topDistance, path, description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."):
        self.createImage(parent, leftDistance, topDistance, path)
        self.createLabel(parent, description, leftDistance + 110, topDistance, 190, 100,
                                "QLabel {font: bold; font-size: 14px; color: black; padding: 0 0 0 0}")
        add_to_cart = self.createButton(parent, "+", leftDistance + 90, topDistance + 90, 25, 25, 
                            'QPushButton {background-color:#000540; color: white; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0;}')
        return add_to_cart

    def createItemToAddRemove(self, parent, leftDistance, topDistance, path, description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."):
        self.createImage(parent, leftDistance, topDistance, path)
        self.createLabel(parent, description, leftDistance + 110, topDistance, 190, 100,
                                "QLabel {font: bold; font-size: 14px; color: black; padding: 0 0 0 0}")
        add_to_cart = self.createButton(parent, "+", leftDistance + 90, topDistance + 90, 25, 25, 
                            'QPushButton {background-color:#000540; color: white; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0;}')
        return add_to_cart
    
    def createItemInCart(self, parent, leftDistance, topDistance, path, quantity, price):
        self.createLabel(parent, "" , leftDistance, topDistance+20, 130, 70, "QLabel {background: white}")


        image = self.createImage(parent, leftDistance, topDistance, path)
        image.show()

        self.createLabel(parent,          "R$ "+str(price), leftDistance + 65, topDistance+20, 80, 20, "QLabel {font: bold; font-size: 14px; color: black;}")
        self.createLabel(parent,                 "total: ", leftDistance + 65, topDistance+50, 30, 10, "QLabel {font: bold; font-size: 10px; color: black;}")
        self.createLabel(parent, "R$ "+str(price*quantity), leftDistance + 65, topDistance+60, 80, 10, "QLabel {font: bold; font-size: 10px; color: black;}")
        
        if(quantity <= 9):
            self.createLabel(parent, str(quantity), leftDistance + 50, topDistance + 70, 20, 20, 
                            ("QLabel {font: bold; font-size: 24; border-radius: 10px; background: black; color: white;  padding: 0 0 2px 3px}"))
        else:
            self.createLabel(parent, str(quantity), leftDistance + 47, topDistance + 70, 25, 25, 
                            ("QLabel {font: bold; font-size: 24; border-radius: 12px; background: black; color: white;  padding: 0 0 2px 3px}"))
        
