# 🐍 Snake

A Python implementation of the classic Snake arcade game, built using the `turtle` graphics library and the `freegames` package. By Gael Leyva, and Emma Sofía García.

## Overview

The player controls a snake that moves around a bounded screen eating food. Each time the snake eats food, it grows longer. The game ends if the snake collides with itself. The snake and food are randomly assigned colors from a predefined palette each round.

## Requirements

- Python 3.x
- [`freegames`](https://pypi.org/project/freegames/) library

Use a virtual environment to create an isolated workspace for a project’s dependencies and Python version.
This prevents package conflicts between projects and keeps your system installation clean.

```bash
sudo apt -get install python3-all-venv
python3 -m venv ./games/
source ./games/bin/activate
```

Install the dependency with:

```bash
python3 -m pip install freegames
```

## How to Run

```bash
python snake.py
```

## Controls

| Input | Action |
|---|---|
| `Arrow keys` | Change direction |
| `Mouse click` | Change direction toward click |

## Changes from the Original

### 1. Wrap-around edges
Instead of dying when hitting a wall, the snake now reappears on the opposite side of the screen. For example, crossing the left wall brings the snake out from the right, and crossing the top brings it out from the bottom.

### 2. Moving food
Food is no longer stationary. Every 200ms it takes a random step in one of four directions. It is constrained to stay within the playable area and will simply skip a move if the chosen direction would take it out of bounds.

### 3. Mouse click controls
In addition to the arrow keys, the player can click anywhere on the screen to change the snake's direction. The snake moves along whichever axis (horizontal or vertical) has the greater distance to the clicked point.

### 4. Random colors
The snake is assigned a random color at the start of each game. Food is also assigned a random color, guaranteed to always differ from the snake's color, and refreshes to a new color each time it is eaten.
