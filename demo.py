"""
Demo Script for Tic-Tac-Toe AI Agent
====================================

This script demonstrates both the console and GUI versions of the 
Tic-Tac-Toe AI agent.
"""

import sys
import os

def show_menu():
    """Display the main menu."""
    print("=" * 50)
    print("Tic-Tac-Toe AI Agent Demo")
    print("=" * 50)
    print("1. Play Console Version")
    print("2. Play GUI Version")
    print("3. Show AI Algorithm Explanation")
    print("4. Exit")
    print("=" * 50)

def show_algorithm_explanation():
    """Explain the Minimax algorithm used by the AI."""
    print("\n" + "=" * 60)
    print("MINIMAX ALGORITHM EXPLANATION")
    print("=" * 60)
    print("""
The AI agent uses the Minimax algorithm with alpha-beta pruning 
to play optimally. Here's how it works:

1. GAME TREE EXPLORATION:
   - The algorithm explores all possible future game states
   - It simulates every possible move for both players
   - Creates a tree of all possible game outcomes

2. EVALUATION FUNCTION:
   - +10 points: AI wins
   - -10 points: Human wins
   - 0 points: Draw or ongoing game
   - Depth adjustment: Prefers faster wins and slower losses

3. MINIMAX STRATEGY:
   - AI (Maximizing player): Chooses moves that maximize score
   - Human (Minimizing player): Assumes human plays optimally to minimize AI score
   - Recursively evaluates all possibilities

4. ALPHA-BETA PRUNING:
   - Optimization technique to reduce computation
   - Eliminates branches that won't affect the final decision
   - Makes the algorithm much faster without losing accuracy

5. RESULT:
   - The AI will never lose if it goes first
   - At best, human can achieve a draw with perfect play
   - The AI adapts to human mistakes to win when possible

DIFFICULTY LEVELS (GUI version):
- Easy: Random moves
- Medium: 70% optimal moves, 30% random
- Hard: Always optimal moves (unbeatable)
    """)
    print("=" * 60)

def main():
    """Main demo function."""
    while True:
        show_menu()
        
        try:
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == '1':
                print("\nStarting Console Version...")
                from tic_tac_toe_agent import main as console_main
                console_main()
            
            elif choice == '2':
                print("\nStarting GUI Version...")
                try:
                    from tic_tac_toe_gui import main as gui_main
                    gui_main()
                except ImportError as e:
                    print(f"Error: {e}")
                    print("Make sure tkinter is installed (usually comes with Python)")
            
            elif choice == '3':
                show_algorithm_explanation()
                input("\nPress Enter to continue...")
            
            elif choice == '4':
                print("Thanks for playing! Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
        
        except KeyboardInterrupt:
            print("\n\nExiting... Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
