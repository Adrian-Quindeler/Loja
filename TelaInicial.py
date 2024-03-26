from Funções import Funcoes
from PyQt5.QtWidgets import QLabel, QMainWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ProductList = []
        self.Quantity = {"pc":0, "teclado":0, "mouse":0, "monitor":0, "mousepad":0, "processador":0,
                        "ssd":0, "cooler" :0, "item1":0,   "item2":0}
        self.windowHeight = 800
        self.windowWidth = 1280 
        self.title = "Adrian's & Adrian's LTDA."
        self.createAllItems()
        self.createButtons()
        self.loadWindow()

    def loadWindow(self):
        self.setGeometry(0, 0, self.windowWidth, self.windowHeight)
        self.setWindowTitle(self.title)
        self.setStyleSheet("QMainWindow {background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop: 0 #000540, stop: 1 #1bdeb4); }")
        self.show()


    def createButtons(self):

        home = Funcoes.createButton(self, "Eletronic Paradise", 950, 10, 320, 50,  
                                'QPushButton {background-color:#000540; border-radius: 25px; font:bold; font-size:30px; color: white}')

        viewProductDetails = Funcoes.createButton(self, "Ver as especificações", 420, 20, 170, 30, 
                                'QPushButton {background-color:#000540; border-radius: 40px; font:bold; font-size:14px; color: white}')

        removeFromCart = Funcoes.createButton(self, "Remover do carrinho", 740, 20, 160, 30,
                                'QPushButton {background-color:#000540; border-radius: 40px; font:bold; font-size:14; color: white}')

        welcomeLabel = Funcoes.createButton(self, "Seja bem vindo!", 10, 10, 400, 60,
                                "QLabel {font: bold; font-size: 45px; color: black;  padding: 10px}")
        
        viewProductDetails.clicked.connect(self.on_view_product_details_clicked)
        removeFromCart.clicked.connect(self.on_remove_from_cart_clicked)
    
    def createAllItems(self):  
        pc = Funcoes.createItemToAdd        (self, 10, 100, "imagens/Medias/pc_m.jpg",          "Supremacy Ultra: o ápice da tecnologia encapsulada em um computador excepcionalmente poderoso e esteticamente impressionante.")
        teclado = Funcoes.createItemToAdd   (self, 330, 100, "imagens/Medias/teclado_m.jpg",     "Teclado mecânico com uma experiência de digitação excepcional! Combina durabilidade, precisão e conforto em um design elegante e excêntrico.")
        monitor = Funcoes.createItemToAdd   (self, 650, 100, "imagens/Medias/monitor_m.jpg",     "VisionXtreme: Com resolução Ultra HD 4K, taxa de atualização de 144Hz e tecnologia HDR, oferece imagens nítidas e vibrantes para uma experiência visual imersiva.")
        mouse = Funcoes.createItemToAdd     (self, 970, 100, "imagens/Medias/mouse_m.jpg",       "PhantomGrip: o Mouse Gamer de Elite Projetado para proporcionar precisão, velocidade e conforto como nenhum outro.")
        processador= Funcoes.createItemToAdd(self,  10, 240, "imagens/Medias/processador_m.jpg", "HyperCore: Perfeito para Desempenho Computacional! Equipado com tecnologia de ponta, tem potência para lidar com as tarefas mais exigentes")
        ssd = Funcoes.createItemToAdd       (self, 330, 240, "imagens/Medias/ssd_m.jpg",         "TurboDrive: o SSD de Elite completo! Com capacidades de armazenamento e velocidades de leitura/gravação ultra-rápidas e alta confiabilidade")
        cooler = Funcoes.createItemToAdd    (self, 650, 240, "imagens/Medias/cooler_m.jpg",      "FrostBlast: o Cooler perfeito para seu Desempenho de Refrigeração! Oferece resfriamento excepcional e silencio para seu sistema.")
        item1 = Funcoes.createItemToAdd     (self, 970, 240, "imagens/Medias/pc_m.jpg") 
        mousepad = Funcoes.createItemToAdd  (self,  10, 380, "imagens/Medias/mousepad_m.jpg",    "HyperGlide Pro: o Mousepad de Elite para sua Precisão e Conforto de Movimento!") 
        item2 = Funcoes.createItemToAdd     (self, 330, 380, "imagens/Medias/pc_m.jpg") 

        pc.clicked.connect         (lambda: self.on_add_to_cart_clicked('pc'))
        teclado.clicked.connect    (lambda: self.on_add_to_cart_clicked('teclado'))
        monitor.clicked.connect    (lambda: self.on_add_to_cart_clicked('monitor'))
        mouse.clicked.connect      (lambda: self.on_add_to_cart_clicked('mouse'))       
        mousepad.clicked.connect   (lambda: self.on_add_to_cart_clicked('mousepad'))
        processador.clicked.connect(lambda: self.on_add_to_cart_clicked('processador'))
        ssd.clicked.connect        (lambda: self.on_add_to_cart_clicked('ssd'))
        cooler.clicked.connect     (lambda: self.on_add_to_cart_clicked('cooler'))
        item1.clicked.connect      (lambda: self.on_add_to_cart_clicked('item1'))
        item2.clicked.connect      (lambda: self.on_add_to_cart_clicked('item2'))

    def on_home_clicked(self):
        self.__init__()

    def on_view_product_details_clicked(self):
        print("Botão 'Ver as especificações' clicado.") 

    def on_add_to_cart_clicked(self, produto):
        if len(self.ProductList) == 0:
            background = QLabel(self)
            background.move(10, 500)
            background.resize(1260, 200)
            background.setStyleSheet("QLabel {font: bold; font-size: 45px; color: black; background: white; border-radius: 25px; padding: 10px}")
            finalizePurchase = self.createButton("Finalizar Compra", 1055, 505, 210, 50, 
                                'QPushButton {background-color:#000540; border-radius: 25px; font:bold; font-size:22px; color: white}')
            finalizePurchase.clicked.connect(self.on_finalize_purchase_clicked)
            background.show()
            finalizePurchase.show()

        self.ProductList.append(produto)
        print(f"Produto {produto} adicionado ao carrinho.")

    def on_remove_from_cart_clicked(self):
        print("Botão 'Remover produto do carrinho' clicado.")

    def on_finalize_purchase_clicked(self):
        print("Botão 'Finalizar Compra' clicado.")
