jogo=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
import itertools as it

def check(game):
    for i in range(1):
        if 1==game[i][i]==game[i][i+1]==game[i][i+2]:
            print("Jogador 1 venceu!")
            exit()
        if 1==game[i][i]==game[i+1][i]==game[i+2][i]:
            print("Jogador 1 venceu!")
            exit()
        if 2==game[i][i]==game[i][i+1]==game[i][i+2]:
            print("Jogador 2 venceu!")
            exit()
        if 2==game[i][i]==game[i+1][i]==game[i+2][i]:
            print("Jogador 2 venceu!")
            exit()
        if 1==game[0][0]==game[1][1]==game[2][2]:
            print("Jogador 1 venceu!")
            exit()
        if 1==game[0][2]==game[1][1]==game[2][0]:
            print("Jogador 1 venceu!")
            exit()
        if 2==game[0][0]==game[1][1]==game[2][2]:
            print("Jogador 2 venceu!")
            exit()
        if 2==game[0][2]==game[1][1]==game[2][0]:
            print("Jogador 2 venceu!")
            exit()
        if 0!=game[0][0] and 0!=game[0][1] and 0!=game[0][2] and 0!=game[1][0] and 0!=game[1][1] and 0!=game[1][2] and 0!=game[2][0] and 0!=game[2][1] and 0!=game[2][2]:
            print("Deu velha!")
            exit()
    print(*game, sep="\n")

def player1(game):
    print("Jogador 1")
    linha=int(input("Linha: "))-1
    coluna=int(input("Coluna: "))-1
    if game[linha][coluna]==0:
        game[linha][coluna]=1
    else:
        print("Já foi marcado!")
        player1(game)

def player2(game):
    print("Jogador 2")
    linha=int(input("Linha: "))-1
    coluna=int(input("Coluna: "))-1
    if game[linha][coluna]==0:
        game[linha][coluna]=2
    else:
        print("Já foi marcado!")
        player2(game)

def jogar(game):
    for i in it.count():
        player1(game)
        check(game)
        player2(game)
        check(game)

print(*jogo, sep="\n")
jogar(jogo)