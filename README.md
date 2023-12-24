# Pathfinding Project README

## Overview

Welcome to the Pathfinding Project! This Python project is designed to implement various pathfinding algorithms to find the shortest path between two points on a grid.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Algorithms](#algorithms)

## Introduction

Pathfinding is a fundamental problem in computer science, involving finding the most efficient route between two points.

## Features

- **Grid Visualization:** View the pathfinding algorithms in action on a visual grid.
- **Multiple Algorithms:** Implement and compare popular pathfinding and traversing algorithms like Dijkstra's, A\*, Bredth-First Search, Depth-First Search.

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/boatnoah/pathfinding-project.git
   ```

2. **Install Dependencies:**
   ```
   pip install pygame
   pip install pygbag
   ```

> For information on deploying Pygame on the web visit these sites:
>
> - https://dev.to/sandy_codes_py/deploy-pygames-to-github-pages-with-webassembly-56po (github method)
> - https://medium.com/@eri.zhang21/running-a-python-game-on-the-web-aa8b13037e15 (hosting service method)

## Usage

1. **Run the Application:**

   ```bash
   python main.py
   ```

2. **Interact with the GUI:**

   - Left Mouse Button: Set start and target positions, draw obstacles.
   - Right Mouse Button: Erase walls.
   - c: Clear the grid.
   - Escape: Return to the algorithm selection menu.
   - Enter: Run the selected algorithm.

## Algorithms

The project currently supports the following pathfinding algorithms:

- Dijkstra's Algorithm
- A\* Algorithm
- Breadth-First Search
- Depth-First Search
