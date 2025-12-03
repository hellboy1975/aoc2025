"""Day 01: [Title TBD]"""

from base import Day as BaseDay

class DialCursor:
    def __init__(self, size):
        self.size = size
        self.position = 50
    
    def move(self, steps):
        """Move cursor by steps (positive or negative)"""
        self.position = (self.position + steps) % self.size
        return self.position
    
    def get(self, array):
        """Get current value from array"""
        return array[self.position]
    
class Day(BaseDay):
    """Solution for Day 01."""

    def part1(self):
        """Solve part 1."""
        cursor = DialCursor(100)
        dial = list(range(100))
        zeros = 0

        for line in self.lines:
            direction = line[0]  # 'L' or 'R'
            distance = int(line[1:])  # e.g., 68
            
            if direction == 'L':
                distance *= -1

            cursor.move(distance)
            if cursor.get(dial) == 0:
                zeros += 1

        return zeros

    def part2(self):
        """Solve part 2."""
        # TODO: Implement part 2
        raise NotImplementedError("Part 2 not yet implemented")
