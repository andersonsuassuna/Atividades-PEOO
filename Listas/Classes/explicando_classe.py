import psycopg2
import os
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import ctypes
import threading as th

#banco de dados

def criar_matrix():
    #----------------Abrindo o banco de dados------------------------
    conexao = psycopg2.connect(
        host='localhost',
        dbname='LIeC_AnthillLib',
        user='postgres',
        password='158575',
        port='5432')
    comandos = conexao.cursor() 
    #----------------criando a matriz a partir do banco----------------
    matrix = []
    titulada = []
    tem = False
    comandos.execute('''select titulo, autor, ano, aluguel from biblioteca
                    order by titulo asc''')
    for titulo,autor,data,aluguel in comandos.fetchall():
        tem = False
        for i in titulada:
            if i == titulo:
                tem = True
        if tem == True:
            continue
        else:
            titulada.append(titulo)
            matrix.append([titulo, autor, data, aluguel])
    #-------------------Fechando banco de dados--------------------------
    conexao.close()    
    return matrix

def adicionar_livros(matriz,livro_novo):
    matriz.append(livro_novo)
    return matriz

def remover_livros(matriz,linha_removida):
    matriz.pop(linha_removida)
    return matriz

def listar_autor(matriz):
    lista_autor=[]
    for a,nome_autor,b,c in matriz:
        tem = False
        for i in range(len(lista_autor)):
            if lista_autor[i][0].lower() == nome_autor.lower():
                lista_autor[i][1] +=1
        
        for j in lista_autor:
                if j[0] == nome_autor:
                    tem = True
        if not tem:
            lista_autor.append([nome_autor,1])
    return lista_autor

def buscar_livros(matriz, digitado):
    for i in matriz:
        if i[0].lower() == digitado.lower():
            return True
    return False

def buscar_direito(matriz,parametro=0, busca=None):
    nova_matriz = []
    for i in matriz:
        try:
            if busca.lower() in i[parametro].lower():
                nova_matriz.append(i)
        except:
            if busca in str(i[parametro]):
                nova_matriz.append(i)
    if len(nova_matriz) == 0:
        return False
    return ordem_tituloabc(nova_matriz, parametro)

def ordem_tituloabc(matriz, parametro=0,padrao=False):
    lista_titulo = []
    nova_matriz = []
    posicao = 0
    if parametro == 2 and padrao == True:
        padrao = False
    elif parametro == 2 and padrao == False:
        padrao = True
    for i in matriz:
        lista_titulo.append(i[parametro])
    lista_ordenada = sorted(lista_titulo,reverse=padrao)
    while len(nova_matriz) < len(matriz):
        for j in matriz:
            if j[parametro] == lista_ordenada[posicao]:
                nova_matriz.append(j)
                if posicao < len(lista_ordenada)-1:
                    posicao +=1
                else:
                    break
    return nova_matriz
    
def print_bonito(matriz):
    for i in matriz:
        print(i)

def recriar_matriz(matriz):
    conexao = psycopg2.connect(
        host='localhost',
        dbname='LIeC_AnthillLib',
        user='postgres',
        password='158575',
        port='5432')
    comandos = conexao.cursor()
    for i in matriz:
        comandos.execute(f'''INSERT INTO biblioteca(titulo, autor, ano, aluguel)
                        VALUES('{i[0]}', '{i[1]}', '{i[2]}', '{i[3]}' )''')
    conexao.commit()
    conexao.close
def deletar_banco():
    conexao = psycopg2.connect(
        host='localhost',
        dbname='LIeC_AnthillLib',
        user='postgres',
        password='158575',
        port='5432')
    comandos = conexao.cursor()
    comandos.execute('''update biblioteca
                    set id = default''')
    conexao.commit()
    comandos.execute('''delete from biblioteca''')
    conexao.commit()
    conexao.close()

def sair(matriz):
    recriar_matriz(matriz)
    os._exit(1)

