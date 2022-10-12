  
import unittest
from unittest.mock import patch
from gameFEND import main
#from gameFEND import Cuatroenlinea


@patch('random.choice', return_value=1)
@patch("builtins.print")
@patch("builtins.input")

class Test4InLine(unittest.TestCase):

    def test_q_exit(self, patched_input, patched_print, *args):
        patched_input.return_value = "q"
        main()
        self.assertEqual(patched_print.call_count, 0)
        patched_input.assert_called_once()

    

    def test_1(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["1", "q"]
        main()
        
        self.assertEqual(patched_print.call_count, 84)
        patched_input.assert_called_with("INGRESE una columna: ")

    #def test_exceed(self, patched_input, patched_print, *args):
    #    
    #    with patch ('builtins.input',return_value=9):
    #        with patch ('builtins.print') as patched_print:
    #            
    #            patched_print.assert_called_with("No se pueden ingresar mas fichas en esta columna",'\n' 
    #                                                'Te has excedido de la tabla', '\n'
    #                                                    '  0 1 2 3 4 5 6 7 ', '\n'
    #                                                    '0 - - - - - - - - '
    #                                                    '1 - - - - - - - - '
    #                                                    '2 - - - - - - - - '
    #                                                    '3 - - - - - - - - '
    #                                                    '4 - - - - - - - - '
    #                                                    '5 - - - - - - - - '
    #                                                    '6 - - - - - - - - '
    #                                                    '7 - - - - - - - - ')
#    def test_exceed45(self, patched_input, patched_print, *args):
#        patched_input.side_effect = ["9"]
#        main()
        
        
        #patched_input.assert_called_with("INGRESE una columna: ")

        
#        patched_input.assert_called_with("No se pueden ingresar mas fichas en esta columna",'\n' 
#                                                    'Te has excedido de la tabla', '\n'
#                                                        '  0 1 2 3 4 5 6 7 ', '\n'
#                                                        '0 - - - - - - - - '
#                                                        '1 - - - - - - - - '
#                                                        '2 - - - - - - - - '
#                                                        '3 - - - - - - - - '
#                                                        '4 - - - - - - - - '
#                                                        '5 - - - - - - - - '
#                                                        '6 - - - - - - - - '
#                                                        '7 - - - - - - - - ')'''
    
#    #def test_exceed2(self, patched_input, patched_print, *args):
#    #    machine= Cuatroenlinea()
#    #    with patch ('builtins.input',return_value=9):
    #        with patch ('builtins.print') as patched_print:
    #            machine.main()
    #            patched_print.assert_called_with("No se pueden ingresar mas fichas en esta columna",'\n', machine.board, '\n',("Jugada: ",machine.jugada), '\n',machine.player, '\n',machine.win)
               

    def test_2(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["1", "2","3","4","q"]
        main()
        self.assertEqual(patched_print.call_count, 336)
        patched_input.assert_called_with("INGRESE una columna: ")
    

    def test_overflow(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["9", "q"]
        main()
        self.assertEqual(patched_print.call_args_list[3][0][0],0)
    
    def test_max_fichas(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["1", "1", "1", "1", "1", "1", "1", "1", "1", "q"]
        main()
        self.assertEqual(patched_print.call_args_list[3][0][0],'-')





        
    
    





    

if __name__ == '__main__':
    unittest.main()