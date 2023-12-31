import customtkinter
from tkinter import *


# Define uma variável global para armazenar o operador------------------
valor = ''
#-----------------------------------------------------------------------

# Função para atualizar a cor da letra dos botões
def atualizar_cor_letra(value=None):
    red = int(sfgRed.get())  # Obtenha o valor do slider de vermelho
    green = int(sfgren.get())  # Obtenha o valor do slider de verde
    blue = int(sfBlue.get())  # Obtenha o valor do slider de azul

    # Converta os valores para representação hexadecimal
    cor_hex = "#{:02X}{:02X}{:02X}".format(red, green, blue)

    # Atualize a cor da letra dos botões
    for botao in [b_Nove, b_oito, b_Sete, b_Seis, b_Cinco, b_Quatro, b_Tres, b_dois, b_Um, b_zero,
                  b_Clear, b_Ponto, b_Divisao, b_Modulo, b_Multiplicacao, b_Subtracao, b_Soma, b_igual]:
        # Tente diferentes argumentos para configurar a cor do texto
        botao.configure(text_color=cor_hex)
        # ou botao.configure(foreground=cor_hex)
# ...


# função para Calcular precentagem e limpar ---------------------------------------------------
def calcular():
    global valor  # Acesse a variável global 'valor'
    entrada = ecra.get()

    if valor == "=":
        # Chame a função calcular() recursivamente para calcular o resultado
        calcular_resultado()
    elif valor == 'C':
        limpar()
    elif valor == '%':
        try:
            partes = entrada.split('%')
            if len(partes) == 2:
                numero = float(partes[0])
                resultado = numero % float(partes[1])  # Use o operador de módulo (%) para calcular o resultado
            else:
                raise ValueError("Entrada inválida")
            ecra.delete(0, customtkinter.END)
            ecra.insert(customtkinter.END, str(resultado))
        except Exception as e:
            ecra.delete(0, customtkinter.END)
            ecra.insert(customtkinter.END, "Erro")
    else:
        ecra.insert(customtkinter.END, str(valor))
#----------------------------------------------------------------------------------------------

# Função para calcular o resultado --------------------------------------------------------------
def calcular_resultado():
    entrada = ecra.get()
    try:
        resultado = eval(entrada)  # Use a função eval para avaliar a expressão
        ecra.delete(0, customtkinter.END)
        ecra.insert(customtkinter.END, str(resultado))
    except Exception as e:
        ecra.delete(0, customtkinter.END)
        ecra.insert(customtkinter.END, "Erro")
#------------------------------------------------------------------------------------------------
# Função para limpar o campo de entrada ----------------------------------------------------------
def limpar():
    ecra.delete(0, customtkinter.END)
#-------------------------------------------------------------------------------------------------
# função a setar o valor e verificar valor -------------------------------------------------------
def set_valor(novo_valor):
    global valor
    valor = novo_valor
      # Verifique se o novo valor é o botão de porcentagem (%)
    if novo_valor == '%':
        calcular_resultado()
    else:
        calcular()
#--------------------------------------------------------------------------------------------------

# criar as cores a usar ---------------------------------------------------------------------------
Co0 ='#7FD5FF'        
#--------------------------------------------------------------------------------------------------        


janela = customtkinter.CTk()
janela.geometry('200x350+100+100')
janela.resizable(False, False)
janela.iconbitmap(r'C:\Users\HP\Desktop\Programas em python\Calculadora Customtkinter V1\Calcudaora v1.1.2\icon.ico')
janela.title('calculadora V2')

# carregar a imagem de fundo -------------------------------------------------------
imag = PhotoImage(file=r"C:\Users\HP\Desktop\Programas em python\Calculadora Customtkinter V1\Calcudaora v1.1.2\fundo.png")
Limg = Label(janela, image=imag)
Limg.place(x=0, y=0)
#-----------------------------------------------------------------------------------

# criar o ecra -------------------------------------------------------------------------------------
ecra = customtkinter.CTkEntry(janela, width=175, justify="right", bg_color=Co0)  # Definindo o alinhamento para a direita
ecra.place(x=10, y=10)
# ---------------------------------------------------------------------------------------------------

# Botões numéricos -----------------------------------------------------------------------------------
b_Nove = customtkinter.CTkButton(janela, text='9', width=40, command=lambda: ecra.insert(customtkinter.END, '9'), bg_color=Co0)
b_Nove.place(x=100, y=85)

b_oito = customtkinter.CTkButton(janela, text='8', width=40, command=lambda: ecra.insert(customtkinter.END, '8'), bg_color=Co0)
b_oito.place(x=55, y=85)

