from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5 import QtGui

class Funcoes:
    def createImage(self, leftDistance, topDistance, path, width = 100, height = 100):
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

    def createItemToAdd(self, leftDistance, topDistance, path, description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."):
        image = self.createImage(leftDistance, topDistance, path)
        label = self.createLabel(description, leftDistance+110, topDistance, 190, 100,
                                "QLabel {font: bold; font-size: 14px; color: black; padding: 0 0 0 0}")
        addToCart = self.createButton("+", leftDistance+90, topDistance+90, 25, 25, 
                            'QPushButton {background-color:#000540; color: white; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0;}')
        return addToCart

    def createItemToAddRemove(self, leftDistance, topDistance, path, description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."):
        image = self.createImage(leftDistance, topDistance, path)
        label = self.createLabel(description, leftDistance+110, topDistance, 190, 100,
                                "QLabel {font: bold; font-size: 14px; color: black; padding: 0 0 0 0}")
        addToCart = self.createButton("+", leftDistance+90, topDistance+90, 25, 25, 
                            'QPushButton {background-color:#000540; color: white; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0;}')
        return addToCart