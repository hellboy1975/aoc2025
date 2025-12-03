"""Base class for Advent of Code day solutions."""

from abc import ABC, abstractmethod


class Day(ABC):
    """Base class that all day solutions should inherit from.

    Attributes:
        data: Raw input string (with trailing whitespace stripped)
        lines: Input split into lines (empty lines preserved)
    """

    def __init__(self, input_data: str):
        """Initialize with puzzle input.

        Args:
            input_data: Raw puzzle input string
        """
        self.data = input_data.rstrip()
        self.lines = self.data.split("\n")

    @abstractmethod
    def part1(self):
        """Solve part 1 of the puzzle.

        Returns:
            The solution to part 1
        """
        pass

    @abstractmethod
    def part2(self):
        """Solve part 2 of the puzzle.

        Returns:
            The solution to part 2
        """
        pass

    def parse_ints(self) -> list[int]:
        """Parse input as a list of integers (one per line)."""
        return [int(line) for line in self.lines if line]

    def parse_grid(self) -> list[list[str]]:
        """Parse input as a 2D grid of characters."""
        return [list(line) for line in self.lines]

    def parse_sections(self, separator: str = "\n\n") -> list[str]:
        """Split input into sections by blank lines or custom separator."""
        return self.data.split(separator)
