from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
import mysql.connector
from mysql.connector import Error

def conexao():
    global con
    con = mysql.connector.connect(
    host = 'localhost',
    database = 'colegio',
    user = 'root',
    password = ''
)

def preencher_tabela():
    try:
        conexao()
        consulta_sql = 'SELECT * FROM cliente'
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        
        for item in tv.get_children():
            tv.delete(item)

        for linha in linhas:
            tv.insert("", "end", values=linha)
    except Error as erro:
        print('Falha ao inserir ao banco', erro) 
    finally:
        if(con.is_connected()):
                cursor.close()
                con.close()
                print('Conexão ao MySQL encerrada')

def inserir_usuario():
    name = EntNome.get()
    idade = EntIdade.get()
    sexo = comboSexo.get()
    cidade = comboCidade.get()
    altura = EntAltura.get()

    try:
        conexao()
        if name != '':
            if idade != '':
                if sexo != '':
                    if cidade != '':
                        if altura != '':        

                            consulta_sql = f'''INSERT INTO cliente
                                                (nomeCliente, dataNascimentoCliente, idSexo, idCidade, altura)
                                                VALUES
                                                ('{name}','{idade}',{sexo}, {cidade}, {altura})'''
                            
                            cursor = con.cursor()
                            cursor.execute(consulta_sql)
                            con.commit()
                            print(cursor.rowcount, 'registros foram iseridos')
                            preencher_tabela()
                            limpaCampos()
                        else:
                            messagebox.showinfo(title='Aviso', message='Informe sua Altura')
                    else:
                        messagebox.showinfo(title='Aviso', message='Informe sua Cidade')    
                else:
                    messagebox.showinfo(title='Aviso', message='Informe seu Sexo')
            else:
                messagebox.showinfo(title='Aviso', message='Informe sua Idade')        
        else:
            messagebox.showinfo(title='Aviso', message='Informe seu Nome')
    
    except Error as erro:
        print('Falha ao inserir ao banco', erro)     
    finally:
        if(con.is_connected()):
            cursor.close()
            con.close()
            print('Conexão ao MySQL encerrada')

def excluir_usuario():
    try: 
        try:
            conexao()
            itemSelecionado = tv.selection()
            idSelecionado = tv.item(itemSelecionado)['values'][0]
            consulta_sql = f'DELETE FROM cliente WHERE idCliente = {idSelecionado}'
            cursor = con.cursor()
            cursor.execute(consulta_sql)
            con.commit()
            print(cursor.rowcount, 'Registros foram Excluídos')
            preencher_tabela()
            limpaCampos()
        except:
            messagebox.showerror(title='ERRO', message='Selecione um elemento para ser deletado')
    except Error as erro:
        messagebox.showerror(title='ERRO', message='Selecione um elemento para ser deletado')
        print('Falha ao inserir ao banco', erro)
    finally:
        if(con.is_connected()):
                cursor.close()
                con.close()
                print('Conexão ao MySQL encerrada')    

def atualizar_usuario():
    name = EntNome.get()
    idade = EntIdade.get()
    sexo = comboSexo.get()
    cidade = comboCidade.get()
    altura = EntAltura.get()

    try:
        try:
            conexao()
            itemSelecionado = tv.selection()
            idSelecionado = tv.item(itemSelecionado)['values'][0]
            if name != '':
                if idade != '':
                    if sexo != '':
                        if cidade != '':
                            if altura != '':        
                                
                                consulta_sql = f'UPDATE cliente SET nomeCliente = "{name}", dataNascimentoCliente = "{idade}", idSexo = "{sexo}", idCidade = "{cidade}", altura = "{altura}"  WHERE idCliente = {idSelecionado}'
                                cursor = con.cursor()
                                cursor.execute(consulta_sql)
                                con.commit()
                                print(cursor.rowcount, 'registros foram alterados')
                                preencher_tabela()
                                limpaCampos()
                            else:
                                messagebox.showinfo(title='Aviso', message='Informe sua Altura')
                        else:
                            messagebox.showinfo(title='Aviso', message='Informe sua Cidade')    
                    else:
                        messagebox.showinfo(title='Aviso', message='Informe seu Sexo')
                else:
                    messagebox.showinfo(title='Aviso', message='Informe sua Idade')        
            else:
                messagebox.showinfo(title='Aviso', message='Informe seu Nome')
        except:
            messagebox.showerror(title='ERRO', message='Selecione um elemento para ser alterado')
    except Error as erro:
        messagebox.showerror(title='ERRO', message='Selecione um elemento para ser alterado')
        print('Falha ao inserir ao banco', erro)     
    finally:
        if(con.is_connected()):
            cursor.close()
            con.close()
            print('Conexão ao MySQL encerrada')   

def limpaCampos():
    EntNome.delete(0, END)
    EntIdade.delete(0, END)
    comboSexo.current(0)
    comboCidade.current(0)
    EntAltura.delete(0, END)

janela = Tk()
janela.title('Cadastro de Clientes')
janela.geometry('800x500')

tv = ttk.Treeview(janela, columns=('ID','Nome','Idade','Cidade','Sexo','Altura'), show='headings')
tv.column('ID', minwidth=0,width=50)
tv.column('Nome', minwidth=0,width=150)
tv.column('Idade', minwidth=0,width=150)
tv.column('Cidade', minwidth=0,width=100)
tv.column('Sexo', minwidth=0,width=100)
tv.column('Altura', minwidth=0,width=100)
tv.heading('ID', text='ID')
tv.heading('Nome', text='NOME')
tv.heading('Idade', text='IDADE')
tv.heading('Cidade', text='CIDADE')
tv.heading('Sexo', text='SEXO')
tv.heading('Altura', text='ALTURA')
preencher_tabela()

tv.place(relx=0.1,rely=0.1)

lbNome = Label(janela, text='Nome:')
lbNome.place(relx=0.1, rely=0.6)

EntNome = Entry(janela)
EntNome.place(relx=0.17, rely=0.6)

lbAltura = Label(janela, text='Altura:')
lbAltura.place(relx=0.1, rely=0.7)

EntAltura = Entry(janela)
EntAltura.place(relx=0.17, rely=0.7)

lbIdade = Label(janela, text='Idade:')
lbIdade.place(relx=0.1, rely=0.8)

EntIdade = Entry(janela)
EntIdade.place(relx=0.17, rely=0.8)

lbSexo = Label(janela, text='Sexo:')
lbSexo.place(relx=0.1, rely=0.9)

comboSexo = Combobox(janela)
comboSexo['values'] = ['Selecionar', '1', '2']
comboSexo.current(0)
comboSexo.place(relx=0.17, rely=0.9)

lbCidade = Label(janela, text='Cidade')
lbCidade.place(relx=0.4, rely=0.6)

comboCidade = Combobox(janela)
comboCidade['values'] = ['Selecionar', '1', '2', '3']
comboCidade.current(0)
comboCidade.place(relx=0.47, rely=0.6)

btInserir = Button(janela, text='Inserir', command=inserir_usuario)
btInserir.place(relx=0.45, rely=0.9)

btExcluir = Button(janela, text='Deletar', command=excluir_usuario)
btExcluir.place(relx=0.55, rely=0.9)

btAlterar = Button(janela, text='Alterar', command=atualizar_usuario)
btAlterar.place(relx=0.65, rely=0.9)


mainloop()