"""
Tic-Tac-Toe AI Agent using Minimax Algorithm
============================================

This module implements a complete Tic-Tac-Toe game with an AI agent
that uses the Minimax algorithm to make optimal moves.
"""

import math
import copy
from typing import List, Tuple, Optional


class TicTacToeGame:
    """
    Main game class that handles the Tic-Tac-Toe board and game logic.
    """
    
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # Human player starts
        self.ai_player = 'O'
        self.human_player = 'X'
    
    def display_board(self):
        """Display the current board state in a formatted way."""
        print("\n   0   1   2")
        for i, row in enumerate(self.board):
            print(f"{i}  {row[0]} | {row[1]} | {row[2]}")
            if i < 2:
                print("  -----------")
        print()
    
    def is_valid_move(self, row: int, col: int) -> bool:
        """Check if a move is valid (within bounds and cell is empty)."""
        return (0 <= row < 3 and 0 <= col < 3 and 
                self.board[row][col] == ' ')
    
    def make_move(self, row: int, col: int, player: str) -> bool:
        """Make a move on the board if valid."""
        if self.is_valid_move(row, col):
            self.board[row][col] = player
            return True
        return False
    
    def check_winner(self) -> Optional[str]:
        """Check if there's a winner on the board."""
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        # Check columns
        for col in range(3):
            if (self.board[0][col] == self.board[1][col] == 
                self.board[2][col] != ' '):
                return self.board[0][col]
        
        # Check diagonals
        if (self.board[0][0] == self.board[1][1] == 
            self.board[2][2] != ' '):
            return self.board[0][0]
        
        if (self.board[0][2] == self.board[1][1] == 
            self.board[2][0] != ' '):
            return self.board[0][2]
        
        return None
    
    def is_board_full(self) -> bool:
        """Check if the board is full (draw condition)."""
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True
    
    def is_game_over(self) -> Tuple[bool, Optional[str]]:
        """Check if the game is over and return winner if any."""
        winner = self.check_winner()
        if winner:
            return True, winner
        elif self.is_board_full():
            return True, 'Draw'
        return False, None
    
    def get_available_moves(self) -> List[Tuple[int, int]]:
        """Get all available moves on the board."""
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    moves.append((i, j))
        return moves


class MinimaxAI:
    """
    AI Agent that uses the Minimax algorithm to play Tic-Tac-Toe optimally.
    """
    
    def __init__(self, ai_player: str, human_player: str):
        self.ai_player = ai_player
        self.human_player = human_player
    
    def evaluate_board(self, game: TicTacToeGame) -> int:
        """
        Evaluate the current board state.
        Returns: +10 if AI wins, -10 if human wins, 0 for draw/ongoing
        """
        winner = game.check_winner()
        if winner == self.ai_player:
            return 10
        elif winner == self.human_player:
            return -10
        else:
            return 0
    
    def minimax(self, game: TicTacToeGame, depth: int, 
                is_maximizing: bool, alpha: int = -math.inf, 
                beta: int = math.inf) -> int:
        """
        Minimax algorithm with alpha-beta pruning for optimal move selection.
        
        Args:
            game: Current game state
            depth: Current depth in the game tree
            is_maximizing: True if AI's turn (maximizing), False if human's turn
            alpha: Alpha value for pruning
            beta: Beta value for pruning
        
        Returns:
            The best score achievable from this position
        """
        # Base case: if game is over, return the evaluation
        is_over, result = game.is_game_over()
        if is_over:
            score = self.evaluate_board(game)
            # Adjust score based on depth to prefer faster wins/slower losses
            if score > 0:
                return score - depth
            elif score < 0:
                return score + depth
            else:
                return 0
        
        if is_maximizing:
            # AI's turn - maximize the score
            max_eval = -math.inf
            for row, col in game.get_available_moves():
                # Make the move
                game.board[row][col] = self.ai_player
                
                # Recursively evaluate
                eval_score = self.minimax(game, depth + 1, False, alpha, beta)
                
                # Undo the move
                game.board[row][col] = ' '
                
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                
                # Alpha-beta pruning
                if beta <= alpha:
                    break
            
            return max_eval
        else:
            # Human's turn - minimize the score
            min_eval = math.inf
            for row, col in game.get_available_moves():
                # Make the move
                game.board[row][col] = self.human_player
                
                # Recursively evaluate
                eval_score = self.minimax(game, depth + 1, True, alpha, beta)
                
                # Undo the move
                game.board[row][col] = ' '
                
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                
                # Alpha-beta pruning
                if beta <= alpha:
                    break
            
            return min_eval
    
    def get_best_move(self, game: TicTacToeGame) -> Tuple[int, int]:
        """
        Find the best move for the AI using the Minimax algorithm.
        
        Returns:
            Tuple of (row, col) representing the best move
        """
        best_score = -math.inf
        best_move = None
        
        print("AI is thinking...")
        
        for row, col in game.get_available_moves():
            # Make the move
            game.board[row][col] = self.ai_player
            
            # Evaluate this move
            score = self.minimax(game, 0, False)
            
            # Undo the move
            game.board[row][col] = ' '
            
            # Update best move if this is better
            if score > best_score:
                best_score = score
                best_move = (row, col)
        
        return best_move


class GameController:
    """
    Main controller that orchestrates the game flow between human and AI.
    """
    
    def __init__(self):
        self.game = TicTacToeGame()
        self.ai = MinimaxAI(self.game.ai_player, self.game.human_player)
    
    def get_human_move(self) -> Tuple[int, int]:
        """Get and validate human player's move."""
        while True:
            try:
                print(f"Your turn (playing as {self.game.human_player})")
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                
                if self.game.is_valid_move(row, col):
                    return row, col
                else:
                    print("Invalid move! Cell is either occupied or out of bounds.")
            except ValueError:
                print("Please enter valid numbers (0-2).")
    
    def play_game(self):
        """Main game loop."""
        print("=" * 50)
        print("Welcome to Tic-Tac-Toe vs AI!")
        print("=" * 50)
        print(f"You are {self.game.human_player}, AI is {self.game.ai_player}")
        print("Enter coordinates as row, column (0-2)")
        
        self.game.display_board()
        
        while True:
            # Human player's turn
            if self.game.current_player == self.game.human_player:
                row, col = self.get_human_move()
                self.game.make_move(row, col, self.game.human_player)
                self.game.current_player = self.game.ai_player
            
            # AI player's turn
            else:
                row, col = self.ai.get_best_move(self.game)
                print(f"AI plays at position ({row}, {col})")
                self.game.make_move(row, col, self.game.ai_player)
                self.game.current_player = self.game.human_player
            
            # Display board after each move
            self.game.display_board()
            
            # Check if game is over
            is_over, result = self.game.is_game_over()
            if is_over:
                if result == 'Draw':
                    print("It's a draw! Well played!")
                elif result == self.game.human_player:
                    print("Congratulations! You won!")
                else:
                    print("AI wins! Better luck next time!")
                break
        
        # Ask if player wants to play again
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again == 'y':
            self.__init__()  # Reset the game
            self.play_game()


def main():
    """Main function to start the game."""
    controller = GameController()
    controller.play_game()


if __name__ == "__main__":
    main()
