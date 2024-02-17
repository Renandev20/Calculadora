import tkinter as tk
def Tela():
    class Calculadora:
        import tkinter as tk

        class Tela():
            def __init__(self):
                self.tela = tk.Tk()
                self.tela.title("Calculadora")
                self.tela.resizable(width=False, height=False)
                self.Res = ""
                self.Valores = 0
                self.WIDTH = 10
                self.HEIGHT = 3
                self.Fonte = "Arial 14 bold"

                def atualizar(auxBt):
                    self.Res += auxBt
                    self.auxResultado.set(self.Res)

                def calcular():
                    Digitos = []
                    oper = []
                    num = []
                    print(self.Res)
                    for i in self.Res:
                        if i.isdigit():
                            Digitos.append(i)
                        else:
                            oper.append(i)
                            Digitos.append("*")
                    NumStr = "".join(Digitos)
                    NumStr = NumStr.split("*")
                    for j in NumStr:
                        num.append(j)

                    # operações
                    if oper[0] == "+":
                        ResTotal = int(num[0]) + int(num[1])
                    if oper[0] == "-":
                        ResTotal = int(num[0]) - int(num[1])
                    if oper[0] == "x":
                        ResTotal = int(num[0]) * int(num[1])
                    if oper[0] == "/":
                        ResTotal = round(int(num[0]) / int(num[1]), 1)

                    self.auxResultado.set(str(ResTotal))

                    print(Digitos)
                    print(NumStr)
                    print(oper)
                    self.Res = []

                def limpar():
                    self.Res = ""
                    self.auxResultado.set("---")

                self.auxResultado = tk.StringVar()
                self.auxResultado.set("---")
                self.lbResultado = tk.Label(self.tela, textvariable=self.auxResultado, font="Verdana 12 bold",
                                            borderwidth=5)
                self.lbResultado.grid(row=0, columnspan=3)

                # (C) botão para limpar
                self.btLimpar = tk.Button(self.tela, text="C", width=self.WIDTH, height=self.HEIGHT, font=self.Fonte,
                                          bg="red", command=lambda: limpar())
                self.btLimpar.grid(row=1, column=3, padx=2, pady=2)

                # Botão 0
                self.auxBt0 = tk.StringVar()
                self.auxBt0.set(0)
                self.bt01 = tk.Button(self.tela, textvariable=self.auxBt0, width=self.WIDTH, height=self.HEIGHT,
                                      font=self.Fonte, command=lambda: atualizar(self.auxBt0.get()))
                self.bt01.grid(row=1, column=0, padx=2, pady=2)

                # Botão 1
                self.auxBt1 = tk.StringVar()
                self.auxBt1.set(1)
                self.bt1 = tk.Button(self.tela, textvariable=self.auxBt1, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt1.get()))
                self.bt1.grid(row=1, column=1, padx=2, pady=2)

                # Botão 2
                self.auxBt2 = tk.StringVar()
                self.auxBt2.set(2)
                self.bt2 = tk.Button(self.tela, textvariable=self.auxBt2, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt2.get()))
                self.bt2.grid(row=1, column=2, padx=2, pady=2)

                # Botão 3
                self.auxBt3 = tk.StringVar()
                self.auxBt3.set(3)
                self.bt4 = tk.Button(self.tela, textvariable=self.auxBt3, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt3.get()))
                self.bt4.grid(row=2, column=0, padx=2, pady=2)

                # Botão 4
                self.auxBt4 = tk.StringVar()
                self.auxBt4.set(4)
                self.bt4 = tk.Button(self.tela, textvariable=self.auxBt4, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt4.get()))
                self.bt4.grid(row=2, column=1, padx=2, pady=2)

                # Botão 5
                self.auxBt5 = tk.StringVar()
                self.auxBt5.set(5)
                self.bt5 = tk.Button(self.tela, textvariable=self.auxBt5, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt5.get()))
                self.bt5.grid(row=2, column=2, padx=2, pady=2)

                # Botão 6
                self.auxBt6 = tk.StringVar()
                self.auxBt6.set(6)
                self.bt6 = tk.Button(self.tela, textvariable=self.auxBt6, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt6.get()))
                self.bt6.grid(row=3, column=0, padx=2, pady=2)

                # Botão 7
                self.auxBt7 = tk.StringVar()
                self.auxBt7.set(7)
                self.bt7 = tk.Button(self.tela, textvariable=self.auxBt7, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt7.get()))
                self.bt7.grid(row=3, column=1, padx=2, pady=2)

                # Botão 8
                self.auxBt8 = tk.StringVar()
                self.auxBt8.set(8)
                self.bt8 = tk.Button(self.tela, textvariable=self.auxBt8, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt8.get()))
                self.bt8.grid(row=3, column=2, padx=2, pady=2)

                # Botão 9
                self.auxBt9 = tk.StringVar()
                self.auxBt9.set(9)
                self.bt9 = tk.Button(self.tela, textvariable=self.auxBt9, width=self.WIDTH, height=self.HEIGHT,
                                     font=self.Fonte, command=lambda: atualizar(self.auxBt9.get()))
                self.bt9.grid(row=4, column=0, padx=2, pady=2)

                # operador -
                self.auxBtMenos = tk.StringVar()
                self.auxBtMenos.set("-")
                self.btMenos = tk.Button(self.tela, textvariable=self.auxBtMenos, width=self.WIDTH, height=self.HEIGHT,
                                         font=self.Fonte, bg="light blue",
                                         command=lambda: atualizar(self.auxBtMenos.get()))
                self.btMenos.grid(row=4, column=1, padx=2, pady=2)

                # operador +
                self.auxBtMais = tk.StringVar()
                self.auxBtMais.set("+")
                self.btMais = tk.Button(self.tela, textvariable=self.auxBtMais, width=self.WIDTH, height=self.HEIGHT,
                                        font=self.Fonte, bg="light blue",
                                        command=lambda: atualizar(self.auxBtMais.get()))
                self.btMais.grid(row=4, column=2, padx=2, pady=2)

                # operador /
                self.auxBtDiv = tk.StringVar()
                self.auxBtDiv.set("/")
                self.btDiv = tk.Button(self.tela, textvariable=self.auxBtDiv, width=self.WIDTH, height=self.HEIGHT,
                                       font=self.Fonte, bg="light blue", command=lambda: atualizar(self.auxBtDiv.get()))
                self.btDiv.grid(row=5, column=0, padx=2, pady=2)

                # operador x
                self.auxBtMul = tk.StringVar()
                self.auxBtMul.set("x")
                self.btMul = tk.Button(self.tela, textvariable=self.auxBtMul, width=self.WIDTH, height=self.HEIGHT,
                                       font=self.Fonte, bg="light blue", command=lambda: atualizar(self.auxBtMul.get()))
                self.btMul.grid(row=5, column=1, padx=2, pady=2)

                # igual
                self.auxBtIgual = tk.StringVar()
                self.auxBtIgual.set("=")
                self.btIgual = tk.Button(self.tela, textvariable=self.auxBtIgual, width=self.WIDTH, height=self.HEIGHT,
                                         font=self.Fonte, bg="gray", command=lambda: calcular())
                self.btIgual.grid(row=5, column=2, padx=2, pady=2)

                self.tela.mainloop()

        Tela()



