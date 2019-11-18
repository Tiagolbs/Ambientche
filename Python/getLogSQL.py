from tkinter import * #Interface
import psycopg2 #Postgresql

class Application: #Definição da interface
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
        
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 5
        self.quartoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Dados do postgres")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Nome do banco", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.nomeTabLabel = Label(self.segundoContainer,text="Nome da database", font=self.fontePadrao)
        self.nomeTabLabel.pack(side=LEFT)

        self.nomeTab = Entry(self.segundoContainer)
        self.nomeTab["width"] = 30
        self.nomeTab["font"] = self.fontePadrao
        self.nomeTab.pack(side=LEFT)
  
        self.portaLabel = Label(self.segundoContainer,text="Porta", font=self.fontePadrao)
        self.portaLabel.pack(side=LEFT)
  
        self.porta = Entry(self.segundoContainer)
        self.porta["width"] = 30
        self.porta["font"] = self.fontePadrao
        self.porta.pack(side=LEFT)
  
        self.senhaLabel = Label(self.segundoContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
  
        self.senha = Entry(self.segundoContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)
        
        self.attLog = Button(self.quartoContainer)
        self.attLog["text"] = "Atualizar Log"
        self.attLog["font"] = ("Calibri", "8")
        self.attLog["width"] = 12
        self.attLog["command"] = self.atualizaLog
        self.attLog.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        scrollbar = Scrollbar(master)
        scrollbar.pack(fill = Y, side = RIGHT)

        self.listbox = Listbox(self.quartoContainer, width = 45, height = 30)
        self.listbox.pack(pady = 5)
        self.listbox.config(yscrollcommand = scrollbar.set)
        self.listbox["font"] = ('Arial, 15')
        self.listbox.pack(side = LEFT)
        scrollbar.config(command = self.listbox)

    def atualizaLog(self):
        conSql = psycopg2.connect(user = self.nome.get(),password = self.senha.get(),host = "localhost",port = self.porta.get(),database = self.nomeTab.get()) #Faz a conexão com o postgresql
        cur = conSql.cursor() #Criação do cursor

        self.listbox.delete('0','end') #Limpa a listbox

        sql = 'select * from LogStatusLuz' #Comando para selecionar os logs da tabela
        cur.execute(sql) #Executa o comando sql
        conSql.commit()
        returnCur = cur.fetchall() #Retorno do comando sql

        for row in returnCur:
            linha = 'ID: ' + str(row[0]) + '    ' + 'Data: ' + str(row[1]) + '    '  + 'Comodo: ' + str(row[2]) + '    '  + 'Status: ' + str(row[3]) #Organiza a linha para mostrar no listbox
            self.listbox.insert(END, linha) #Insere a linha no final do listbox
        
  
root = Tk()
Application(root)
root.wm_title("Ambientche Log")
root.mainloop()



