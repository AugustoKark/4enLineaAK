  
import unittest
from unittest.mock import patch
from gameFEND import main


@patch('random.choice', return_value=1)
@patch("builtins.print")
@patch("builtins.input")

class Test4InLine(unittest.TestCase):

    def test_q_exit(self, patched_input, patched_print, *args):
        patched_input.return_value = "q"
        main()
        self.assertEqual(patched_print.call_count, 0)
        patched_input.assert_called_once()

    

if __name__ == '__main__':
    unittest.main()