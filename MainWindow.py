from CreateOne import *
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.createOne = CreateOne()
        self.leftDistance = -140
        self.topDistance = 500
        self.all = []
        self.labels= {}
        self.quantity = {}
        self.position = {}
        self.price = {"pc":6500.69, "teclado":180.50, "mouse":65.5, "monitor":680.10, "mousepad":59.99, "processador":4000.75, "ssd":450.20, "cooler" :30.15, "placaVideo":1900.30, "fone":60.96, "ram":50.00, "gabinete":50.50}
        self.createAllToAdd()
        self.createButtons()
        self.loadWindow()

    def loadWindow(self):
        self.setGeometry(0, 0, 1280,720)
        self.setWindowTitle("Adrian's & Adrian's LTDA.")
        self.setStyleSheet("QMainWindow {background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop: 0 #000540, stop: 1 #1bdeb4); }")
        self.show()

    def createButtons(self):
        self.createOne.label(self, "Eletronic Paradise", 950, 10, 320, 50,'QLabel {background-color:#000540; border-radius: 16px; font:bold; font-size:30px; color: white; padding: 0 0 0 15px}')
        viewProductDetails = self.createOne.button(self, "Ver as especificações", 415, 22, 170, 30, 'QPushButton {background-color:#000540; border-radius: 15; font:bold; font-size:14px; color: white}')
        addToCart = self.createOne.button(self, "Adicionar ao carrinho", 600, 22, 160, 30, 'QPushButton {background-color:#000540; border-radius: 15; font:bold; font-size:14; color: white}')
        removeFromCart = self.createOne.button(self, "Remover do carrinho", 780, 22, 160, 30, 'QPushButton {background-color:#000540; border-radius: 15; font:bold; font-size:14; color: white}')
        self.createOne.label(self, "Seja bem vindo!", 10, 5, 400, 80,"QLabel {font: bold; font-size: 45px; color: black;  padding: 10px}")
        
        viewProductDetails.clicked.connect(self.onViewProductDetailsClicked)
        removeFromCart.clicked.connect(self.createAllToRemove)
        addToCart.clicked.connect(self.createAllToAdd)

    def createAllToAdd(self):  
        pc = self.createOne.itemToAdd        (self,  10, 100, "imagens/Medias/pc_m.jpg",          "Supremacy Ultra: o ápice da tecnologia encapsulada em um computador excepcionalmente poderoso e esteticamente impressionante.")
        teclado = self.createOne.itemToAdd   (self, 330, 100, "imagens/Medias/teclado_m.jpg",     "ultra type: teclado mecânico com uma experiência de digitação excepcional! Combina durabilidade, precisão e conforto em um design elegante e excêntrico.")
        monitor = self.createOne.itemToAdd   (self, 650, 100, "imagens/Medias/monitor_m.jpg",     "VisionXtreme: Com resolução Ultra HD 4K, taxa de atualização de 144Hz e tecnologia HDR, oferece imagens nítidas e vibrantes para uma experiência visual imersiva.")
        mouse = self.createOne.itemToAdd     (self, 970, 100, "imagens/Medias/mouse_m.jpg",       "PhantomGrip: o Mouse Gamer de Elite Projetado para proporcionar precisão, velocidade e conforto como nenhum outro.")
        processador= self.createOne.itemToAdd(self,  10, 240, "imagens/Medias/processador_m.jpg", "HyperCore: Perfeito para Desempenho Computacional! Equipado com tecnologia de ponta, tem potência para lidar com as tarefas mais exigentes")
        ssd = self.createOne.itemToAdd       (self, 330, 240, "imagens/Medias/ssd_m.jpg",         "TurboDrive: o SSD de Elite completo! Com capacidades de armazenamento e velocidades de leitura/gravação ultra-rápidas e alta confiabilidade")
        cooler = self.createOne.itemToAdd    (self, 650, 240, "imagens/Medias/cooler_m.jpg",      "FrostBlast: o Cooler perfeito para seu Desempenho de Refrigeração! Oferece resfriamento excepcional e silencio para seu sistema.")
        placaVideo = self.createOne.itemToAdd(self, 970, 240, "imagens/Medias/placaVideo_m.jpg",  "TurBoost 9000X tem uma potência de processamento gráfico projetada para elevar sua experiência a novos patamares. Com velocidade, eficiência e potência líderes de mercado") 
        mousepad = self.createOne.itemToAdd  (self,  10, 380, "imagens/Medias/mousepad_m.jpg",    "HyperGlide Pro: o Mousepad de Elite para sua Precisão e Conforto de Movimento!") 
        fone = self.createOne.itemToAdd      (self, 330, 380, "imagens/Medias/fone_m.jpg",        "SonicBlast 8000X: projetados para proporcionar áudio imersivo e de alta qualidade. Com drivers de última geração e tecnologia de cancelamento de ruído ativo.") 
        ram = self.createOne.itemToAdd       (self, 650, 380, "imagens/Medias/ram_m.jpg",           "RAM Triforce: uma solução poderosa que oferece não uma, mas três memórias RAM de alta velocidade, Com capacidade total de 24GB (3x8GB)") 
        gabinete = self.createOne.itemToAdd  (self, 970, 380, "imagens/Medias/gabinete_m.jpg",      "Gamer Turbo X, uma escolha para os entusiastas de PC que buscam o máximo em desempenho e estilo. Com iluminação RGB personalizável e amplo espaço interno") 

        pc.clicked.connect         (lambda: self.onAddToCartClicked('pc'))
        teclado.clicked.connect    (lambda: self.onAddToCartClicked('teclado'))
        monitor.clicked.connect    (lambda: self.onAddToCartClicked('monitor'))
        mouse.clicked.connect      (lambda: self.onAddToCartClicked('mouse'))       
        mousepad.clicked.connect   (lambda: self.onAddToCartClicked('mousepad'))
        processador.clicked.connect(lambda: self.onAddToCartClicked('processador'))
        ssd.clicked.connect        (lambda: self.onAddToCartClicked('ssd'))
        cooler.clicked.connect     (lambda: self.onAddToCartClicked('cooler'))
        placaVideo.clicked.connect (lambda: self.onAddToCartClicked('placaVideo'))
        fone.clicked.connect       (lambda: self.onAddToCartClicked('fone'))
        ram.clicked.connect        (lambda: self.onAddToCartClicked('ram'))
        gabinete.clicked.connect   (lambda: self.onAddToCartClicked('gabinete'))

    def createAllToRemove(self):
        pc_remove =          self.createOne.button(self, "-",  100, 190, 25, 25, 'QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}')
        teclado_remove =     self.createOne.button(self, "-",  420, 190, 25, 25, 'QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}')
        monitor_remove =     self.createOne.button(self, "-",  740, 190, 25, 25, 'QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}')
        mouse_remove =       self.createOne.button(self, "-", 1060, 190, 25, 25, 'QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}')
        processador_remove = self.createOne.button(self, "-",  100, 330, 25, 25, 'QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}')
        ssd_remove =         self.createOne.button(self, "-",  420, 330, 25, 25, 'QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}')
        cooler_remove =      self.createOne.button(self, "-",  740, 330, 25, 25, 'QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}')
        placaVideo_remove =  self.createOne.button(self, "-", 1060, 330, 25, 25, 'QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}')
        mousepad_remove =    self.createOne.button(self, "-",  100, 470, 25, 25, 'QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}')
        fone_remove =        self.createOne.button(self, "-",  420, 470, 25, 25, 'QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}')
        ram_remove =         self.createOne.button(self, "-",  740, 470, 25, 25, 'QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}')
        gabinete_remove =    self.createOne.button(self, "-", 1060, 470, 25, 25, 'QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}')

        pc_remove.clicked.connect         (lambda: self.onRemoveItemClicked('pc'))
        teclado_remove.clicked.connect    (lambda: self.onRemoveItemClicked('teclado'))
        monitor_remove.clicked.connect    (lambda: self.onRemoveItemClicked('monitor'))
        mouse_remove.clicked.connect      (lambda: self.onRemoveItemClicked('mouse'))       
        processador_remove.clicked.connect(lambda: self.onRemoveItemClicked('processador'))
        ssd_remove.clicked.connect        (lambda: self.onRemoveItemClicked('ssd'))
        cooler_remove.clicked.connect     (lambda: self.onRemoveItemClicked('cooler'))
        placaVideo_remove.clicked.connect (lambda: self.onRemoveItemClicked('placaVideo'))
        mousepad_remove.clicked.connect   (lambda: self.onRemoveItemClicked('mousepad'))
        fone_remove.clicked.connect       (lambda: self.onRemoveItemClicked('fone'))
        ram_remove.clicked.connect        (lambda: self.onRemoveItemClicked('ram'))
        gabinete_remove.clicked.connect   (lambda: self.onRemoveItemClicked('gabinete'))

    def onViewProductDetailsClicked(self):
        print("Botão 'Ver as especificações' clicado.") 

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
    
    def onRemoveItemClicked(self, product):
        if(product in self.all):
            self.clearCartDisplay()
            self.all.remove(product)
            for item in self.all:
                self.AddToCart(item)

        if(len(self.all) == 0 ):
            self.createOne.label(self, " ", 10, 505, 1260, 200, "QLabel {font: bold; font-size: 45px; background: white; border-radius: 25px; padding: 10px}")
            self.labels["total"] = self.createOne.newTotal(self, self.price, self.quantity)
            self.createAllToAdd()

    def clearCartDisplay(self):
        self.leftDistance = -140
        self.topDistance = 500
        self.labels = {}
        self.quantity = {}
        self.position = {}
    
    def onFinalizePurchaseClicked(self, produto):
        print("A")
    
    def isInDict(self, produto, dict):
        for key in dict.keys():
            if(produto == key):
               return True
        return False
