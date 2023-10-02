import pygame
import os,sys
pygame.init()
click=False
largura,altura=900,600
state="inicio"
tela=pygame.display.set_mode((largura,altura))
fundo=pygame.image.load(os.path.join("assets","cor.png"))
cor=pygame.image.load(os.path.join("assets","botão.png"))
correc=cor.get_rect(center=(200,200))
escrito=pygame.image.load(os.path.join("assets","escrito.png"))
escrrec=escrito.get_rect(center=(450,500))
color=(255,255,255)
rectt=pygame.Rect(150,100,600,200)
gamestate=""
font=pygame.font.Font(os.path.join("assets","Sigmar-Regular.ttf"))
escrita=font.render("next",True,(0,0,0))
texrec=escrita.get_rect(center=(450,500))

pygame.mixer.music.load("assets/Duda.mp3")

pygame.mouse.set_visible(False)

mouse=""                     
loop= True
while loop:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             loop = False
             sys.exit()
    
        if event.type== pygame.MOUSEBUTTONDOWN:
            if correc.colliderect(escrrec):
                if state=="inicio":
                    state='next1'
                elif state=="next1":
                    state="next2"  
                elif state=='next2':
                    state='next3'
                elif state=="next3":
                    state="next4"
                elif state=='next4':
                    state='next5'
                elif state=='next5':
                    state='next6'
                    pygame.mixer.music.play()
    
    pos = pygame.mouse.get_pos()
    correc.center=(pos)
    
    if state == "inicio":
        texto="""
    Olá meu amor, nesse joguinho você ira receber uma caixa com um cadeado, esse cadeado tem uma senha, 
    a senha será dada com dicas, cada parte desse game tem uma dica de onde procurar as senhas, teremos também fazes bônus com alguns 
    brindes, boa sorte, te amo!!
        """
    elif state=="next1":
        texto="""
    agora já com a caixa em mãos, vamos a primeira dica: 
    no local onde as comidas são feitas, enquanto mais frio, mais próximo está da dica 
        """
    elif state=="next2":
        texto="""
    parabéns você encontrou a primeira pista, vamos para mais uma: 
    onde de manhã o galo canta, e meu sono dança, na parte ao lado no teto onde não alcança
    """
    elif state=="next3":
        texto="""
ótimo vamos a terceira pista, essa será uma fase bônus então fique atenta: 
onde na construção algo se levanta, na parte alta uma surpresa se encontra
"""
    elif state=="next4":
        texto="""
parabéns meu amor espero que tenha gostado do presente, vamos a mais uma fase bônus? vamos lá então: 
onde há camas mas ninguém dorme, mais uma surpresa ocorre
"""
    elif state=="next5":
        texto="""
esse eu escolhi direitinho né? desculpa a brincadeira da capinha com nossa foto,
acho que essa você vai usar né ? 
vamos a ultima dica da caixinha: 
onde a agua cai do teto, uma pista final vai  deixar seu presente aberto
"""
    linhas = []
    palavras = texto.split()
    linha_atual = ""

    for palavra in palavras:
        teste_linha = linha_atual + " " + palavra if linha_atual else palavra
        largura_linha, altura_linha = font.size(teste_linha)
        if largura_linha <= largura - 350:  # 40 pixels de margem
            linha_atual = teste_linha
        else:
            linhas.append(linha_atual)
            linha_atual = palavra
    linhas.append(linha_atual)
                




    y=150


    tela.blit(fundo,(0,0))
    if state=="next6":
        pass
    else:
        tela.blit(escrito,escrrec)
        tela.blit(escrita,texrec)
        pygame.draw.rect(tela,color,rectt)
   
        for linha in linhas:
            texto_surface = font.render(linha, True, (0,0,0))
            tela.blit(texto_surface, (170, y))
            y+=20
    tela.blit(cor,correc)  
            
    
    pygame.display.update()
pygame.quit()