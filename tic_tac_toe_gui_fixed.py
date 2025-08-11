"""
Tic-Tac-Toe AI Agent with GUI Interface
======================================

This module provides a graphical user interface for the Tic-Tac-Toe game
using Tkinter. The AI agent uses the same Minimax algorithm.
"""

import tkinter as tk
from tkinter import messagebox, ttk
import threading
import time
from tic_tac_toe_agent import TicTacToeGame, MinimaxAI


class TicTacToeGUI:
    """
    GUI version of the Tic-Tac-Toe game with AI opponent.
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("TIC TAC TOE - AI Agent")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        self.root.configure(bg='#0a0a0a')
        
        # Game components
        self.game = TicTacToeGame()
        self.ai = MinimaxAI(self.game.ai_player, self.game.human_player)
        
        # GUI components
        self.buttons = []
        self.status_label = None
        self.score_label = None
        
        # Game statistics
        self.wins = 0
        self.losses = 0
        self.draws = 0
        
        self.setup_gui()
    
    def setup_gui(self):
        """Set up the GUI components with neon-style design."""
        # Title with neon effect
        title_label = tk.Label(
            self.root, 
            text="TIC TAC TOE",
            font=("Arial", 24, "bold"),
            fg="#00ffff",
            bg="#0a0a0a",
            relief="flat"
        )
        title_label.pack(pady=15)
        
        # Subtitle
        subtitle_label = tk.Label(
            self.root,
            text="vs AI Agent",
            font=("Arial", 14),
            fg="#8888ff",
            bg="#0a0a0a"
        )
        subtitle_label.pack(pady=5)
        
        # Score display with neon styling
        self.score_label = tk.Label(
            self.root,
            text=f"Wins: {self.wins} | Losses: {self.losses} | Draws: {self.draws}",
            font=("Arial", 12, "bold"),
            fg="#00ff88",
            bg="#0a0a0a"
        )
        self.score_label.pack(pady=5)
        
        # Status display with neon styling
        self.status_label = tk.Label(
            self.root, 
            text="Your turn! Click any cell to make a move.",
            font=("Arial", 14),
            fg="#ffffff",
            bg="#0a0a0a"
        )
        self.status_label.pack(pady=10)
        
        # Game board frame with dark background
        board_frame = tk.Frame(self.root, bg="#0a0a0a")
        board_frame.pack(pady=20)
        
        # Create 3x3 grid of buttons with neon style
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(
                    board_frame,
                    text=" ",
                    font=("Arial", 36, "bold"),
                    width=3,
                    height=1,
                    command=lambda r=i, c=j: self.on_cell_click(r, c),
                    bg="#1a1a2e",
                    fg="#ffffff",
                    activebackground="#16213e",
                    activeforeground="#ffffff",
                    relief="flat",
                    borderwidth=2
                )
                button.grid(row=i, column=j, padx=3, pady=3)
                row.append(button)
            self.buttons.append(row)
        
        # Control buttons frame with dark theme
        control_frame = tk.Frame(self.root, bg="#0a0a0a")
        control_frame.pack(pady=20)
        
        # New game button with neon styling
        new_game_btn = tk.Button(
            control_frame,
            text="NEW GAME",
            font=("Arial", 12, "bold"),
            command=self.new_game,
            bg="#1a1a2e",
            fg="#00ffff",
            activebackground="#00ffff",
            activeforeground="#1a1a2e",
            relief="flat",
            borderwidth=2,
            width=12,
            height=2
        )
        new_game_btn.pack(side=tk.LEFT, padx=15)
        
        # Quit button with neon styling
        quit_btn = tk.Button(
            control_frame,
            text="QUIT",
            font=("Arial", 12, "bold"),
            command=self.root.quit,
            bg="#1a1a2e",
            fg="#ff4444",
            activebackground="#ff4444",
            activeforeground="#1a1a2e",
            relief="flat",
            borderwidth=2,
            width=12,
            height=2
        )
        quit_btn.pack(side=tk.LEFT, padx=15)
    
    def on_cell_click(self, row: int, col: int):
        """Handle cell click event."""
        # Only process if it's human's turn and game is not over
        if (self.game.current_player == self.game.human_player and 
            not self.game.is_game_over()[0]):
            
            if self.game.make_move(row, col, self.game.human_player):
                self.update_board()
                
                # Check if game is over after human move
                is_over, result = self.game.is_game_over()
                if is_over:
                    self.handle_game_end(result)
                else:
                    # Switch to AI turn
                    self.game.current_player = self.game.ai_player
                    self.status_label.config(text="AI is thinking...", fg="#ffaa00")
                    self.disable_board()
                    
                    # Use after() instead of threading to avoid issues
                    self.root.after(500, self.ai_move)
    
    def ai_move(self):
        """Handle AI move."""
        # Get AI move
        row, col = self.ai.get_best_move(self.game)
        
        # Make AI move
        self.game.make_move(row, col, self.game.ai_player)
        self.update_board()
        
        # Check if game is over after AI move
        is_over, result = self.game.is_game_over()
        if is_over:
            self.handle_game_end(result)
        else:
            # Switch back to human turn
            self.game.current_player = self.game.human_player
            self.status_label.config(text="Your turn! Click any cell to make a move.", fg="#ffffff")
            self.enable_board()
    
    def update_board(self):
        """Update the GUI board to reflect the current game state with neon effects."""
        for i in range(3):
            for j in range(3):
                cell_value = self.game.board[i][j]
                button = self.buttons[i][j]
                
                if cell_value == 'X':
                    # Neon blue X
                    button.config(
                        text='✕',
                        fg='#00aaff',
                        bg='#0f1419',
                        activebackground='#1a2332',
                        activeforeground='#00aaff',
                        relief="flat",
                        borderwidth=2
                    )
                elif cell_value == 'O':
                    # Neon red O
                    button.config(
                        text='◯',
                        fg='#ff2d55',
                        bg='#0f1419',
                        activebackground='#331a1a',
                        activeforeground='#ff2d55',
                        relief="flat",
                        borderwidth=2
                    )
                else:
                    # Empty cell
                    button.config(
                        text=' ',
                        fg='#ffffff',
                        bg='#1a1a2e',
                        activebackground='#16213e',
                        activeforeground='#ffffff',
                        relief="flat",
                        borderwidth=2
                    )
    
    def disable_board(self):
        """Disable all board buttons."""
        for row in self.buttons:
            for button in row:
                button.config(state='disabled')
    
    def enable_board(self):
        """Enable all empty board buttons."""
        for i in range(3):
            for j in range(3):
                if self.game.board[i][j] == ' ':
                    self.buttons[i][j].config(state='normal')
    
    def handle_game_end(self, result):
        """Handle the end of the game with enhanced visual feedback."""
        self.disable_board()
        
        if result == 'Draw':
            message = "It's a draw! Well played!"
            status_color = "#ffaa00"
            self.draws += 1
        elif result == self.game.human_player:
            message = "🎉 YOU WIN! 🎉"
            status_color = "#00ff88"
            self.wins += 1
        else:
            message = "AI WINS! Try again!"
            status_color = "#ff4444"
            self.losses += 1
        
        self.status_label.config(text=message, fg=status_color)
        self.update_score_display()
        
        # Show message box with result
        messagebox.showinfo("Game Over", message + "\n\nClick 'NEW GAME' to play again!")
    
    def update_score_display(self):
        """Update the score display with neon styling."""
        self.score_label.config(
            text=f"Wins: {self.wins} | Losses: {self.losses} | Draws: {self.draws}",
            fg="#00ff88"
        )
    
    def new_game(self):
        """Start a new game."""
        # Create a new game instance
        self.game = TicTacToeGame()
        self.ai = MinimaxAI(self.game.ai_player, self.game.human_player)
        
        # Reset board display with neon styling
        for i in range(3):
            for j in range(3):
                button = self.buttons[i][j]
                button.config(
                    text=' ', 
                    fg='#ffffff', 
                    bg='#1a1a2e',
                    activebackground='#16213e',
                    activeforeground='#ffffff',
                    state='normal',
                    relief="flat",
                    borderwidth=2
                )
        
        self.status_label.config(
            text="Your turn! Click any cell to make a move.",
            fg="#ffffff"
        )
    
    def run(self):
        """Start the GUI application."""
        self.root.mainloop()


def main():
    """Main function to start the GUI version."""
    app = TicTacToeGUI()
    app.run()


if __name__ == "__main__":
    main()
