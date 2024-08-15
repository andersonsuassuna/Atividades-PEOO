jogo=[[0,0,0],[0,0,0],[0,0,0]]
def check(game):
    if game[0][0]==1 and game[1][0]==1 and game[2][0]==1:
        print("Jogador 1 venceu!")

    elif game[0][0]==2 and game[0][0]==2 and game[0][0]==2:
    
    elif game[0][1]==1 and game[1][1]==1 and game[1][2]==1:
        print("Jogador 1 venceu!")
    
    if game[0][2]==1 and game[1][2]==1 and game[2][2]==1:
    
    if game[0][0]==1 and game[0][0]==1 and game[0][0]==1:
    
    if game[0][0]==1 and game[0][0]==1 and game[0][0]==1:
    
    if game[0][0]==1 and game[0][0]==1 and game[0][0]==1:

def player1(game):
    linha=int(input("Linha: "))
    coluna=int(input("Coluna: "))
    game[linha][coluna]=1
def player2(game):
    linha=int(input("Linha: "))
    coluna=int(input("Coluna: "))
    game[linha][coluna]=2