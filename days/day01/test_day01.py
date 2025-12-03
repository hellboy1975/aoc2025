"""Tests for Day 01 solution."""

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


class TestDay01:
    """Tests for Day 01."""

    def test_part1(self, day):
        """Test part 1 with example input."""
        # TODO: Update expected value once you know it
        # expected = 42
        # assert day.part1() == expected
        pass

    def test_part2(self, day):
        """Test part 2 with example input."""
        # TODO: Update expected value once you know it
        # expected = 42
        # assert day.part2() == expected
        pass

    # Add tests for helper methods below:
    # def test_helper_method(self, day):
    #     """Test a specific helper method."""
    #     assert day.some_helper(input) == expected_output