b_Sete = customtkinter.CTkButton(janela, text='7', width=40, command=lambda: ecra.insert(customtkinter.END, '7'), bg_color=Co0)
b_Sete.place(x=10, y=85)

b_Seis = customtkinter.CTkButton(janela, text='6', width=40, command=lambda: ecra.insert(customtkinter.END, '6'), bg_color=Co0)
b_Seis.place(x=100, y=120)

b_Cinco = customtkinter.CTkButton(janela, text='5', width=40, command=lambda: ecra.insert(customtkinter.END, '5'), bg_color=Co0)
b_Cinco.place(x=55, y=120)

b_Quatro = customtkinter.CTkButton(janela, text='4', width=40, command=lambda: ecra.insert(customtkinter.END, '4'), bg_color=Co0)
b_Quatro.place(x=10, y=120)

b_Tres = customtkinter.CTkButton(janela, text='3', width=40, command=lambda: ecra.insert(customtkinter.END, '3'), bg_color=Co0)
b_Tres.place(x=100, y=155)

b_dois = customtkinter.CTkButton(janela, text='2', width=40, command=lambda: ecra.insert(customtkinter.END, '2'), bg_color=Co0)
b_dois.place(x=55, y=155)

b_Um = customtkinter.CTkButton(janela, text='1', width=40, command=lambda: ecra.insert(customtkinter.END, '1'), bg_color=Co0)
b_Um.place(x=10, y=155)

b_zero = customtkinter.CTkButton(janela, text='0', width=70, command=lambda: ecra.insert(customtkinter.END, '0'), bg_color=Co0)
b_zero.place(x=10, y=190)

b_Clear = customtkinter.CTkButton(janela, text='C', width=80, command=limpar, bg_color=Co0)  # Adicionei o comando para limpar
b_Clear.place(x=10, y=50)

b_Ponto = customtkinter.CTkButton(janela, text='.', width=50, command=lambda: ecra.insert(customtkinter.END, '.'), bg_color=Co0)
b_Ponto.place(x=85, y=190)
#--------------------------------------------------------------------------------------------------------------------

# Operadores --------------------------------------------------------------------------------------------------------
b_Divisao = customtkinter.CTkButton(janela, text='/', width=40, command=lambda: ecra.insert(customtkinter.END, '/'), bg_color=Co0)
b_Divisao.place(x=145, y=50)

b_Modulo = customtkinter.CTkButton(janela, text='%', width=40, command=lambda: set_valor('%'), bg_color=Co0)
b_Modulo.place(x=100, y=50)


b_Multiplicacao = customtkinter.CTkButton(janela, text='*', width=40, command=lambda: ecra.insert(customtkinter.END, '*'), bg_color=Co0)
b_Multiplicacao.place(x=145, y=85)

b_Subtracao = customtkinter.CTkButton(janela, text='-', width=40, command=lambda: ecra.insert(customtkinter.END, '-'), bg_color=Co0)
b_Subtracao.place(x=145, y=120)

b_Soma = customtkinter.CTkButton(janela, text='+', width=40, command=lambda: ecra.insert(customtkinter.END, '+'), bg_color=Co0)
b_Soma.place(x=145, y=155)


b_igual = customtkinter.CTkButton(janela, text='=', width=45, command=lambda: set_valor('='),bg_color=Co0)
b_igual.place(x=140, y=190)

#--------------------------------------------------------------------------------------------------------------------

forground = customtkinter.CTkLabel(janela, text='Mudar a Cor de Letra ao Botões', bg_color=Co0)
forground.place(x=5, y=225)

# criar os sacles para aletar o fg ----------------------------------------------------------------------------------
sfgRed = customtkinter.CTkSlider(janela, to=0, from_=255, command=atualizar_cor_letra, bg_color=Co0)
sfgRed.place(x=0, y=255)
sfgren = customtkinter.CTkSlider(janela, to=0, from_=255, command=atualizar_cor_letra, bg_color=Co0)
sfgren.place(x=0, y=285)
sfBlue = customtkinter.CTkSlider(janela, to=0, from_=255, command=atualizar_cor_letra, bg_color=Co0)
sfBlue.place(x=0, y=315)
# variaveis ---------------------------------------------------------------------------------------------------------
# Configurar os sliders para chamar a função de atualização de cor quando seus valores mudam
sfgRed.configure(command=atualizar_cor_letra)
sfgren.configure(command=atualizar_cor_letra)
sfBlue.configure(command=atualizar_cor_letra)
#--------------------------------------------------------------------------------------------------------------------
janela.mainloop()