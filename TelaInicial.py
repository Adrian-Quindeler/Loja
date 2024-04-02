from Funções import Funcoes
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.funcoes = Funcoes()
        self.leftDistance = -120
        self.topDistance = 500
        self.quantity = {}
        self.position = {}
        self.price = {"pc":12345, "teclado":10, "mouse":5, "monitor":10, "mousepad":2, "processador":20, "ssd":20, "cooler" :15, "item1":20,   "item2":20}
        self.createAllItems()
        self.createButtons()
        self.loadWindow()

    def loadWindow(self):
        self.setGeometry(0, 0, 1280,720)
        self.setWindowTitle("Adrian's & Adrian's LTDA.")
        self.setStyleSheet("QMainWindow {background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop: 0 #000540, stop: 1 #1bdeb4); }")
        self.show()

    def createButtons(self):

        home = self.funcoes.createButton(self, "Eletronic Paradise", 950, 10, 320, 50,  
                                'QPushButton {background-color:#000540; border-radius: 25px; font:bold; font-size:30px; color: white}')

        viewProductDetails = self.funcoes.createButton(self, "Ver as especificações", 420, 20, 170, 30, 
                                'QPushButton {background-color:#000540; border-radius: 15; font:bold; font-size:14px; color: white}')

        removeFromCart = self.funcoes.createButton(self, "Remover do carrinho", 740, 20, 160, 30,
                                'QPushButton {background-color:#000540; border-radius: 15; font:bold; font-size:14; color: white}')

        welcomeLabel = self.funcoes.createLabel(self, "Seja bem vindo!", 10, 10, 400, 60,
                                "QLabel {font: bold; font-size: 45px; color: black;  padding: 10px}")
        
        viewProductDetails.clicked.connect(self.onViewProductDetailsClicked)
        removeFromCart.clicked.connect(self.onRemoveFromCartClicked)
    
    def createAllItems(self):  
        pc = self.funcoes.createItemToAdd        (self,  10, 100, "imagens/Medias/pc_m.jpg",          "Supremacy Ultra: o ápice da tecnologia encapsulada em um computador excepcionalmente poderoso e esteticamente impressionante.")
        teclado = self.funcoes.createItemToAdd   (self, 330, 100, "imagens/Medias/teclado_m.jpg",     "Teclado mecânico com uma experiência de digitação excepcional! Combina durabilidade, precisão e conforto em um design elegante e excêntrico.")
        monitor = self.funcoes.createItemToAdd   (self, 650, 100, "imagens/Medias/monitor_m.jpg",     "VisionXtreme: Com resolução Ultra HD 4K, taxa de atualização de 144Hz e tecnologia HDR, oferece imagens nítidas e vibrantes para uma experiência visual imersiva.")
        mouse = self.funcoes.createItemToAdd     (self, 970, 100, "imagens/Medias/mouse_m.jpg",       "PhantomGrip: o Mouse Gamer de Elite Projetado para proporcionar precisão, velocidade e conforto como nenhum outro.")
        processador= self.funcoes.createItemToAdd(self,  10, 240, "imagens/Medias/processador_m.jpg", "HyperCore: Perfeito para Desempenho Computacional! Equipado com tecnologia de ponta, tem potência para lidar com as tarefas mais exigentes")
        ssd = self.funcoes.createItemToAdd       (self, 330, 240, "imagens/Medias/ssd_m.jpg",         "TurboDrive: o SSD de Elite completo! Com capacidades de armazenamento e velocidades de leitura/gravação ultra-rápidas e alta confiabilidade")
        cooler = self.funcoes.createItemToAdd    (self, 650, 240, "imagens/Medias/cooler_m.jpg",      "FrostBlast: o Cooler perfeito para seu Desempenho de Refrigeração! Oferece resfriamento excepcional e silencio para seu sistema.")
        item1 = self.funcoes.createItemToAdd     (self, 970, 240, "imagens/Medias/pc_m.jpg") 
        mousepad = self.funcoes.createItemToAdd  (self,  10, 380, "imagens/Medias/mousepad_m.jpg",    "HyperGlide Pro: o Mousepad de Elite para sua Precisão e Conforto de Movimento!") 
        item2 = self.funcoes.createItemToAdd     (self, 330, 380, "imagens/Medias/pc_m.jpg") 

        pc.clicked.connect         (lambda: self.onAddToCartClicked('pc'))
        teclado.clicked.connect    (lambda: self.onAddToCartClicked('teclado'))
        monitor.clicked.connect    (lambda: self.onAddToCartClicked('monitor'))
        mouse.clicked.connect      (lambda: self.onAddToCartClicked('mouse'))       
        mousepad.clicked.connect   (lambda: self.onAddToCartClicked('mousepad'))
        processador.clicked.connect(lambda: self.onAddToCartClicked('processador'))
        ssd.clicked.connect        (lambda: self.onAddToCartClicked('ssd'))
        cooler.clicked.connect     (lambda: self.onAddToCartClicked('cooler'))
        item1.clicked.connect      (lambda: self.onAddToCartClicked('item1'))
        item2.clicked.connect      (lambda: self.onAddToCartClicked('item2'))

    def onHomeClicked(self):
        self.__init__()

    def onViewProductDetailsClicked(self):
        print("Botão 'Ver as especificações' clicado.") 

    def onAddToCartClicked(self, produto):

        if len(self.quantity) == 0:
            self.funcoes.createLabel(self, " ", 10, 505, 1260, 200, "QLabel {font: bold; font-size: 45px; background: white; border-radius: 25px; padding: 10px}")
        finalizePurchase = self.funcoes.createButton(self, "Finalizar Compra", 1060, 510, 200, 45, 'QPushButton {background-color:#000540; border-radius: 20px; font:bold; font-size:22px; color: white}')
        finalizePurchase.show()
        
        if(self.isInDict(produto, self.quantity)):
            self.quantity[produto] += 1
        else:
            self.quantity[produto] = 1

        path = (f"imagens/Pequenas/{produto}_p.jpg")

        if(self.leftDistance > 900):
            self.leftDistance = -120
            self.topDistance = 590
        if(self.isInDict(produto, self.position)):
            self.funcoes.createItemInCart(self, self.position[produto][0], self.position[produto][1], path, self.quantity[produto], self.price[produto])
        else:
            self.leftDistance += 150
            self.position[produto] = [self.leftDistance, self.topDistance]
            self.funcoes.createItemInCart(self, self.position[produto][0], self.position[produto][1], path, self.quantity[produto], self.price[produto])

        finalizePurchase.clicked.connect(lambda: self.onFinalizePurchaseClicked(produto))

    def onRemoveFromCartClicked(self):
        print("Botão 'Remover produto do carrinho' clicado.")

    def onFinalizePurchaseClicked(self, produto):
        print("A")
    
    def isInDict(self, produto, dict):
        for key in dict.keys():
            if(produto == key):
               return True
        return False