def restaurar_banco():
    conexao = psycopg2.connect(
        host='localhost',
        dbname='LIeC_AnthillLib',
        user='postgres',
        password='158575',
        port='5432')
    comandos = conexao.cursor() 
    #----------------criando a matriz a partir do banco----------------
    matrix = []
    titulada = []
    tem = False
    comandos.execute('''select titulo, autor, ano, aluguel from biblio_backup
                    order by titulo asc''')
    for titulo,autor,data,aluguel in comandos.fetchall():
        tem = False
        for i in titulada:
            if i == titulo:
                tem = True
        if tem == True:
            continue
        else:
            titulada.append(titulo)
            matrix.append([titulo, autor, data, aluguel])
    recriar_matriz(matrix)
    #-------------------Fechando banco de dados--------------------------
    
    conexao.close()    
def editar_livro(matriz, livro, linha):
    matriz[linha] = livro

matriz_principal = criar_matrix()
matriz = matriz_principal





#?-----------------------------------------------------FRONT------------------------------------------------------
class Tela():
    def __init__(self):
        ctk.set_appearance_mode('dark')  
        
        self.contador, self.contador2, self.pagina_atual, self.tamanho_pagina, self.lista_autor, self.linha = 0, True, 0, 16, listar_autor(matriz_principal), None
        self.tamanho, self.X, self.Y = ('720x480'), 720, 480  # definindo tamanho
        self.janela = ctk.CTk()  # transformando o objeto janela num objeto ctk
        self.janela.geometry(self.tamanho)  # utilizando o tamanho definido
        self.janela.resizable(False, False)
        self.janela.title('Anthill Library')
    
        app_id = 'meu.aplicativo.id'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

        # Fontes e Imagens
        ctk.FontManager.load_font(font_path='bibliotecaIf/WINGDNG3.ttf')
        self.fonteceta = ctk.CTkFont(family='Wingdings 3', size=24, weight='bold')
        ctk.FontManager.load_font(font_path='AnnyantRoman.ttf')
        self.fonte = ctk.CTkFont(family='AnnyantRoman', size=60)
        self.fonte2 = ctk.CTkFont(family='AnnyantRoman', size=10)
        self.logo = ImageTk.PhotoImage(Image.open('bibliotecaIf/images/logo250.png'))
        self.logo_menor = ImageTk.PhotoImage(Image.open('bibliotecaIf/images/logo2.png'))
        self.lupinha = ImageTk.PhotoImage(Image.open('bibliotecaIf/images/lupamassa.png'))
        
        self.livroaz,self.livroza = ImageTk.PhotoImage(Image.open('bibliotecaIf/images/livro_az_20x20.png')),ImageTk.PhotoImage(Image.open('bibliotecaIf/images/livro_za_20x20.png'))
        self.autoraz, self.autorza = ImageTk.PhotoImage(Image.open('bibliotecaIf/images/autor_az_20x20.png')),ImageTk.PhotoImage(Image.open('bibliotecaIf/images/autor_za_20x20.png'))
        self.datadesc,self.datacresc = ImageTk.PhotoImage(Image.open('bibliotecaIf/images/datadesc.png')),ImageTk.PhotoImage(Image.open('bibliotecaIf/images/datacresc.png'))
        self.b_livroaz,self.b_livroza = ImageTk.PhotoImage(Image.open('bibliotecaIf/images/livroAZ.png')),ImageTk.PhotoImage(Image.open('bibliotecaIf/images/livroZA.png'))
        self.b_autoraz, self.b_autorza = ImageTk.PhotoImage(Image.open('bibliotecaIf/images/autorAZ.png')),ImageTk.PhotoImage(Image.open('bibliotecaIf/images/autorZA.png'))
        self.b_datadesc,self.b_datacresc = ImageTk.PhotoImage(Image.open('bibliotecaIf/images/data321_20x20.png')),ImageTk.PhotoImage(Image.open('bibliotecaIf/images/data123_20x20.png'))
        self.imagem_botordem=self.autoraz
        self.icone = 'bibliotecaIf/images/logo2.ico'

        self.janela.iconbitmap(self.icone)
        self.janela.iconphoto(False, self.logo)

        self.frame_atual = None
        self.estilo = "mystyle.Treeview"
        self.style = ttk.Style()
        self.style.theme_use('alt')
        self.style.configure(self.estilo,
                            highlightthickness=0,
                            bd=0,
                            font=('Calibri', 11),
                            background='#242424',
                            foreground='#f0f0f0',
                            fieldbackground='#242424')
        self.style.configure(f"{self.estilo}.Heading",
                            font=('Calibri', 13, 'bold'),
                            background='#242424',  # Cor de fundo dos cabeçalhos
                            foreground='#f0f0f0')  # Cor do texto dos cabeçalhos
        self.style.layout(self.estilo,
                        [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
        self.trocar_telas(self.telainicio)

    def trocar_telas(self, definir_frame):
        if self.frame_atual is not None:
            self.frame_atual.destroy()
        self.frame_atual = ctk.CTkFrame(self.janela)
        self.frame_atual.pack(fill="both", expand=True)
        definir_frame()
        os.system("cls")

    def botao_ordem(self):
        self.frame_bot = ctk.CTkScrollableFrame(master=self.frame_atual, width=110, height=150,bg_color='#545454',fg_color='#545454')
        self.frame_bot.place(x=120, y=50)
        self.frame_bot.pack_propagate(False)

        self.bot_titulo = ctk.CTkButton(master=self.frame_bot, image=self.b_livroza, width=100, height=50, fg_color='#545454', hover_color='#545454', command=lambda: self.ordenar_titulo(0,self.livroza))
        self.bot_titulo.grid()
        self.bot_titulo2 = ctk.CTkButton(master=self.frame_bot, image=self.b_livroaz, width=100, height=50, fg_color='#545454', hover_color='#545454', command=lambda: self.ordenar_titulo(0,self.livroaz, True))
        self.bot_titulo2.grid()
        self.bot_autor = ctk.CTkButton(master=self.frame_bot, image=self.b_autoraz, width=100, height=50, fg_color='#545454', hover_color='#545454', command=lambda: self.ordenar_titulo(1,self.autoraz))
        self.bot_autor.grid()
        self.bot_autor2 = ctk.CTkButton(master=self.frame_bot, image=self.b_autorza, width=100, height=50, fg_color='#545454', hover_color='#545454', command=lambda: self.ordenar_titulo(1,self.autorza, True))
        self.bot_autor2.grid()
        self.bot_ano = ctk.CTkButton(master=self.frame_bot, image=self.datadesc, width=100, height=50, fg_color='#545454', hover_color='#545454', command=lambda: self.ordenar_titulo(2,self.b_datadesc))
        self.bot_ano.grid()
        self.bot_ano2 = ctk.CTkButton(master=self.frame_bot, image=self.datacresc, width=100, height=50, fg_color='#545454', hover_color='#545454', command=lambda: self.ordenar_titulo(2,self.b_datacresc, True))
        self.bot_ano2.grid()

    def mudar_titulo(self,nova_imagem):
        self.imagem_botordem=nova_imagem
    
    def ordenar_titulo(self, parametro,nova_imagem, ordem=False):
        
        if self.frame_planilha is not None:
            self.frame_planilha.destroy()
        self.frame_planilha = ctk.CTkFrame(self.frame_atual, width=525, height=350)
        self.frame_planilha.place(x=120, y=50)
        self.frame_planilha.pack_propagate(False)
        nova_ordem = ordem_tituloabc(matriz, parametro, ordem)
        self.planilha(nova_ordem,self.pagina_atual,self.tamanho_pagina)
        self.mudar_titulo(nova_imagem)

    def opcao_barra(self, evento):
        texto = evento
        self.pesq_titulo = ctk.CTkButton(master=self.frame_barra, text=f'Pesquisar "{texto}" por Titulo', font=('', 20), width=100, height=50, fg_color='#373434', hover_color='#575757', command=lambda: self.pesquisa(matriz, 0, texto))
        self.pesq_titulo.grid()
        self.pesq_autor = ctk.CTkButton(master=self.frame_barra, text=f'Pesquisar "{texto}" por Autor', width=100, font=('', 20), height=50, fg_color='#373434', hover_color='#575757', command=lambda: self.pesquisa(matriz, 1, texto))
        self.pesq_autor.grid()
        self.pesq_ano = ctk.CTkButton(master=self.frame_barra, text=f'Pesquisar "{texto}" Por ano', width=100, font=('', 20), height=50, fg_color='#373434', hover_color='#575757', command=lambda: self.pesquisa(matriz, 2, texto))
        self.pesq_ano.grid()

    def pesquisa(self, matriz_recebida, parametro, digitado):
        global matriz
        if buscar_direito(matriz_recebida, parametro, digitado):
            matriz = ordem_tituloabc(buscar_direito(matriz_recebida, parametro, digitado))
            self.trocar_telas(self.frame_pesquisa)
            self.planilha(matriz,self.pagina_atual,self.tamanho_pagina)
        else:
            pass
    
    def criar_destruir(self, event):
        texto = self.barra_pesquisa.get()
        if texto == '':
            if self.frame_barra is not None:
                self.frame_barra.destroy()
        else:
            if texto != '':
                self.frame_barra.destroy()
                self.frame_barra = ctk.CTkFrame(master=self.frame_atual)
                self.frame_barra.place(x=300, y=100)
                self.frame_barra.pack_propagate(False)
            self.opcao_barra(texto)

    def bot_alterar_titulo(self):
        self.frame_titulo = ctk.CTkFrame(self.frame_atual, width=40, height=40)
        self.frame_titulo.place(x=120, y=10)
        self.frame_titulo.pack_propagate(False)

        self.bot_titulo = ctk.CTkButton(master=self.frame_titulo, image=self.imagem_botordem, width=20, height=20,text=None,bg_color='#2b2b2b',hover_color='#2b2b2b' ,fg_color='#2b2b2b', command=lambda: self.botao_ordem())
        self.bot_titulo.place(x=1,y=0)

    def espera(self,caminho_tela):
        carrega=th.Thread(target=caminho_tela)
        carrega.start()

    def telainicio(self):
        global matriz
        global matriz_principal
        matriz = matriz_principal
        self.nome = ctk.CTkLabel(self.frame_atual, text='Anthill', font=self.fonte, text_color='#f0f0f0')
        self.nome.place(x=15, y=250)
        self.nome2 = ctk.CTkLabel(self.frame_atual, text='Library', font=self.fonte, text_color='#f0f0f0')
        self.nome2.place(x=100, y=310)

        self.barra_pesquisa = ctk.CTkEntry(self.frame_atual, width=400,height=40, placeholder_text='Buscar Livros', font=('AnnyantRoman', 20, 'bold'), text_color='white', fg_color='#242424', state='normal')
        self.barra_pesquisa.place(x=300, y=50)
        self.barra_pesquisa.bind("<KeyRelease>", self.criar_destruir)

        self.bot_listlivro = ctk.CTkButton(self.frame_atual, width=280,height=40, text='Exibir Biblioteca', font=('AnnyantRoman', 20, 'bold'), text_color='lightgray', fg_color='#1b1b1b', hover_color='#373434', command=lambda: self.trocar_telas(self.biblioteca))
        self.bot_listlivro.place(x=400, y=150)

        self.bot_addlivro = ctk.CTkButton(self.frame_atual, width=280,height=40, text='Registrar Livros', font=('AnnyantRoman', 20, 'bold'), text_color='lightgray', fg_color='#1b1b1b', hover_color='#373434', command=lambda: self.trocar_telas(self.registrar_livro))
        self.bot_addlivro.place(x=400, y=270)

        self.bot_listautor = ctk.CTkButton(self.frame_atual, width=280,height=40, text='Exibir Autores', font=('AnnyantRoman', 20, 'bold'), text_color='lightgray', fg_color='#1b1b1b', hover_color='#373434', command=lambda: self.trocar_telas((self.exibe_autor)))
        self.bot_listautor.place(x=400, y=210)

        self.Bot_fechar_ne = ctk.CTkButton(self.frame_atual, width=280,height=40, text='Sair', font=('AnnyantRoman', 20, 'bold'), text_color='lightgray', fg_color='#1b1b1b', hover_color='#373434',command=lambda: sair(matriz_principal))
        self.Bot_fechar_ne.place(x=400, y=330)

        self.label_lupa = ctk.CTkLabel(master=self.frame_atual, text=None, image=self.lupinha, bg_color='#242424')
        self.label_lupa.place(x=665, y=55)
        self.label_logo = ctk.CTkLabel(master=self.frame_atual, text=None, image=self.logo, bg_color='#242424')
        self.label_logo.place(x=50, y=50)

        self.frame_barra = ctk.CTkFrame(master=self.frame_atual, width=400, height=300)
        self.direitos()

    def frame_pesquisa(self):
        self.padrao_logo()
        self.frame_planilha = ctk.CTkFrame(self.frame_atual, width=525, height=350)
        self.bot_alterar_titulo()
        self.frame_planilha.place(x=120, y=50)
        self.frame_planilha.pack_propagate(False)
    
        bot_voltar = ctk.CTkButton(self.frame_atual, width=50, text='^', font=self.fonteceta, text_color='lightgray', fg_color='#2b2b2b', hover_color='#373434', command=lambda: self.trocar_telas(self.telainicio))
        bot_voltar.place(x=15, y=50)
        self.direitos()

    def planilha(self, dados, pagina_atual, tamanho_pagina):
        def carregar_dados(treeview, dados, inicio, fim):
            for i in range(inicio, min(fim, len(dados))):
                if dados[i][2] < 0:
                    ano = f'{dados[i][2] * -1}A.c'   
                else:
                    ano= dados[i][2]
                situacao = 'Disponivel' if not dados[i][3] else 'Indisponivel'
                treeview.insert('', 'end', iid=i, values=(dados[i][0], dados[i][1], ano, situacao))

        def atualizar_exibicao(tree, dados, pagina, tamanho_pagina):
            tree.delete(*tree.get_children())
            inicio = pagina * tamanho_pagina
            fim = inicio + tamanho_pagina
            carregar_dados(tree, dados, inicio, fim)
            tree.yview_moveto(0)
            self.janela.after(100, criar_botao)
            self.janela.after(100, criar_botao2)

        def avancar_pagina():
            nonlocal pagina_atual
            if (pagina_atual + 1) * tamanho_pagina < len(dados):
                pagina_atual += 1
                atualizar_exibicao(tree, dados, pagina_atual, tamanho_pagina)

        def voltar_pagina():
            nonlocal pagina_atual
            if pagina_atual > 0:
                pagina_atual -= 1
                atualizar_exibicao(tree, dados, pagina_atual, tamanho_pagina)

        def criar_botao():
            for item in tree.get_children():
                bbox = tree.bbox(item, column="col5")
                if bbox:
                    x, y, largura, altura = bbox
                    canvas = tk.Canvas(tree, width=largura, height=altura, borderwidth=0, highlightthickness=0, bg='#242424')
                    canvas.place(x=x, y=y, anchor='nw')
                    botao_tree = ctk.CTkButton(tree, text='X', height=20, width=20, bg_color='#202020',hover_color='#992525', fg_color='transparent', command=lambda item=item: clicar_botao(item))
                    canvas.create_window((largura // 2, altura // 2), window=botao_tree, anchor='center')

        def clicar_botao(item):
            global matriz
            global matriz_principal
            if self.frame_planilha is not None:
                self.frame_planilha.destroy()
            self.frame_planilha = ctk.CTkFrame(self.frame_atual, width=525, height=350)
            self.frame_planilha.place(x=120, y=50)
            self.frame_planilha.pack_propagate(False)
            item_removido = matriz[int(item)]
            for i in range(len(matriz_principal)-1):
                if matriz_principal[i][0] == item_removido[0]:
                    matriz_principal = remover_livros(matriz_principal, i)
            self.planilha(matriz, self.pagina_atual, self.tamanho_pagina)

        def criar_botao2():
            for item in tree.get_children():
                bbox = tree.bbox(item, column="col6")
                if bbox:
                    x, y, largura, altura = bbox
                    canvas = tk.Canvas(tree, width=largura, height=altura, borderwidth=0, highlightthickness=0, bg='#242424')
                    canvas.place(x=x, y=y, anchor='nw')
                    botao_tree = ctk.CTkButton(tree, text='edit', height=20, width=20, bg_color='#202020',hover_color='#242424', fg_color='transparent', command=lambda item=item: clicar_botao2(item))
                    canvas.create_window((largura // 2, altura // 2), window=botao_tree, anchor='center')

        def clicar_botao2(item):
            self.trocar_telas(self.trocar_livro)
            self.linha=item
           

        tree = ttk.Treeview(self.frame_planilha, style=self.estilo, show='headings')
        tree.pack(fill=tk.BOTH, expand=True)
        tree["columns"] = ("col1", "col2", "col3", "col4", "col5","col6")
        tree.heading("col1", text="Titulo")
        tree.heading("col2", text="Autor")
        tree.heading("col3", text='Ano')
        tree.heading("col4", text='Situação')
        tree.heading("col5", text='del')
        tree.heading("col6", text='edit')
        tree.column("col1", width=150, minwidth=100)
        tree.column("col2", width=110)
        tree.column("col3", width=40)
        tree.column("col4", width=100)
        tree.column("col5", width=50)
        tree.column("col6", width=50)

        botao_anterior = ctk.CTkButton(self.frame_atual,width=10, text="t",font=self.fonteceta, fg_color='#2b2b2b', hover_color='#373434', command=voltar_pagina)
        botao_anterior.place(x=120,y=420)
        botao_proximo = ctk.CTkButton(self.frame_atual,width=10, text="u",font=self.fonteceta,  fg_color='#2b2b2b', hover_color='#373434', command=avancar_pagina)
        botao_proximo.place(x=160,y=420)

        atualizar_exibicao(tree, dados, pagina_atual, tamanho_pagina)
    
    def exibe_autor(self):
        self.espera(self.criar_frame())

    def criar_frame(self):
        self.padrao_logo()
        def atualizar_exibicao(pagina_atual):
            inicio_autor = pagina_atual * 15
            fim_autor = inicio_autor + 15
            autores_a_exibir = self.lista_autor[inicio_autor:fim_autor]
            
            for widget in frame_autor.winfo_children():
                widget.destroy()
            
            for i, autor in enumerate(autores_a_exibir):
                bot_exibe_autor = ctk.CTkButton(frame_autor, width=420, height=20, text=f'{autor[0]}', font=('', 15, 'bold'), text_color='lightgray', fg_color='#373434', hover_color='#f0f0f0', command=lambda autor=autor: self.espera(self.pesquisa(matriz_principal, 1, autor[0])))
                bot_exibe_autor.grid(column=0, row=i)
                exibe_vezes = ctk.CTkLabel(frame_autor, width=10, height=20, text=f'{autor[1]}', font=('', 15, 'bold'), text_color='lightgray', fg_color='#373434')
                exibe_vezes.grid(column=1, row=i)

        def proxima_pagina():
            nonlocal pagina_atual
            if (pagina_atual + 1) * 15 < len(self.lista_autor):
                pagina_atual += 1
                atualizar_exibicao(pagina_atual)

        def pagina_anterior():
            nonlocal pagina_atual
            if pagina_atual > 0:
                pagina_atual -= 1
                atualizar_exibicao(pagina_atual)

        pagina_atual = 0

        frame_autor = ctk.CTkFrame(self.frame_atual, width=450, height=360)
        frame_autor.place(x=120, y=50)
        frame_autor.pack_propagate(False)

        atualizar_exibicao(pagina_atual)

        bot_voltar = ctk.CTkButton(self.frame_atual, width=50, text='^', font=self.fonteceta, text_color='lightgray', fg_color='#2b2b2b', hover_color='#373434', command=lambda: self.trocar_telas(self.telainicio))
        bot_voltar.place(x=15, y=50)

        bot_pagina_anterior = ctk.CTkButton(self.frame_atual, width=30, text='t', font=self.fonteceta, text_color='lightgray', fg_color='#2b2b2b', hover_color='#373434', command=pagina_anterior)
        bot_pagina_anterior.place(x=120, y=420)

        bot_proxima_pagina = ctk.CTkButton(self.frame_atual, width=30, text='u', font=self.fonteceta, text_color='lightgray', fg_color='#2b2b2b', hover_color='#373434', command=proxima_pagina)
        bot_proxima_pagina.place(x=160, y=420)
        
        self.direitos()
    def registrar_livro(self):
        global matriz_principal
        self.label_logo = ctk.CTkLabel(master=self.frame_atual, text=None, image=self.logo, bg_color='#242424')
        self.label_logo.place(x=50, y=50)
        self.nome = ctk.CTkLabel(self.frame_atual, text='Anthill', font=('AnnyantRoman',40,'bold'), text_color='#f0f0f0')
        self.nome.place(x=15, y=250)
        self.nome2 = ctk.CTkLabel(self.frame_atual, text='Library', font=('AnnyantRoman',40,'bold'), text_color='#f0f0f0')
        self.nome2.place(x=50, y=300)
        self.nome3 = ctk.CTkLabel(self.frame_atual, text='Resgistrar novo livro', font=('AnnyantRoman',23,'bold'), text_color='#f0f0f0')
        self.nome3.place(x=280, y=30)


        self.titulo_entry=ctk.CTkEntry(self.frame_atual,width=380,height=40,placeholder_text='TITULO',font=('',18,'bold'),fg_color='#242424',placeholder_text_color='#545454')
        self.autor_entry=ctk.CTkEntry(self.frame_atual,width=380,height=40,placeholder_text='AUTOR',font=('',18,'bold'),fg_color='#242424',placeholder_text_color='#545454')
        self.ano_entry=ctk.CTkEntry(self.frame_atual,width=380,height=40,placeholder_text='ANO',font=('',18,'bold'),fg_color='#242424',placeholder_text_color='#545454')
        self.titulo_entry.place(x=280,y=100)
        self.autor_entry.place(x=280,y=200)
        self.ano_entry.place(x=280,y=300)
        self.titulo_desc=ctk.CTkLabel(self.frame_atual,text='Insira o TITULO do livro aqui:',font=('AnnyantRoman',12,'bold'),text_color='#909090')
        self.titulo_desc.place(x=280,y=70)
        self.titulo_desc=ctk.CTkLabel(self.frame_atual,text='Insira o AUTOR do livro aqui:',font=('AnnyantRoman',12,'bold'),text_color='#909090')
        self.titulo_desc.place(x=280,y=170)
        self.titulo_desc=ctk.CTkLabel(self.frame_atual,text='Insira o ANO em que o livro foi publicado aqui:',font=('AnnyantRoman',12,'bold'),text_color='#909090')
        self.titulo_desc.place(x=280,y=270)
        self.registroo = ctk.CTkButton(self.frame_atual, width=380, height=34,text='FINALIZAR REGISTRO', font=('AnnyantRoman', 20, 'bold'), text_color='#909090', fg_color='#1b1b1b', hover_color='#373434', command=lambda: adicionar_livros(matriz_principal, [self.titulo_entry.get(), self.autor_entry.get(), int(self.ano_entry.get()), False]))
        self.registroo.place(x=280, y=355)

        bot_voltar = ctk.CTkButton(self.frame_atual, width=50, text='^', font=self.fonteceta, text_color='lightgray', fg_color='#2b2b2b', hover_color='#373434', command=lambda: self.trocar_telas(self.telainicio))
        bot_voltar.place(x=15, y=25)

    
    def trocar_livro(self):
        global matriz_principal

        self.label_logo = ctk.CTkLabel(master=self.frame_atual, text=None, image=self.logo, bg_color='#242424')
        self.label_logo.place(x=50, y=50)
        self.nome = ctk.CTkLabel(self.frame_atual, text='Anthill', font=('AnnyantRoman',40,'bold'), text_color='#f0f0f0')
        self.nome.place(x=15, y=250)
        self.nome2 = ctk.CTkLabel(self.frame_atual, text='Library', font=('AnnyantRoman',40,'bold'), text_color='#f0f0f0')
        self.nome2.place(x=50, y=300)
        self.nome3 = ctk.CTkLabel(self.frame_atual, text='Editar Livro', font=('AnnyantRoman',23,'bold'), text_color='#f0f0f0')
        self.nome3.place(x=280, y=30)

        self.titulo_entry=ctk.CTkEntry(self.frame_atual,width=380,height=40,placeholder_text='TITULO',font=('',20,'bold'),fg_color='#242424',placeholder_text_color='#545454')
        self.autor_entry=ctk.CTkEntry(self.frame_atual,width=380,height=40,placeholder_text='AUTOR',font=('',20,'bold'),fg_color='#242424',placeholder_text_color='#545454')
        self.ano_entry=ctk.CTkEntry(self.frame_atual,width=380,height=40,placeholder_text='ANO',font=('',20,'bold'),fg_color='#242424',placeholder_text_color='#545454')
        self.titulo_entry.place(x=280,y=100)
        self.autor_entry.place(x=280,y=200)
        self.ano_entry.place(x=280,y=300)
        self.titulo_desc=ctk.CTkLabel(self.frame_atual,text='Insira o TITULO do livro aqui:',font=('AnnyantRoman',12,'bold'),text_color='#909090')
        self.titulo_desc.place(x=280,y=70)
        self.titulo_desc=ctk.CTkLabel(self.frame_atual,text='Insira o AUTOR do livro aqui:',font=('AnnyantRoman',12,'bold'),text_color='#909090')
        self.titulo_desc.place(x=280,y=170)
        self.titulo_desc=ctk.CTkLabel(self.frame_atual,text='Insira o ANO em que o livro foi publicado aqui:',font=('AnnyantRoman',12,'bold'),text_color='#909090')
        self.titulo_desc.place(x=280,y=270)
        self.registroo = ctk.CTkButton(self.frame_atual, width=380, height=34,text='EDITAR REGISTRO', font=('AnnyantRoman', 20, 'bold'), text_color='#909090', fg_color='#1b1b1b', hover_color='#373434', command=lambda: editar_livro(matriz_principal, [self.titulo_entry.get(), self.autor_entry.get(), int(self.ano_entry.get()), False],int(self.linha)))
        self.registroo.place(x=280, y=355)

        bot_voltar = ctk.CTkButton(self.frame_atual, width=50, text='^', font=self.fonteceta, text_color='lightgray', fg_color='#2b2b2b', hover_color='#373434', command=lambda: self.trocar_telas(self.telainicio))
        bot_voltar.place(x=15, y=25)

    def biblioteca(self):
        self.padrao_logo()
        bot_voltar = ctk.CTkButton(self.frame_atual, width=50, text='^', font=self.fonteceta, text_color='lightgray', fg_color='#2b2b2b', hover_color='#373434', command=lambda: self.trocar_telas(self.telainicio))
        bot_voltar.place(x=15, y=50)

        self.frame_planilha = ctk.CTkFrame(self.frame_atual, width=525, height=350)
        self.frame_planilha.place(x=120, y=50)
        self.frame_planilha.pack_propagate(False)

        self.planilha(matriz, self.pagina_atual, self.tamanho_pagina)
        self.direitos()
        self.bot_alterar_titulo()
   
    def direitos(self):
        direitos = 'LIeC  Email: liec@gmail.com   IFRN-Campus Pau Dos Ferros'
        self.ref = ctk.CTkLabel(self.frame_atual, text=direitos, font=('', 12, 'bold'), text_color='#f0f0f0')
        self.ref.place(x=380, y=455)
    
    def padrao_logo(self):
        self.label_logo2 = ctk.CTkLabel(master=self.frame_atual, text=None, image=self.logo_menor, bg_color='#242424')
        self.label_logo2.place(x=12, y=12)

        self.nome_menor = ctk.CTkLabel(master=self.frame_atual, text='Anthill', text_color='#f0f0f0', font=self.fonte2, height=10)
        self.nome_menor.place(x=40, y=18)
        self.nome_menor2 = ctk.CTkLabel(master=self.frame_atual, text='LIB.', text_color='#f0f0f0', font=self.fonte2, height=10)
        self.nome_menor2.place(x=40, y=28)

#______________________________________________________________________
