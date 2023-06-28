#desenvolvido por Alvinho Soares
saldo= float(1000)
quantia= int(0)
saques=[]
op=0
depositos=[]
header='###################################'
ext='#---------------------------------#'

while op < 4 :
    print(header)
    print("#       Introduza um opcção       #")
    print("#         1-> Deposito            #")
    print("#         2-> Saque               #")
    print("#         3-> Extrato             #")
    print("#         4-> Sair                #")
    print(header)
    op=int(input('->'))
    #deposito
    if op==1:
        quantia=int(input('introduza a quantia :'))
        
        if quantia > 0 :
            depositos.append(quantia)
            saldo =saldo+quantia
            print(f" {quantia:.2f}R$ Depositado com sucesso.")        
    #Sacar
    elif op ==2:
        quantia=int(input('Introdusa quantia a sacar :'))
        if len(saques)< 3 and quantia <= 500 and quantia<=saldo:
            saldo =saldo -quantia
            saques.append(quantia)
            print(f"Saque de  {quantia:.2f}R$ realizado com succeso.")
        else:
            print("Não foi possível realizar o saque OBS: só é permitido 3 saques por dia e val-Max 500R$")
    #extrato
    elif op == 3 :
        print("Extrato :")
        if len(depositos) == 0 and len(saques):
            print("0 movimentações realizadas.")
        else:
            for deposito in depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in saques:
                print(ext)
                print('#                                 #')
                print(f"Saque: R$ {saque:.2f}")
                print(f"Saldo atual: R$ {saldo:.2f}")
                print('#                                 #')
                print(ext)