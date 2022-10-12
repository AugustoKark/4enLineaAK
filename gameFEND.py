from game import Cuatroenlinea
from exception import *

def main():
    game = Cuatroenlinea()
    game.jugada=0
    playing = True
    
    while playing:
        #printboard(game.board)
        playing = play(game)
        


def play(game):
    try:
        colum_ingreso =(input("INGRESE una columna: "))
        if colum_ingreso=="q" or "Q":
            return False
        game.jugada+=1
        letter_ingreso= input("Ingrese X o 0: ")
        game.token = (letter_ingreso)

        game.col= int(colum_ingreso)
        game.set(game.col, game.token)

    except ValueError:
        print("Valor no valido")
    except SamePlayerException:
        print("No puedes jugar con el mismo jugador")
    except MaxFichasException:
        print("No puedes poner mas fichas en dicha columna")
    except GameOverException:
        print("Te has excedido de la tabla")
    except NoLetterException:
        print("No has ingresado una letra valida")

    
    print_board(game.board)
 
    if game.win == 'Yes':
        print("Ganaste")
        return False
    return True

def print_board(board):
    rows = 8
    cols = 8
    content = [["-"] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            content[i][j] = board[i][j]
    print("  0 1 2 3 4 5 6 7")
    for i in range(rows):
        print(i, end=" ")
        for j in range(cols):
            print(content[i][j], end=" ")
        print()


 



if __name__ == "__main__":
    main()