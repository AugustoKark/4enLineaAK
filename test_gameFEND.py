import unittest
from unittest.mock import patch
from gameFEND import *
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
    

    def test_2(self, patched_input, patched_print, *args):
        patched_input.side_effect = ["1", "2","3","4","q"]
        main()
        self.assertEqual(patched_print.call_count, 336)
        patched_input.assert_called_with("INGRESE una columna: ")

    
    def test_max_fichas(self, patched_input, patched_print, *args):
        try:
            patched_input.side_effect = ["1", "1", "1", "1", "1", "1", "1", "1", "1", "q"]
            main()
        except:
            self.fail("No puedes poner mas fichas en dicha columna")
    
    def test_max_fichas1(self, patched_input, patched_print, *args):
            patched_input.side_effect = ["1", "1", "1", "1", "1", "1", "1", "1", "1", "q"]
            main()
            AssertionError("No puedes poner mas fichas en dicha columna")

    def test_overflow2(self, patched_input, patched_print, *args):
            patched_input.side_effect = ["8", "q"]
            main()
            AssertionError("Te has excedido de la tabla")
    
    def test_ValueError(self, patched_input, patched_print, *args):
        try:
            patched_input.side_effect = ["a"]
            main()
        except:
            AssertionError("Valor no valido")

            


        

    

    
    


        





        
    
    





    

if __name__ == '__main__':
    unittest.main()