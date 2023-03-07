import os 

while True:
    tamanho = input ("Qal o tamanho do ovo que você vai querer\nPequeno - R$7.80\nMédio - R$12.90\nGrande - R$23.95\nR: ").lower()

    if tamanho == "pequeno" :
        preco = 7.98
    elif tamanho == "medio" or tamanho == "médio":
        preco = 12.90
    else: 
        preco = 23.95

    sabor = input("\nQual sabor você ira querer\n1-Chocolate preto - R$9.67\n2-Chocolate branco R$4.50\n3-Chocolate ao leite R$9.32\nR: ").lower()

    if sabor == "Chocolate preto" or sabor == "1" or sabor ==  "preto":
        preco += 9.67
    elif sabor == "Chocolate branco" or sabor == "2" or sabor == "branco":
        preco += 4.50
    else: 
        preco += 9.32

    recheio1 = int(input ("\nQuantos recheios quer que o teu ovo tenha ? maximo 2 (temos apenas dois recheios sendo eles de chocolate branco e preto)\nR: "))

    if recheio1 == 1:
        recheio2 = input ("\nQual tipo de recheio você quer\nChocolate preto R$4.83\nChocolate branco R$2.25\nR: ")
        
        if recheio2 == "chocolate preto" or recheio2 == "preto":
            preco += 4.83
        else:
            preco += 2.25
    else:
        preco += ((4.83 / 2) + (2.25 / 2))

    adi = input ("\n Gostaria de ter adicional ?\nR: ").lower()

    if adi == "sim" or adi == "s" or adi == "ss":
        adi2 = int(input ("\nquantos adicionais você gostaria de por ? (Max 2 e temos apenas dois adicionais, mm e kitkat)\nR: "))
        if adi2 == 1:
            adi3 = input ("\nQual adicional você gostaria ?\nKitKat R$4.83\nMM R$5.43\nR: ").lower()
            if adi3 == "kitkat" or adi3 == "kit kat" or adi3 == "kit" or adi3 == "kat":
                preco += 4.83
            else:
                preco += 5.43
        else:
            preco += ((4.83 / 2) + (5.43 / 2))

    presente = input ("\nE para presente ?(tera um aumento de R$2.50)\nR: ").lower()

    if presente == "sim" or presente == "s" or presente == "ss":
        preco += 2.50

    entrega = input ("\nE para entrega ?(Tera um aumento de R$5.00)\nR: ")

    if entrega == "sim" or entrega == "s" or entrega == "ss":
        preco += 5.00

    quantidade = input("\nirá pedir mais de um ovo deste tipo?\nR: ").lower()

    if quantidade == "sim" or quantidade == "s" or quantidade == "ss":
        quantidade2 = int(input("\nQuantos ?\nR: "))
        if quantidade2 > 1:
         preco *= quantidade2

    pagamento = input ("\nQual a forma de pagamento ?\n1-Cartão de credito\n2-Pix\n3-Dinheiro\n4-Cartão de debito\nR: ").lower()

    if pagamento == "1" or pagamento == "credito" or pagamento == "crédito" or pagamento == "cartão de credito" or pagamento == "cartao de credito" or pagamento == "cartão de crédito" or pagamento == "cartao de credito":
        preco += 3.30
        
    elif pagamento == "dinheiro" or pagamento == "pix":
        pagamento *= 1.10

    print ("\no valor total foi de: R$"+str(preco))
    
    repetir = input("\nGostaria de fazer um outro pedido ?\nR: ")

    if repetir == "não" or repetir == "n" or repetir == "nn" or repetir == "nao":
        break
    os.system("pause")
    os.system("cls")
os.system("cls")