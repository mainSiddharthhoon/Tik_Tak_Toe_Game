# Tic Tac Toe – Python CLI Game

## 🎮 Project Overview

This project is a simple **command-line Tic Tac Toe game written in Python**.
It was developed as a learning project to practice **game logic, matrix-based board handling, and player turn management**.

The game runs completely inside the terminal and allows two players to play Tic Tac Toe by entering row and column coordinates.

---

## 🎯 Goal of the Project

The purpose of this project was to understand how small games can be built using basic programming constructs such as:

* Loops
* Conditional logic
* Functions
* Matrix data structures
* Input handling

The project also explores how win conditions can be detected programmatically using rows, columns, and diagonals.

---

## 🧠 Core Concepts Used

This project demonstrates the following programming concepts:

* **2D List (Matrix) representation of the board**
* **Turn-based game loop**
* **Input validation**
* **Win condition detection**
* **Row, column, and diagonal checking**
* **Game termination using `sys.exit()`**

---

## 🏗️ Game Architecture

### Board Representation

The game board is implemented as a **3×3 matrix**:

```
matrix_field = [[None for _ in range(3)] for _ in range(3)]
```

Each cell can contain:

* `None` → empty position
* `1` → Player 1 (X)
* `0` → Player 2 (O)

---

### Player Functions

The game uses two main functions:

**`x()`**
Handles moves for **Player 1 (X)**.

**`o()`**
Handles moves for **Player 2 (O)**.

Each function:

1. Validates coordinates
2. Places the symbol on the board
3. Checks for win conditions
4. Prints the updated board

---

### Win Condition Logic

The game checks three types of winning patterns:

1️⃣ **Row win**

```
X X X
```

2️⃣ **Column win**

```
X
X
X
```

3️⃣ **Diagonal win**

```
X   X
  X
X   X
```

If any player satisfies one of these conditions, the game immediately ends.

---

## ▶️ How to Run the Game

### Requirements

* Python 3 installed

### Run the game

```
python tic_tac_toe.py
```

Follow the prompts and enter coordinates:

```
Rows: 1-3
Columns: 1-3
```

Example input:

```
Player 1 row: 1
Player 1 col: 2
```

---

## 🎮 Gameplay Flow

1. Player 1 (X) starts the game.
2. Player 2 (O) takes the next turn.
3. Players alternate turns.
4. The board updates after every move.
5. The game ends when:

   * A player wins
   * All 9 moves are filled (draw)

---

## 🧪 Example Board

```
 X  O  .
 .  X  .
 O  .  X
```

`.` indicates an empty cell.

---

## 📚 Learning Outcomes

Through this project, the following concepts were practiced:

* Designing simple game logic
* Working with 2D lists in Python
* Validating user input
* Detecting game states
* Structuring CLI applications

---

## 🚀 Possible Future Improvements

Possible upgrades for this project include:

* Add **single-player mode with AI**
* Add **graphical interface (Tkinter or Pygame)**
* Improve board rendering
* Refactor repeated code into reusable functions
* Add unit tests for win detection

---

## 🏁 Conclusion

This project is a small but effective demonstration of how basic programming concepts can be used to build an interactive game. It serves as a good starting point for learning game logic and CLI-based application design in Python.
## 🛠️ Development Status

This project currently provides a **fully functional CLI (Command Line Interface) version** of the Tic Tac Toe game.

A **graphical frontend version is currently under development** and will be introduced in a separate **`dev` branch** in future updates.

Planned improvements include:

* Graphical user interface (GUI)
* Improved game board visualization
* Better input handling and validation
* Possible single-player mode

The CLI version will remain as the **core logic implementation**, while the GUI version will focus on improving the user experience.
