"""Tests for Day 06 solution."""

import pytest
from pathlib import Path

from .solution import Day


@pytest.fixture
def test_input() -> str:
    """Load the test input data."""
    test_file = Path(__file__).parent / "test.txt"
    return test_file.read_text()


@pytest.fixture
def day(test_input) -> Day:
    """Create a Day instance with test input."""
    return Day(test_input)


class TestDay06:
    """Tests for Day 06."""

    def test_part1(self, day):
        """Test part 1 with example input."""
        pass

    def test_part2(self, day):
        """Test part 2 with example input."""
        pass
