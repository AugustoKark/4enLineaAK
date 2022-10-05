import unittest
from game import Cuatroenlinea
from exception import *




class TestCuatroenlinea(unittest.TestCase):
    def test_create_board(self):
        machine = Cuatroenlinea()
        self.assertEqual(len(machine.board), 8)
        self.assertEqual(len(machine.board[0]), 8)
    
    def test_board_view(self):
        machine = Cuatroenlinea()
        self.assertEqual(machine.board ,
        [['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-']])

    def test_first_move(self):
        machine = Cuatroenlinea()
        machine.set(1,'0')
        self.assertEqual(machine.board ,
        [['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '0', '-', '-', '-', '-', '-', '-']])
    

    def test_first_move0(self):
        machine = Cuatroenlinea()
        machine.set(0,'0')
        self.assertEqual(machine.jugada,1)
        self.assertEqual(machine.win,'No')
        self.assertEqual(machine.board ,
        [['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['0', '-', '-', '-', '-', '-', '-', '-']])


    def test_second_move1(self):
        machine = Cuatroenlinea()
        machine.set(0,'0')
        self.assertEqual(machine.jugada,1)
        machine.set(0,'X')
        self.assertEqual(machine.jugada,2)
        self.assertEqual(machine.win,'No')

    def test_same_player(self):
        machine = Cuatroenlinea()
        machine.set(0,'0')
        self.assertEqual(machine.jugada,1)
        try:
            machine.set(1,'0')
        except SamePlayerException:
                pass   
        self.assertEqual(machine.jugada,1)
        self.assertEqual(machine.win,'No')
        self.assertEqual(machine.board ,
        [['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['0', '-', '-', '-', '-', '-', '-', '-']])

        

    def test_second_movex1(self):
        machine = Cuatroenlinea()
        machine.set(0,'0')
        machine.set(0,'X')
        self.assertEqual(machine.jugada,2)
        self.assertEqual(machine.win,'No')
        self.assertEqual(machine.board ,
        [['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['X', '-', '-', '-', '-', '-', '-', '-'], 
        ['0', '-', '-', '-', '-', '-', '-', '-']])

    
    def test_third_move0(self):
        machine = Cuatroenlinea()
        machine.set(0,'0')
        machine.set(0,'X')
        machine.set(0,'0')
        self.assertEqual(machine.jugada,3)
        self.assertEqual(machine.win,'No')
        self.assertEqual(machine.board ,
        [['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['0', '-', '-', '-', '-', '-', '-', '-'], 
        ['X', '-', '-', '-', '-', '-', '-', '-'], 
        ['0', '-', '-', '-', '-', '-', '-', '-']])

    def test_fourth_moveX2(self):
        machine = Cuatroenlinea()
        machine.set(0,'0')
        machine.set(0,'X')
        machine.set(0,'0')
        machine.set(1,'X')
        self.assertEqual(machine.jugada,4)
        self.assertEqual(machine.win,'No')
        self.assertEqual(machine.board ,
        [['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['0', '-', '-', '-', '-', '-', '-', '-'], 
        ['X', '-', '-', '-', '-', '-', '-', '-'], 
        ['0', 'X', '-', '-', '-', '-', '-', '-']])

    def test_fiveth_moveX3(self):
        machine = Cuatroenlinea()
        machine.set(0,'0')
        machine.set(0,'X')
        machine.set(0,'0')
        machine.set(1,'X')
        machine.set(4,'0')
        self.assertEqual(machine.jugada,5)
        self.assertEqual(machine.win,'No')
        self.assertEqual(machine.board ,
        [['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['0', '-', '-', '-', '-', '-', '-', '-'], 
        ['X', '-', '-', '-', '-', '-', '-', '-'], 
        ['0', 'X', '-', '-', '0', '-', '-', '-']])

    def test_error_sameplace(self):
        machine = Cuatroenlinea()
        machine.set(0,'0')
        machine.set(0,'X')
        machine.set(0,'0')
        machine.set(0,'X')
        machine.set(0,'0')
        machine.set(0,'X')
        machine.set(0,'0')
        machine.set(0,'X')
        try:
            machine.set(0,'0')
        except MaxFichasException:
            pass
        self.assertEqual(machine.jugada,8)
        self.assertEqual(machine.win,'No')
        self.assertEqual(machine.board ,
        [['X', '-', '-', '-', '-', '-', '-', '-'],
        ['0', '-', '-', '-', '-', '-', '-', '-'], 
        ['X', '-', '-', '-', '-', '-', '-', '-'], 
        ['0', '-', '-', '-', '-', '-', '-', '-'], 
        ['X', '-', '-', '-', '-', '-', '-', '-'], 
        ['0', '-', '-', '-', '-', '-', '-', '-'], 
        ['X', '-', '-', '-', '-', '-', '-', '-'], 
        ['0', '-', '-', '-', '-', '-', '-', '-']]) 

    def test_victory(self):
        machine = Cuatroenlinea()
        machine.set(0,'0')
        machine.set(0,'X')
        machine.set(1,'0')
        machine.set(0,'X')
        machine.set(2,'0')
        machine.set(0,'X')
        machine.set(3,'0')
        self.assertEqual(machine.jugada,7)
        self.assertEqual(machine.win,'Yes')
        self.assertEqual(machine.board ,
        [['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['X', '-', '-', '-', '-', '-', '-', '-'], 
        ['X', '-', '-', '-', '-', '-', '-', '-'], 
        ['X', '-', '-', '-', '-', '-', '-', '-'], 
        ['0', '0', '0', '0', '-', '-', '-', '-']]) 

    def test_victoryver(self):
        machine = Cuatroenlinea()
        machine.set(0,'0')
        machine.set(0,'X')
        machine.set(1,'0')
        machine.set(0,'X')
        machine.set(2,'0')
        machine.set(0,'X')
        machine.set(5,'0')
        machine.set(0,'X')

        self.assertEqual(machine.jugada,8)
        self.assertEqual(machine.win,'Yes')
        self.assertEqual(machine.board ,
        [['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['X', '-', '-', '-', '-', '-', '-', '-'], 
        ['X', '-', '-', '-', '-', '-', '-', '-'], 
        ['X', '-', '-', '-', '-', '-', '-', '-'], 
        ['X', '-', '-', '-', '-', '-', '-', '-'], 
        ['0', '0', '0', '-', '-', '0', '-', '-']])


    def test_victoryincl(self):
        machine = Cuatroenlinea()
        machine.set(0,'0')
        machine.set(1,'X')
        machine.set(1,'0')
        machine.set(0,'X')
        machine.set(0,'0')
        machine.set(1,'X')
        machine.set(2,'0')
        machine.set(2,'X')
        machine.set(4,'0')
        machine.set(3,'X')
        machine.set(5,'0')
        machine.set(0,'X')
        self.assertEqual(machine.jugada,12)
        self.assertEqual(machine.win,'Yes')
        self.assertEqual(machine.board ,
        [['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['X', '-', '-', '-', '-', '-', '-', '-'], 
        ['0', 'X', '-', '-', '-', '-', '-', '-'], 
        ['X', '0', 'X', '-', '-', '-', '-', '-'], 
        ['0', 'X', '0', 'X', '0', '0', '-', '-']])

    def test_victoryincl2(self):
        machine = Cuatroenlinea()
        machine.set(7,'0')
        machine.set(6,'X')
        machine.set(6,'0')
        machine.set(7,'X')
        machine.set(7,'0')
        machine.set(7,'X')
        machine.set(5,'0')
        machine.set(6,'X')
        machine.set(3,'0')
        machine.set(5,'X')
        machine.set(3,'0')
        machine.set(4,'X')
        self.assertEqual(machine.jugada,12)
        self.assertEqual(machine.win,'Yes')
        self.assertEqual(machine.board ,
        [['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', '-'], 
        ['-', '-', '-', '-', '-', '-', '-', 'X'], 
        ['-', '-', '-', '-', '-', '-', 'X', '0'], 
        ['-', '-', '-', '0', '-', 'X', '0', 'X'], 
        ['-', '-', '-', '0', 'X', '0', 'X', '0']])  



if __name__ == '__main__':
       
        unittest.main()

