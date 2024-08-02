from CreateOne import *
class CreateMany:
    def firstScreen(parent):  
        parent.createOne.item        (parent,  10, 100, "imagens/Medias/pc_m.jpg",          "Supremacy Ultra: o ápice da tecnologia encapsulada em um computador excepcionalmente poderoso e esteticamente impressionante.")
        parent.createOne.item   (parent, 330, 100, "imagens/Medias/teclado_m.jpg",     "ultra type: teclado mecânico com uma experiência de digitação excepcional! Combina durabilidade, precisão e conforto em um design elegante e excêntrico.")
        parent.createOne.item   (parent, 650, 100, "imagens/Medias/monitor_m.jpg",     "VisionXtreme: Com resolução Ultra HD 4K, taxa de atualização de 144Hz e tecnologia HDR, oferece imagens nítidas e vibrantes para uma experiência visual imersiva.")
        parent.createOne.item     (parent, 970, 100, "imagens/Medias/mouse_m.jpg",       "PhantomGrip: o Mouse Gamer de Elite Projetado para proporcionar precisão, velocidade e conforto como nenhum outro.")
        parent.createOne.item(parent,  10, 240, "imagens/Medias/processador_m.jpg", "HyperCore: Perfeito para Desempenho Computacional! Equipado com tecnologia de ponta, tem potência para lidar com as tarefas mais exigentes")
        parent.createOne.item       (parent, 330, 240, "imagens/Medias/ssd_m.jpg",         "TurboDrive: o SSD de Elite completo! Com capacidades de armazenamento e velocidades de leitura/gravação ultra-rápidas e alta confiabilidade")
        parent.createOne.item    (parent, 650, 240, "imagens/Medias/cooler_m.jpg",      "FrostBlast: o Cooler perfeito para seu Desempenho de Refrigeração! Oferece resfriamento excepcional e silencio para seu sistema.")
        parent.createOne.item(parent, 970, 240, "imagens/Medias/placaVideo_m.jpg",  "TurBoost 9000X tem uma potência de processamento gráfico projetada para elevar sua experiência a novos patamares. Com velocidade, eficiência e potência líderes de mercado") 
        parent.createOne.item  (parent,  10, 380, "imagens/Medias/mousepad_m.jpg",    "HyperGlide Pro: o Mousepad de Elite para sua Precisão e Conforto de Movimento!") 
        parent.createOne.item      (parent, 330, 380, "imagens/Medias/fone_m.jpg",        "SonicBlast 8000X: projetados para proporcionar áudio imersivo e de alta qualidade. Com drivers de última geração e tecnologia de cancelamento de ruído ativo.") 
        parent.createOne.item       (parent, 650, 380, "imagens/Medias/ram_m.jpg",           "RAM Triforce: uma solução poderosa que oferece não uma, mas três memórias RAM de alta velocidade, Com capacidade total de 24GB (3x8GB)") 
        parent.createOne.item  (parent, 970, 380, "imagens/Medias/gabinete_m.jpg",      "Gamer Turbo X, uma escolha para os entusiastas de PC que buscam o máximo em desempenho e estilo. Com iluminação RGB personalizável e amplo espaço interno") 


    def itemsToAdd(parent):
        pc_add =          parent.createOne.button(parent, '+',  100, 190, 25, 25, "QPushButton {background-color:#00CC00; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        teclado_add =     parent.createOne.button(parent, '+',  420, 190, 25, 25, "QPushButton {background-color:#00CC00; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        monitor_add =     parent.createOne.button(parent, '+',  740, 190, 25, 25, "QPushButton {background-color:#00CC00; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        mouse_add =       parent.createOne.button(parent, '+', 1060, 190, 25, 25, "QPushButton {background-color:#00CC00; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        processador_add = parent.createOne.button(parent, '+',  100, 330, 25, 25, "QPushButton {background-color:#00CC00; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        ssd_add =         parent.createOne.button(parent, '+',  420, 330, 25, 25, "QPushButton {background-color:#00CC00; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        cooler_add =      parent.createOne.button(parent, '+',  740, 330, 25, 25, "QPushButton {background-color:#00CC00; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        placaVideo_add =  parent.createOne.button(parent, '+', 1060, 330, 25, 25, "QPushButton {background-color:#00CC00; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        mousepad_add =    parent.createOne.button(parent, '+',  100, 470, 25, 25, "QPushButton {background-color:#00CC00; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        fone_add =        parent.createOne.button(parent, '+',  420, 470, 25, 25, "QPushButton {background-color:#00CC00; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        ram_add =         parent.createOne.button(parent, '+',  740, 470, 25, 25, "QPushButton {background-color:#00CC00; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        gabinete_add =    parent.createOne.button(parent, '+', 1060, 470, 25, 25, "QPushButton {background-color:#00CC00; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        
        pc_add.clicked.connect         (lambda: parent.onAddToCartClicked("pc"))
        teclado_add.clicked.connect    (lambda: parent.onAddToCartClicked("teclado"))
        monitor_add.clicked.connect    (lambda: parent.onAddToCartClicked("monitor"))
        mouse_add.clicked.connect      (lambda: parent.onAddToCartClicked("mouse"))       
        mousepad_add.clicked.connect   (lambda: parent.onAddToCartClicked("mousepad"))
        processador_add.clicked.connect(lambda: parent.onAddToCartClicked("processador"))
        ssd_add.clicked.connect        (lambda: parent.onAddToCartClicked("ssd"))
        cooler_add.clicked.connect     (lambda: parent.onAddToCartClicked("cooler"))
        placaVideo_add.clicked.connect (lambda: parent.onAddToCartClicked("placaVideo"))
        fone_add.clicked.connect       (lambda: parent.onAddToCartClicked("fone"))
        ram_add.clicked.connect        (lambda: parent.onAddToCartClicked("ram"))
        gabinete_add.clicked.connect   (lambda: parent.onAddToCartClicked("gabinete"))


    def itemsToRemove(parent):
        pc_remove =          parent.createOne.button(parent, '-',  100, 190, 25, 25, "QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        teclado_remove =     parent.createOne.button(parent, '-',  420, 190, 25, 25, "QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        monitor_remove =     parent.createOne.button(parent, '-',  740, 190, 25, 25, "QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        mouse_remove =       parent.createOne.button(parent, '-', 1060, 190, 25, 25, "QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        processador_remove = parent.createOne.button(parent, '-',  100, 330, 25, 25, "QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        ssd_remove =         parent.createOne.button(parent, '-',  420, 330, 25, 25, "QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        cooler_remove =      parent.createOne.button(parent, '-',  740, 330, 25, 25, "QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        placaVideo_remove =  parent.createOne.button(parent, '-', 1060, 330, 25, 25, "QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        mousepad_remove =    parent.createOne.button(parent, '-',  100, 470, 25, 25, "QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        fone_remove =        parent.createOne.button(parent, '-',  420, 470, 25, 25, "QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        ram_remove =         parent.createOne.button(parent, '-',  740, 470, 25, 25, "QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")
        gabinete_remove =    parent.createOne.button(parent, '-', 1060, 470, 25, 25, "QPushButton {background-color:#D40000; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 5px 0}")

        pc_remove.clicked.connect         (lambda: parent.removeFromCart("pc"))
        teclado_remove.clicked.connect    (lambda: parent.removeFromCart("teclado"))
        monitor_remove.clicked.connect    (lambda: parent.removeFromCart("monitor"))
        mouse_remove.clicked.connect      (lambda: parent.removeFromCart("mouse"))       
        processador_remove.clicked.connect(lambda: parent.removeFromCart("processador"))
        ssd_remove.clicked.connect        (lambda: parent.removeFromCart("ssd"))
        cooler_remove.clicked.connect     (lambda: parent.removeFromCart("cooler"))
        placaVideo_remove.clicked.connect (lambda: parent.removeFromCart("placaVideo"))
        mousepad_remove.clicked.connect   (lambda: parent.removeFromCart("mousepad"))
        fone_remove.clicked.connect       (lambda: parent.removeFromCart("fone"))
        ram_remove.clicked.connect        (lambda: parent.removeFromCart("ram"))
        gabinete_remove.clicked.connect   (lambda: parent.removeFromCart("gabinete"))


    def itemDetails(parent):
        pc_details =          parent.createOne.button(parent, '?',  100, 190, 25, 25, "QPushButton {background-color:#FFFFFF; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 0 2px}")
        teclado_details =     parent.createOne.button(parent, '?',  420, 190, 25, 25, "QPushButton {background-color:#FFFFFF; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 0 2px}")
        monitor_details =     parent.createOne.button(parent, '?',  740, 190, 25, 25, "QPushButton {background-color:#FFFFFF; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 0 2px}")
        mouse_details =       parent.createOne.button(parent, '?', 1060, 190, 25, 25, "QPushButton {background-color:#FFFFFF; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 0 2px}")
        processador_details = parent.createOne.button(parent, '?',  100, 330, 25, 25, "QPushButton {background-color:#FFFFFF; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 0 2px}")
        ssd_details =         parent.createOne.button(parent, '?',  420, 330, 25, 25, "QPushButton {background-color:#FFFFFF; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 0 2px}")
        cooler_details =      parent.createOne.button(parent, '?',  740, 330, 25, 25, "QPushButton {background-color:#FFFFFF; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 0 2px}")
        placaVideo_details =  parent.createOne.button(parent, '?', 1060, 330, 25, 25, "QPushButton {background-color:#FFFFFF; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 0 2px}")
        mousepad_details =    parent.createOne.button(parent, '?',  100, 470, 25, 25, "QPushButton {background-color:#FFFFFF; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 0 2px}")
        fone_details =        parent.createOne.button(parent, '?',  420, 470, 25, 25, "QPushButton {background-color:#FFFFFF; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 0 2px}")
        ram_details =         parent.createOne.button(parent, '?',  740, 470, 25, 25, "QPushButton {background-color:#FFFFFF; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 0 2px}")
        gabinete_details =    parent.createOne.button(parent, '?', 1060, 470, 25, 25, "QPushButton {background-color:#FFFFFF; color: black; font:bold; font-size:24px; border-radius:12px; padding: 0 0 0 2px}")

        pc_details.clicked.connect         (lambda: parent.productDetails("pc", "",
                                                                          ""))
        
        teclado_details.clicked.connect    (lambda: parent.productDetails("teclado", "O Ultra Type é um teclado mecânico que redefine o padrão da digitação, oferecendo uma experiência excepcional que combina durabilidade, precisão e conforto.\n\nEquipado com switches mecânicos de alta qualidade, o Ultra Type proporciona uma resposta tátil e auditiva única a cada pressionar de tecla, resultando em uma velocidade de digitação incomparável.\n\nSeu design ergonômico foi meticulosamente desenvolvido para reduzir a fadiga durante longas sessões de uso, com teclas ligeiramente côncavas que se adaptam perfeitamente aos seus dedos, garantindo uma postura natural e confortável.\n\nAlém disso, o Ultra Type conta com um sistema de iluminação RGB personalizável, permitindo que você ajuste as cores e os efeitos de iluminação conforme o seu gosto, criando um ambiente de trabalho ou jogo imersivo e estiloso.",
                                                                          "A aparência do Ultra Type é uma combinação de elegância e excentricidade.\n\nSua estrutura robusta de alumínio escovado confere ao teclado uma durabilidade impressionante, enquanto seu layout compacto e moderno economiza espaço na sua mesa sem comprometer a funcionalidade.\n\nCom conectividade versátil, o Ultra Type pode ser utilizado tanto via cabo USB quanto via conexão sem fio Bluetooth, oferecendo a flexibilidade que você precisa para trabalhar ou jogar em qualquer lugar.\n\nAdicionalmente, o teclado é compatível com diversas plataformas, incluindo Windows, macOS, e dispositivos móveis, tornando-o uma escolha ideal para qualquer usuário que busca eficiência e estilo.\n\nEm resumo, o Ultra Type é o teclado definitivo para quem valoriza uma experiência de digitação superior, combinando desempenho excepcional com um design arrojado e funcional."))
        
        monitor_details.clicked.connect    (lambda: parent.productDetails("monitor", "O VisionXtreme é um monitor que eleva a experiência visual a um novo patamar, combinando resolução Ultra HD 4K com uma taxa de atualização de 144Hz e tecnologia HDR.\n\nCom 3840 x 2160 pixels, o VisionXtreme oferece uma clareza impressionante, revelando os mínimos detalhes com uma nitidez inigualável. A alta taxa de atualização de 144Hz garante uma fluidez excepcional nas cenas de ação, eliminando borrões e garantindo que até os movimentos mais rápidos sejam exibidos com precisão.\n\nA tecnologia HDR (High Dynamic Range) aprimora ainda mais a qualidade das imagens, proporcionando cores mais vibrantes e um contraste mais profundo, resultando em uma experiência visual que é ao mesmo tempo realista e envolvente.",
                                                                          "O design do VisionXtreme é uma obra de arte em si: com uma moldura ultrafina, o monitor maximiza a área de visualização, oferecendo uma aparência elegante e moderna que se encaixa perfeitamente em qualquer ambiente, seja no escritório ou em casa.\n\nAlém disso, o VisionXtreme possui diversas opções de conectividade, incluindo portas HDMI, DisplayPort e USB-C, garantindo compatibilidade com uma ampla gama de dispositivos.\n\nO suporte ajustável permite que você encontre a posição de visualização perfeita, enquanto o modo de baixa luz azul e a tecnologia anti-flicker ajudam a reduzir a fadiga ocular durante longas sessões de uso.\n\nEm suma, o VisionXtreme é o monitor ideal para quem busca uma experiência visual imersiva, combinando desempenho de ponta com um design sofisticado e funcionalidades versáteis."))
       
        mouse_details.clicked.connect      (lambda: parent.productDetails("mouse", "",
                                                                          ""))  
             
        processador_details.clicked.connect(lambda: parent.productDetails("processador", "",
                                                                          ""))

        ssd_details.clicked.connect        (lambda: parent.productDetails("ssd", "O TurboDrive é o SSD de elite que redefine o conceito de armazenamento de dados, oferecendo capacidades impressionantes e velocidades de leitura/gravação ultra-rápidas.\n\nProjetado para proporcionar um desempenho superior, o TurboDrive utiliza a mais avançada tecnologia de memória flash NAND, garantindo transferências de dados em velocidades que transformam a maneira como você interage com seus arquivos.\n\nCom velocidades de leitura que podem alcançar até 3500 MB/s e gravações de até 3000 MB/s, o TurboDrive permite que você inicie o sistema operacional, carregue aplicativos e transfira arquivos grandes em uma fração do tempo comparado aos discos rígidos tradicionais.",
                                                                          "Além de sua velocidade incrível, o TurboDrive se destaca pela alta confiabilidade e durabilidade, tornando-o ideal para uso intensivo e prolongado.\n\nCom capacidades de armazenamento que variam de 256 GB a 2 TB, este SSD oferece opções flexíveis para atender às suas necessidades específicas, seja para armazenar uma vasta biblioteca de jogos, projetos de trabalho complexos ou coleções multimídia.\n\nO TurboDrive também incorpora tecnologias avançadas de correção de erros e gerenciamento de desgaste, garantindo a integridade dos dados e uma vida útil prolongada do dispositivo.\n\nEm resumo, o TurboDrive é o SSD definitivo para quem busca uma combinação de desempenho ultrarrápido, alta capacidade de armazenamento e confiabilidade incomparável, transformando sua experiência computacional em todos os aspectos."))

        cooler_details.clicked.connect     (lambda: parent.productDetails("cooler", "O FrostBlast é o cooler definitivo para quem busca um desempenho de refrigeração excepcional aliado ao silêncio absoluto.\n\nProjetado com tecnologia de ponta, o FrostBlast garante que seu sistema se mantenha em temperaturas ideais mesmo sob as cargas de trabalho mais intensas.\n\nEquipado com uma combinação de heatpipes de cobre e aletas de alumínio, este cooler maximiza a dissipação de calor, proporcionando um resfriamento eficiente e consistente.\n\nO ventilador de alta performance, com rolamentos fluidodinâmicos, opera de maneira incrivelmente silenciosa, permitindo que você se concentre em suas tarefas sem o incômodo de ruídos excessivos.",
                                                                          "Além de sua eficiência térmica e operação silenciosa, o FrostBlast apresenta um design moderno e elegante, que complementa qualquer configuração de PC.\n\nCom LEDs RGB personalizáveis, você pode ajustar a iluminação para sincronizar com o restante do seu hardware, criando uma estética visualmente fantástica.\n\nA instalação é simplificada graças ao sistema de montagem universal, compatível com uma ampla gama de sockets de CPU, tanto Intel quanto AMD.\n\nEm suma, o FrostBlast é a escolha perfeita para quem busca um cooler que combine resfriamento excepcional, operação silenciosa e um design atraente, garantindo que seu sistema funcione com desempenho máximo e estilo inigualável."))

        placaVideo_details.clicked.connect (lambda: parent.productDetails("placaVideo", "A TurBoost 9000X é a placa de vídeo que eleva sua experiência gráfica a novos patamares, combinando velocidade, eficiência e potência líderes de mercado.\n\nCom uma arquitetura avançada e uma quantidade impressionante de núcleos CUDA, a TurBoost 9000X oferece um desempenho gráfico incomparável, permitindo que você desfrute dos jogos mais recentes em configurações máximas, com taxas de quadros ultrassuaves e uma qualidade visual de tirar o fôlego.\n\nO suporte a Ray Tracing em tempo real e a tecnologia DLSS (Deep Learning Super Sampling) da NVIDIA garantem gráficos hiper-realistas e uma eficiência superior, proporcionando uma imersão total em seus jogos e aplicações de realidade virtual.",
                                                                          "Além de seu poder de processamento gráfico bruto, a TurBoost 9000X destaca-se pela sua eficiência energética e pelo design térmico inovador.\n\nCom um sistema de refrigeração triplo e ventiladores de alta performance, a placa mantém temperaturas baixas mesmo nas sessões de uso mais intensas, garantindo um funcionamento estável e duradouro.\n\nO design elegante, com iluminação RGB personalizável, permite que você adapte a aparência da placa ao restante do seu setup, criando uma estética coesa e impressionante.\n\nA TurBoost 9000X também oferece uma conectividade robusta, com múltiplas saídas HDMI e DisplayPort, além de suporte a monitores 4K e 8K, tornando-a ideal para profissionais de edição de vídeo, designers gráficos e gamers exigentes.\n\nEm resumo, a TurBoost 9000X é a placa de vídeo definitiva para quem busca o melhor em desempenho gráfico, eficiência e estilo, transformando cada sessão de uso em uma experiência extraordinária."))

        mousepad_details.clicked.connect   (lambda: parent.productDetails("mousepad", "",
                                                                          ""))

        fone_details.clicked.connect       (lambda: parent.productDetails("fone", "",
                                                                          ""))

        ram_details.clicked.connect        (lambda: parent.productDetails("ram", "",
                                                                          ""))

        gabinete_details.clicked.connect   (lambda: parent.productDetails("gabinete", "",
                                                                          ""))