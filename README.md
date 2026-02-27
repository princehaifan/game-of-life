# Game of Life

## Overview

The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It consists of a grid of cells, each of which can be in one of two states: alive or dead. The state of each cell is updated based on a few simple rules, resulting in potentially complex patterns over time.

## Project Documentation

### Rules of the Game
1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

### Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/princehaifan/game-of-life.git
   ```

2. Navigate into the project directory:
   ```bash
   cd game-of-life
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   **Windows (PowerShell or Command Prompt)**
   ```powershell
   python main.py
   ```
   > **Note:** Do not type the folder path as a command. PowerShell does not execute bare file paths.
   > Always `cd` into the project folder first, then run `python main.py`.
   > If your project folder path contains spaces (e.g. `C:\Users\Admin\Desktop\Python Coursework\game-of-life`), quote the path when changing directory:
   > ```powershell
   > cd "C:\Users\Admin\Desktop\Python Coursework\python coursework\game-of-life"
   > python main.py
   > ```

   **macOS / Linux**
   ```bash
   python3 main.py
   ```

5. Run the tests:
   ```bash
   python -m pytest
   ```

### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgements

- Inspired by the original work and the community around cellular automata.