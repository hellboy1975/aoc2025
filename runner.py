"""Runner module for loading and executing day solutions."""

import importlib
import time
from pathlib import Path


def load_input(day: int, test: bool = False) -> str:
    """Load input file for a given day.

    Args:
        day: Day number (1-25)
        test: If True, load test.txt instead of input.txt

    Returns:
        Contents of the input file

    Raises:
        FileNotFoundError: If the input file doesn't exist
    """
    day_dir = Path(__file__).parent / "days" / f"day{day:02d}"
    filename = "test.txt" if test else "input.txt"
    input_path = day_dir / filename

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    return input_path.read_text()


def load_day_class(day: int):
    """Dynamically load the Day class for a given day.

    Args:
        day: Day number (1-25)

    Returns:
        The Day class for the specified day

    Raises:
        ModuleNotFoundError: If the day module doesn't exist
        AttributeError: If the module doesn't have a Day class
    """
    module_name = f"days.day{day:02d}.solution"
    module = importlib.import_module(module_name)

    if not hasattr(module, "Day"):
        # Try looking for DayXX class name as fallback
        class_name = f"Day{day:02d}"
        if hasattr(module, class_name):
            return getattr(module, class_name)
        raise AttributeError(f"Module {module_name} has no 'Day' class")

    return module.Day


def run_day(day: int, part: int, test: bool = False) -> bool:
    """Run a specific day and part.

    Args:
        day: Day number (1-25)
        part: Part number (1 or 2)
        test: If True, use test input

    Returns:
        True if successful, False otherwise
    """
    input_type = "test" if test else "real"
    print(f"Day {day:02d} Part {part} ({input_type} input)")
    print("-" * 40)

    try:
        input_data = load_input(day, test)
        day_class = load_day_class(day)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return False
    except ModuleNotFoundError:
        print(f"Error: Day {day:02d} solution not found")
        print(f"Expected: days/day{day:02d}/solution.py")
        return False
    except AttributeError as e:
        print(f"Error: {e}")
        return False

    solution = day_class(input_data)

    method = solution.part1 if part == 1 else solution.part2

    start_time = time.perf_counter()
    try:
        result = method()
    except NotImplementedError:
        print(f"Part {part} not yet implemented")
        return False
    except Exception as e:
        print(f"Error running part {part}: {e}")
        raise
    end_time = time.perf_counter()

    elapsed_ms = (end_time - start_time) * 1000

    print(f"Result: {result}")
    print(f"Time: {elapsed_ms:.3f}ms")

    return True
