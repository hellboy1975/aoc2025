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
        """
        Solve part 2 - attempt 2
        This one gets the correct answer.  It's a bit simpler than the other attempt, just rotates 
        one click at a time and matches zeros
        This solution takes 108.715ms compared to the broken "solution" in part2_busted - which completes in 1.787ms
        It's likely adding code to count the >100 numbers could speed this up quite a bit, but I'd rather move onto Day 2
        """
        cursor = DialCursor(100)
        dial = list(range(100))
        zeros = 0
        graph = ""

        for line in self.lines:
            direction = line[0]  # 'L' or 'R'
            distance = int(line[1:])  # e.g., 68

            direction = -1 if direction == "L" else 1
            graph = ""
            for i in range(distance):
                cursor.move(direction * 1)
                if cursor.get(dial) == 0:
                    zeros += 1
                    graph += "🟩"
                else:
                    graph += "🟥"

            print(f"{line}|{cursor.get(dial)} {graph}")
        return zeros


    def part2_busted(self):
        """
        Solve part 2 - attempt 1
        Tried to work it out in an efficient manner initially, building on the approach
        for part 1.  I just couldn't get this to return the right answer.  
        There's a bug somewhere, but wasn't able to spot it.  It returns an answer 7
        less than the right answer.
        """

        cursor = DialCursor(100)
        dial = list(range(100))
        zeros = 0
        previous = 50
        current = 0

        for line in self.lines:
            direction = line[0]  # 'L' or 'R'
            distance = int(line[1:])  # e.g., 68
            
            if direction == 'L':
                distance *= -1

             # Count full rotations first
            full_rotations = abs(distance) // 100
            zeros += full_rotations

            # Move cursor and check for zero crossing in remainder
            cursor.move(distance)
            current = cursor.get(dial)

            # Check if we crossed zero (excluding full rotations)
            remainder = abs(distance) % 100
            if remainder > 0:
                if direction == 'L' and current > previous:
                    zeros += 1
                elif direction == 'R' and current < previous:
                    zeros += 1

            previous = current

        return zeros
