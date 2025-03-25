# DSAprep Project

## Overview
The project is designed to help users visualize and solve problems related to data structures and algorithms (DSA). It includes a tool for simulating a coin chessboard game and generates a hierarchical directed graph with the first winning path found highlighted. With simple adjustments it can be used to traverse any binary tree or otherwise using DFS. It includes a js and python implementation.

## Exercise - A Chessboard Game
Two players are playing a game on a 15x15 board. The game starts with a coin placed in (x,y) coordinated. Players take alternating turns moving thr coin, the first player who is unable to make a move loses the game.
The problem is fully defined on [hackerrank](https://www.hackerrank.com/challenges/a-chessboard-game-1/problem?isFullScreen=true)

Given a set of initial coordinates of the player's coin and assuming perfect play, determine which player will the game.

Valid moves are considered the following:
    [-2, -1], 
    [-1, -2],
    [-2, +1], 
    [+1, -2], 

![Chessboard Game Example](images/valid_moves.png)

---

## Setup Instructions

### Prerequisites
Ensure you have the following installed on your system:
- [pyvis](https://pyvis.readthedocs.io/en/latest/install.html) 

### Run the project
Run `AChessboardGame.py` and call the `chessboardGame(...)` function
The function will create an html file with the directed graph.

### Example Output
```python
# winnig player
First 
# first found winnig path
Winning Path: [(5, 3), (6, 1), (4, 2), (2, 1)]
```
![Visualised search](images/hierarchy_graph.png)
*Player 1 moves are denoted by red edges and nodes*