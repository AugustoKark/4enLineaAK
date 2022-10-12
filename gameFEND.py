from game import Cuatroenlinea
from exception import *

def main():
    game = Cuatroenlinea()
    
    game.jugada=0
    playing = True
    
    while playing:
        playing = play(game)


def play(game):
    try:
        colum_ingreso =(input("INGRESE una columna: "))
        if colum_ingreso=="q":
            return False
        
        if game.jugada ==1:
            lettera='X'
        if game.jugada %2==0:
            lettera='O'
        else:
            lettera='X'


        
        
        game.set(int(colum_ingreso),lettera)
        print_board(game.board)
        print("Jugada: ",game.jugada)

        if game.win == 'Yes':
            print("Player {} wins!".format(game.player))
            return False
        print(game.player)
        print(game.win)
        return True
    except MaxFichasException:
        print("No se pueden ingresar mas fichas en esta columna")
        return True

        
        

    except ValueError:
        print("Valor no valido")
        
    except SamePlayerException:
        print("No puedes jugar con el mismo jugador")
        
    except MaxFichasException:
        print("No puedes poner mas fichas en dicha columna")
        
    except ExceedTableException:
        print("Te has excedido de la tabla")
        
    

    
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