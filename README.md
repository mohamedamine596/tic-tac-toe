# Tic-Tac-Toe AI Agent 🎮✨

A complete implementation of a Tic-Tac-Toe AI agent using the Minimax algorithm with alpha-beta pruning. Features a stunning neon-styled GUI and unbeatable AI that plays optimally.

## Features

- **Unbeatable AI**: Uses Minimax algorithm with alpha-beta pruning
- **Neon-Styled GUI**: Beautiful cyberpunk-inspired dark theme with glowing effects
- **Multiple Interfaces**: Console and GUI versions available
- **Difficulty Levels**: Easy, Medium, and Hard modes in GUI version
- **Performance Optimized**: Alpha-beta pruning for faster decisions
- **Complete Test Suite**: Unit tests and integration tests
- **Score Tracking**: Keep track of wins, losses, and draws
- **Visual Effects**: Hover animations, neon glows, and winning celebrations

## Project Structure

```
agent/
├── tic_tac_toe_agent.py    # Core game logic and AI implementation
├── tic_tac_toe_gui.py      # GUI interface using Tkinter
├── demo.py                 # Demo script with menu options
├── test_agent.py           # Comprehensive test suite
└── README.md               # This file
```

## Files Description

### `tic_tac_toe_agent.py`
Core implementation containing:
- `TicTacToeGame`: Main game logic and board management
- `MinimaxAI`: AI agent using Minimax algorithm
- `GameController`: Console interface controller

### `tic_tac_toe_gui.py`
GUI implementation featuring:
- **Neon-styled interface** with cyberpunk dark theme
- **Glowing X's and O's** with blue and red neon effects
- **Hover animations** and visual feedback
- **Difficulty level selection** with dark-themed controls
- **Score tracking** with neon styling
- **Threaded AI processing** to prevent GUI freezing
- **Winning celebrations** with flash effects

### `demo.py`
Main demo script offering:
- Menu-driven interface
- Access to both console and GUI versions
- Algorithm explanation
- Easy testing of different modes

### `test_agent.py`
Comprehensive testing including:
- Unit tests for game logic
- AI behavior verification
- Performance benchmarking
- Integration tests

## Screenshots & Design

### Neon-Styled GUI
The GUI features a stunning cyberpunk-inspired design:
- **Dark Background**: Deep black (#0a0a0a) for that futuristic feel
- **Neon Blue X's**: Glowing blue crosses (#00aaff) with hover effects
- **Neon Red O's**: Bright red circles (#ff2d55) with visual flair
- **Interactive Elements**: Buttons glow and respond to user interaction
- **Smooth Animations**: Hover effects and winning celebrations

### Color Scheme
- **Primary Background**: #0a0a0a (Deep Black)
- **Secondary Background**: #1a1a2e (Dark Blue-Gray)
- **Player X Color**: #00aaff (Neon Blue)
- **Player O Color**: #ff2d55 (Neon Red)
- **Accent Colors**: #00ffff (Cyan), #00ff88 (Green), #ffffff (White)

## How to Run

## Quick Start 🚀

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually included with Python)

### Installation
1. Clone or download the project files
2. Navigate to the project directory:
   ```bash
   cd agent
   ```
3. Run the demo:
   ```bash
   python demo.py
   ```

### Running the Demo
```bash
python demo.py
```

### Running Console Version Directly
```bash
python tic_tac_toe_agent.py
```

### Running GUI Version Directly
```bash
python tic_tac_toe_gui.py
```

### Running Tests
```bash
python test_agent.py
```

## How It Works

### Minimax Algorithm

The AI uses the Minimax algorithm to make optimal decisions:

1. **Game Tree Exploration**: Explores all possible future game states
2. **Evaluation Function**: 
   - +10 for AI win
   - -10 for human win
   - 0 for draw/ongoing
3. **Minimax Strategy**:
   - AI maximizes its score
   - Assumes human plays optimally to minimize AI score
4. **Alpha-Beta Pruning**: Eliminates unnecessary branches for efficiency

### Game Architecture

```
User Input → Game Board → Game Logic → AI Agent → Board Update → Display
     ↑                                                              ↓
     ←←←←←←←←←←←←←← Game Loop ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
```

### AI Decision Process

1. **Perception**: Analyze current board state
2. **Decision**: Use Minimax to evaluate all possible moves
3. **Action**: Execute the move with highest evaluation score
4. **Learning**: N/A (Perfect play doesn't require learning)

## Difficulty Levels

### Easy
- Random move selection
- Beatable by humans

### Medium  
- 70% optimal moves, 30% random
- Challenging but not impossible

### Hard
- Always optimal moves using Minimax
- Unbeatable (best case: draw)

## Game Rules

1. 3x3 grid board
2. Players alternate turns (Human = X, AI = O)
3. First to get 3 in a row (horizontal, vertical, diagonal) wins
4. If board fills without winner, it's a draw

## AI Performance

The AI agent demonstrates several key characteristics:

- **Perfect Play**: Never makes suboptimal moves on Hard difficulty
- **Fast Decisions**: Alpha-beta pruning ensures quick response times
- **Adaptive**: Responds optimally to any human strategy
- **Defensive**: Always blocks human winning moves
- **Offensive**: Takes winning opportunities immediately

## Educational Value

This project demonstrates:

- **Game Theory**: Minimax algorithm implementation
- **AI Concepts**: Search algorithms, evaluation functions
- **Software Engineering**: Clean code, testing, documentation
- **User Interface Design**: Both console and GUI development
- **Algorithm Optimization**: Alpha-beta pruning

## Future Enhancements

Possible improvements:
- **3D Effects**: Add depth and shadows to the neon elements
- **Sound Effects**: Neon-themed audio feedback for moves and wins
- **Particle Effects**: Sparkling animations for special moments
- **Themes**: Multiple color schemes (Matrix green, retro pink, etc.)
- **Machine Learning Version**: Neural network-based AI
- **Online Multiplayer**: Network play with friends
- **Different Board Sizes**: 4x4, 5x5 variations
- **Tournament Mode**: Multiple AIs competing
- **Move Suggestion**: Learning aid for beginners
- **Animation Sequences**: Smooth move transitions and effects

## Technical Notes

### Performance
- Average decision time: < 0.1 seconds
- Maximum game tree depth: 9 (worst case)
- Memory usage: Minimal (recursive with pruning)

### Code Quality
- Comprehensive docstrings
- Type hints for better code clarity
- Error handling for edge cases
- Modular design for easy extension

## License

This project is created for educational purposes. Feel free to use and modify for learning and teaching AI concepts.

## Contributing

This is an educational project. Suggestions for improvements or additional features are welcome!
