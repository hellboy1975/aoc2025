# Advent of Code 2025

My solutions for [Advent of Code 2025](https://adventofcode.com/2025).

## Setup

```bash
# Clone the repo
git clone https://github.com/hellboy1975/aoc2025.git
cd aoc2025

# Optional: create virtual environment for testing
python3 -m venv venv
source venv/bin/activate
pip install pytest
```

## Usage

```bash
# Run a solution
./aoc2025 --day=1 --part=1

# Run with test input
./aoc2025 -d 1 -p 1 --test

# Run tests
pytest days/day01/
pytest  # all tests
```

## Project Structure

```
aoc2025/
├── aoc2025              # CLI entry point
├── runner.py            # Solution runner with timing
├── base.py              # Base Day class
├── pyproject.toml       # Project config
└── days/
    └── dayXX/
        ├── solution.py  # Solution code
        ├── input.txt    # Puzzle input (gitignored)
        ├── test.txt     # Example input
        └── test_dayXX.py  # Unit tests
```

## Writing Solutions

Each day's solution extends the `Day` base class:

```python
from base import Day as BaseDay

class Day(BaseDay):
    def part1(self):
        # self.data - raw input string
        # self.lines - input split by lines
        # self.parse_ints() - parse as integers
        # self.parse_grid() - parse as 2D grid
        # self.parse_sections() - split by blank lines
        return answer

    def part2(self):
        return answer
```
