"""
Test Suite for Tic-Tac-Toe AI Agent
===================================

This module contains unit tests to verify the correctness of the 
Tic-Tac-Toe AI agent implementation.
"""

import unittest
from tic_tac_toe_agent import TicTacToeGame, MinimaxAI


class TestTicTacToeGame(unittest.TestCase):
    """Test cases for the TicTacToeGame class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.game = TicTacToeGame()
    
    def test_initial_board(self):
        """Test that the board is properly initialized."""
        for row in self.game.board:
            for cell in row:
                self.assertEqual(cell, ' ')
    
    def test_valid_move(self):
        """Test making valid moves."""
        self.assertTrue(self.game.make_move(0, 0, 'X'))
        self.assertEqual(self.game.board[0][0], 'X')
    
    def test_invalid_move(self):
        """Test invalid moves."""
        # Make a move first
        self.game.make_move(0, 0, 'X')
        
        # Try to make a move in the same position
        self.assertFalse(self.game.make_move(0, 0, 'O'))
        
        # Try to make a move out of bounds
        self.assertFalse(self.game.make_move(3, 3, 'O'))
        self.assertFalse(self.game.make_move(-1, 0, 'O'))
    
    def test_horizontal_win(self):
        """Test horizontal win detection."""
        # Create winning condition
        self.game.board = [
            ['X', 'X', 'X'],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.assertEqual(self.game.check_winner(), 'X')
    
    def test_vertical_win(self):
        """Test vertical win detection."""
        # Create winning condition
        self.game.board = [
            ['O', ' ', ' '],
            ['O', ' ', ' '],
            ['O', ' ', ' ']
        ]
        self.assertEqual(self.game.check_winner(), 'O')
    
    def test_diagonal_win(self):
        """Test diagonal win detection."""
        # Create winning condition
        self.game.board = [
            ['X', ' ', ' '],
            [' ', 'X', ' '],
            [' ', ' ', 'X']
        ]
        self.assertEqual(self.game.check_winner(), 'X')
        
        # Test other diagonal
        self.game.board = [
            [' ', ' ', 'O'],
            [' ', 'O', ' '],
            ['O', ' ', ' ']
        ]
        self.assertEqual(self.game.check_winner(), 'O')
    
    def test_no_winner(self):
        """Test when there's no winner."""
        self.game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', ' ']
        ]
        self.assertIsNone(self.game.check_winner())
    
    def test_board_full(self):
        """Test board full detection."""
        self.game.board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        self.assertTrue(self.game.is_board_full())
    
    def test_available_moves(self):
        """Test getting available moves."""
        self.game.board = [
            ['X', ' ', ' '],
            [' ', 'O', ' '],
            [' ', ' ', ' ']
        ]
        available = self.game.get_available_moves()
        expected = [(0,1), (0,2), (1,0), (1,2), (2,0), (2,1), (2,2)]
        self.assertEqual(sorted(available), sorted(expected))


class TestMinimaxAI(unittest.TestCase):
    """Test cases for the MinimaxAI class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.game = TicTacToeGame()
        self.ai = MinimaxAI('O', 'X')
    
    def test_ai_blocks_winning_move(self):
        """Test that AI blocks human's winning move."""
        # Human has two X's in a row
        self.game.board = [
            ['X', 'X', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        
        move = self.ai.get_best_move(self.game)
        # AI should block at (0, 2)
        self.assertEqual(move, (0, 2))
    
    def test_ai_takes_winning_move(self):
        """Test that AI takes a winning move when available."""
        # AI has two O's in a row
        self.game.board = [
            ['O', 'O', ' '],
            ['X', ' ', ' '],
            ['X', ' ', ' ']
        ]
        
        move = self.ai.get_best_move(self.game)
        # AI should win at (0, 2)
        self.assertEqual(move, (0, 2))
    
    def test_ai_center_preference(self):
        """Test that AI prefers center when starting."""
        # Empty board, AI should prefer center
        move = self.ai.get_best_move(self.game)
        # Center is usually the best opening move
        self.assertEqual(move, (1, 1))
    
    def test_evaluation_function(self):
        """Test the board evaluation function."""
        # AI wins
        self.game.board = [
            ['O', 'O', 'O'],
            ['X', 'X', ' '],
            [' ', ' ', ' ']
        ]
        self.assertEqual(self.ai.evaluate_board(self.game), 10)
        
        # Human wins
        self.game.board = [
            ['X', 'X', 'X'],
            ['O', 'O', ' '],
            [' ', ' ', ' ']
        ]
        self.assertEqual(self.ai.evaluate_board(self.game), -10)
        
        # No winner
        self.game.board = [
            ['X', 'O', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.assertEqual(self.ai.evaluate_board(self.game), 0)


class TestGameIntegration(unittest.TestCase):
    """Integration tests for the complete game."""
    
    def test_complete_game_scenario(self):
        """Test a complete game scenario."""
        game = TicTacToeGame()
        ai = MinimaxAI('O', 'X')
        
        # Simulate a game where human goes first
        moves = []
        
        # Human move
        game.make_move(0, 0, 'X')
        moves.append("Human: (0,0)")
        
        # AI move
        ai_move = ai.get_best_move(game)
        game.make_move(ai_move[0], ai_move[1], 'O')
        moves.append(f"AI: {ai_move}")
        
        # Continue until game ends
        while not game.is_game_over()[0]:
            # For testing, we'll make random human moves
            available = game.get_available_moves()
            if available:
                import random
                human_move = random.choice(available)
                game.make_move(human_move[0], human_move[1], 'X')
                moves.append(f"Human: {human_move}")
                
                if not game.is_game_over()[0]:
                    ai_move = ai.get_best_move(game)
                    game.make_move(ai_move[0], ai_move[1], 'O')
                    moves.append(f"AI: {ai_move}")
        
        # Game should end properly
        is_over, result = game.is_game_over()
        self.assertTrue(is_over)
        self.assertIn(result, ['X', 'O', 'Draw'])
        
        print(f"\nGame moves: {moves}")
        print(f"Result: {result}")


def run_performance_test():
    """Test the performance of the AI agent."""
    import time
    
    print("\n" + "="*50)
    print("PERFORMANCE TEST")
    print("="*50)
    
    game = TicTacToeGame()
    ai = MinimaxAI('O', 'X')
    
    # Test AI decision time for different board states
    test_boards = [
        # Empty board
        [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']],
        # One move made
        [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']],
        # Mid-game
        [['X', 'O', ' '], [' ', 'X', ' '], [' ', ' ', ' ']],
        # Near end-game
        [['X', 'O', 'X'], ['O', 'X', 'O'], [' ', ' ', ' ']],
    ]
    
    for i, board in enumerate(test_boards):
        game.board = board
        start_time = time.time()
        move = ai.get_best_move(game)
        end_time = time.time()
        
        print(f"Test {i+1}: AI decision time = {end_time - start_time:.4f} seconds")
        print(f"         Best move: {move}")


if __name__ == "__main__":
    print("Running Tic-Tac-Toe AI Agent Tests...")
    print("="*50)
    
    # Run unit tests
    unittest.main(verbosity=2, exit=False)
    
    # Run performance test
    run_performance_test()
    
    print("\nAll tests completed!")
