x=0 # Enquanto uma condição for verdadeira, algo acontece.
while x<300:
    x=x+1 # somando
    print(x)
    
vt=int(input("Valor total: "))
pessoas=4
while pessoas>0:
    vn=float(input("Valor que a primeira pessoa vai pagar: "))
    vt=vt-vn
    if vt<0:
        print("O valor foi além do suportado!")
        exit()
    print(f"Restante: {vt}")
    pessoas=pessoas-1 # subtraindo
print("Obrigado!")