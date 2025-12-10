"""Day 02: [Title TBD]"""

from base import Day as BaseDay

def int_len(num):
    return len(str(abs(num)))  

# credit to this stack overflow post:  
# https://stackoverflow.com/questions/29481088/how-can-i-tell-if-a-string-repeats-itself-in-python/29482936#29482936
def repeating_strings(s):
        i = (s+s).find(s, 1, -1)
        return None if i == -1 else s[:i]

class Day(BaseDay):
    """Solution for Day 02."""

    def is_odd_len(self, number):
        """check if the number passed has a length that is odd"""
        return len(str(number)) % 2 != 0

    def split_number(self, number):
        num_str = str(number)
        mid = len(num_str) // 2
        
        first_half = int(num_str[:mid])
        second_half = int(num_str[mid:])
        
        return first_half, second_half

    def check_invalid(self, id):
        """ checks an ID to see if it's invalid"""

        # if the length of the number is odd then it can be two patterns
        if len(str(id)) % 2:
            return 0
        
        x, y = self.split_number(id)

        return x == y

    def part1(self):
        """Solve part 1."""
        total = 0

        for item in self.data.split(','):
            min, max = map(int, item.split('-'))
            print(f"{min} | {max}")

            # if it's too odd numbers of the same length then they are valid, and can be skipped
            if int_len(min) == int_len(max) and self.is_odd_len(min) and self.is_odd_len(max):
                continue

            for i in range(min, max + 1):
                if self.check_invalid(i):
                    total += i

        return total

    def part2(self):
        """Solve part 2."""
        total = 0

        for item in self.data.split(','):
            

            min, max = map(int, item.split('-'))
            # print(f"{min} | {max}")

            for i in range(min, max + 1):

                foo = repeating_strings(str(i))
                if foo: 
                    print(f"{i}: {foo} ")
                    total += i

        return total
