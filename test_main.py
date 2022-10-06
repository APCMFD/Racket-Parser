import unittest
from main import GAME_GUI

class Test_SOS_GUI(unittest.TestCase):
  
    def setUp(self):
        self.game = GAME_GUI(3, True)
        self.game.gameboard_GUI()
        
    def tearDown(self):
        return None
      
    def test_set_r_turn(self):
        self.game.set_r_turn()
        return self.assertEqual(self.game.current_turn.get(), self.game.R_TURN)
      
    def test_set_b_turn(self):
        self.game.set_b_turn()
        return self.assertEqual(self.game.current_turn.get(), self.game.B_TURN)
      
    def test_r_player_option(self):
        self.game.red_player.option.set('S')
        return self.assertEqual(self.game.red_player.option.get(), 'S')
      
    def test_b_player_option(self):
        self.game.blue_player.option.set('S')
        return self.assertEqual(self.game.blue_player.option.get(), 'S')
      
    def test_red_move(self):
        self.game.start_simple()
        self.game.set_r_turn()
        self.game.red_player.option.set('S')
        self.game.move(0,1)
        return self.assertEqual(self.game.board[0][1]['text'], self.game.red_player.option.get())

    def test_blue_move(self):
        self.game.start_simple_game()
        self.game.set_b_turn()
        self.game.blue_player.option.set('O')
        self.game.move(0,1)
        return self.assertEqual(self.game.board[0][1]['text'], self.game.blue_player.option.get())

    def test_invalid_move(self):
        self.game.start_simple()
        self.game.set_r_turn()
        self.game.red_player.option.set('S')
        self.game.move(2,2)
        
        # blue tries to make move in spot occupied with 'O' from red's turn
        self.game.blue_player.option.set('O')
        self.game.move(2,2)

        return self.assertEqual(self.game.board[2][2]['text'], 'S')

    def test_simple_game(self):
        self.game.start_simple()
        return self.assertEqual(self.game.gametype, self.game.SIMPLE_GAME)
      
    def test_general_game(self):
        self.game.start_general_game()
        return self.assertEqual(self.game.gametype, self.game.GENERAL_GAME)
        
    def test_check_if_board_not_full(self):
        return self.assertEqual(self.game.full_board_check(), False)
      
    def test_check_if_board_full(self):
        for row in range(self.game.row_num):
            for col in range(self.game.col_num):
                self.game.board[row][col]['text'] = 'S'
        return self.assertEqual(self.game.full_board_check(), True)
      
if __name__ == '__main__':
    start = Test_SOS_GUI()
    start.setUp()
    start.test_set_r_turn()
    start.tearDown()
    start.setUp()
    start.test_set_b_turn()
    start.tearDown()
    start.setUp()
    start.test_r_player_option()
    start.tearDown()
    start.setUp()
    start.test_b_player_option()
    start.tearDown()
    start.setUp()
    start.test_red_move()
    start.tearDown()
    start.setUp()
    start.test_blue_move()
    start.tearDown()
    start.setUp()
    start.test_invalid_move()
    start.tearDown()
    start.setUp()
    start.test_simple_game()
    start.tearDown()
    start.setUp()
    start.test_general_game()
    start.tearDown()
    start.setUp()
    start.test_check_if_board_not_full()
    start.tearDown()
    start.setUp()
    start.test_check_if_board_full()
    start.tearDown()

