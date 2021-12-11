# https: // adventofcode.com/2021/day/2

# Now, you need to figure out how to pilot this thing.

# It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.
# Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.

# The submarine seems to already have a planned course(your puzzle input). You should probably figure out where it's going. For example:

# forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2
# Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

# forward 5 adds 5 to your horizontal position, a total of 5.
# down 5 adds 5 to your depth, resulting in a value of 5.
# forward 8 adds 8 to your horizontal position, a total of 13.
# up 3 decreases your depth by 3, resulting in a value of 2.
# down 8 adds 8 to your depth, resulting in a value of 10.
# forward 2 adds 2 to your horizontal position, a total of 15.
# After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

# Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?

def dive(instructions):
    h = 0
    d = 0

    for instruction in instructions.split("\n"):
        direction, steps = instruction.split()
        if direction == "up":
            d -= int(steps)
        elif direction == "down":
            d += int(steps)
        else:
            h += int(steps)

    return h * d


example = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

print(dive(example))

input = """forward 4
down 9
forward 6
down 5
up 2
forward 5
forward 7
up 5
down 9
up 6
down 6
down 1
down 1
up 2
down 3
up 3
forward 8
forward 7
down 6
down 7
forward 6
forward 9
forward 7
up 9
down 4
down 6
down 5
down 9
forward 8
down 9
forward 9
forward 4
forward 4
up 3
up 8
down 9
down 8
down 4
forward 5
forward 4
up 6
forward 6
up 3
up 8
up 3
up 4
down 3
down 5
down 5
up 1
forward 9
down 4
forward 6
down 6
up 2
up 9
forward 1
forward 2
forward 7
down 6
up 6
forward 1
forward 7
down 7
forward 9
forward 4
forward 6
down 5
up 9
down 1
up 5
up 5
up 9
down 5
forward 7
down 1
up 9
down 7
forward 2
down 4
down 4
forward 8
forward 8
down 6
down 3
up 7
down 3
forward 9
down 7
forward 2
down 1
forward 5
up 9
down 2
up 2
down 3
up 7
forward 9
forward 7
down 4
down 5
up 3
down 3
down 5
forward 9
down 3
forward 9
down 3
up 9
down 5
forward 4
down 4
up 8
forward 7
up 1
down 2
forward 4
down 7
down 9
down 4
down 4
forward 6
down 7
down 2
down 1
forward 1
down 2
forward 1
down 7
forward 5
up 3
forward 6
up 9
down 3
down 3
down 9
forward 4
down 4
forward 9
forward 6
down 7
up 9
up 6
forward 4
down 5
forward 2
down 7
down 7
forward 4
forward 5
down 8
down 5
up 4
forward 7
up 8
down 8
forward 4
forward 5
down 6
down 1
down 1
down 9
forward 4
up 1
down 8
up 7
down 1
up 2
forward 4
down 7
down 7
down 2
forward 7
down 2
up 1
up 4
down 6
forward 5
forward 2
up 1
forward 2
forward 9
up 9
up 7
forward 9
down 8
up 5
down 6
down 6
up 8
down 1
forward 6
down 5
forward 2
down 9
down 9
up 4
forward 4
forward 2
forward 7
forward 3
down 1
forward 8
up 9
down 7
forward 9
forward 1
forward 5
up 6
down 6
forward 6
up 3
forward 9
down 3
forward 2
down 7
down 3
up 9
down 2
down 3
forward 5
down 9
forward 8
down 2
forward 1
down 9
down 7
forward 2
forward 6
forward 4
forward 5
down 5
down 1
forward 5
up 4
down 4
up 8
down 4
up 4
down 1
down 2
down 9
down 2
up 4
down 1
forward 2
forward 1
forward 9
down 5
up 4
up 1
forward 8
forward 6
forward 9
up 9
forward 4
forward 4
down 1
forward 6
forward 7
forward 3
up 5
up 7
down 1
forward 4
down 3
down 5
up 7
down 4
up 9
down 3
down 5
forward 7
forward 8
up 5
up 1
forward 3
up 8
forward 3
down 2
forward 1
forward 9
forward 1
down 2
forward 7
down 5
forward 6
down 9
up 9
forward 5
forward 7
forward 6
down 2
up 2
forward 3
forward 4
forward 3
down 5
forward 1
forward 2
forward 6
down 4
forward 2
forward 6
up 8
forward 2
up 4
forward 7
down 2
forward 1
forward 7
down 6
forward 4
down 3
down 2
down 2
forward 4
down 8
forward 6
forward 6
down 2
up 3
up 1
forward 1
down 5
down 2
forward 4
forward 7
forward 3
down 3
forward 9
down 1
down 7
forward 6
forward 1
up 6
forward 7
forward 1
down 5
down 4
forward 6
up 1
down 1
up 9
down 2
down 2
forward 3
up 4
down 5
down 5
down 3
down 6
up 8
forward 2
forward 2
down 6
down 1
up 4
up 1
down 5
up 4
up 2
forward 4
forward 6
forward 3
down 7
forward 8
up 5
forward 5
down 1
forward 2
forward 6
down 8
up 6
down 1
down 7
forward 4
forward 2
up 1
down 6
forward 3
forward 1
forward 5
forward 9
forward 9
down 4
forward 2
down 1
forward 1
forward 7
forward 5
down 9
down 8
down 1
down 6
down 1
up 7
down 3
forward 3
up 6
up 4
down 7
down 7
forward 6
up 7
down 7
forward 9
down 9
down 3
forward 6
forward 9
forward 1
down 4
forward 5
down 4
down 2
down 3
up 3
forward 9
forward 7
forward 5
down 5
forward 7
up 4
down 1
forward 3
down 3
forward 4
down 9
forward 2
down 5
down 1
forward 8
down 3
forward 7
up 1
down 3
forward 2
up 8
down 2
forward 4
forward 4
forward 4
down 5
up 6
down 3
forward 5
down 4
up 5
forward 1
forward 6
up 1
down 3
forward 2
forward 9
down 7
down 4
forward 5
up 3
up 6
up 1
forward 4
forward 1
forward 1
down 7
up 4
down 3
down 8
down 3
forward 8
forward 3
down 6
down 9
forward 3
forward 9
forward 7
down 8
down 6
down 4
forward 2
up 4
forward 8
down 1
forward 9
forward 1
down 9
forward 2
down 7
down 2
up 7
down 1
up 8
forward 8
down 7
forward 1
down 1
forward 3
forward 1
up 2
down 7
down 5
forward 5
down 8
forward 4
down 1
up 2
up 8
down 8
down 1
down 5
up 3
forward 3
forward 5
down 2
up 4
down 2
forward 7
forward 9
up 9
up 7
forward 1
up 4
forward 3
up 5
forward 9
forward 9
forward 6
forward 2
down 7
forward 8
forward 4
forward 7
down 8
down 5
down 6
forward 6
down 4
down 1
down 9
down 1
forward 3
forward 5
down 6
down 7
down 9
down 8
down 4
up 5
forward 7
down 9
forward 6
down 7
forward 5
down 5
forward 1
down 5
down 3
up 9
up 3
forward 2
up 9
forward 6
down 1
down 5
down 9
down 4
up 6
forward 9
down 4
down 9
down 5
down 8
down 5
down 4
up 5
down 8
up 8
forward 5
down 9
forward 2
up 2
down 6
forward 2
forward 4
forward 6
down 6
down 1
forward 8
down 5
down 5
forward 2
down 7
down 5
down 6
down 9
forward 4
up 9
down 3
down 7
forward 3
down 5
up 1
forward 5
up 2
down 2
forward 2
up 3
up 6
forward 2
forward 7
down 8
forward 8
forward 7
forward 6
down 5
down 6
down 6
down 9
up 5
down 3
up 1
up 9
up 5
down 4
down 4
down 8
forward 8
up 5
down 9
forward 1
up 1
forward 2
down 9
forward 5
up 9
forward 7
down 7
down 5
up 1
up 2
down 8
down 7
up 4
forward 9
down 4
up 8
down 5
down 1
forward 9
down 6
up 8
down 6
forward 7
up 6
up 5
forward 2
up 7
forward 7
forward 5
down 1
forward 9
down 8
forward 9
down 3
down 3
forward 9
up 1
down 2
forward 9
down 7
forward 4
forward 3
forward 4
down 5
forward 9
forward 9
down 5
forward 4
down 5
down 2
down 6
forward 5
forward 8
forward 6
up 9
down 9
forward 7
down 6
down 7
down 4
forward 1
forward 3
forward 6
forward 4
forward 3
forward 4
down 1
forward 2
forward 3
forward 9
up 8
forward 6
down 1
up 5
down 1
down 4
down 7
down 5
down 9
down 2
down 9
forward 2
down 2
up 5
forward 2
forward 3
forward 5
up 8
up 1
down 9
forward 2
down 4
down 9
down 6
down 5
down 8
forward 3
forward 8
forward 7
up 3
up 5
down 9
down 5
up 6
forward 4
forward 4
forward 4
down 9
down 2
down 7
down 1
down 2
down 4
forward 7
down 9
forward 4
forward 5
up 5
forward 4
forward 9
forward 1
forward 5
down 3
forward 1
forward 5
up 9
down 7
forward 7
forward 6
down 2
down 3
forward 9
down 1
forward 4
forward 9
up 7
forward 7
down 5
forward 9
forward 2
up 3
down 3
down 7
down 5
up 7
up 9
up 7
forward 3
forward 3
forward 8
up 9
forward 8
forward 9
forward 4
down 2
forward 7
down 6
up 3
up 9
forward 8
forward 2
down 9
down 7
forward 1
up 4
up 7
forward 2
up 4
forward 4
up 1
forward 3
down 7
forward 5
down 4
forward 2
forward 7
up 4
down 1
down 6
forward 1
forward 9
up 6
forward 7
forward 7
down 8
forward 7
down 8
down 9
up 3
forward 3
forward 3
down 8
up 2
down 2
down 4
up 3
down 3
forward 7
down 4
up 8
down 9
down 9
up 7
down 1
forward 2
up 1
down 3
up 9
down 6
up 2
forward 6
up 8
up 1
down 6
down 1
up 6
up 4
up 2
forward 6
down 6
down 1
forward 7
up 9
up 1
forward 4
forward 5
up 6
forward 9
down 1
down 9
down 3
down 7
forward 7
down 1
down 4
forward 6
down 5
up 4
forward 9
up 5
down 1
down 2
down 2
up 4
forward 1
forward 3
down 7
forward 4
down 4
down 8
down 5
forward 3
up 4
forward 5
down 2
down 4
down 4
down 1
forward 2
forward 1
forward 8
forward 4
up 4
down 9
up 6
forward 9
up 5
down 5
forward 3
up 1
forward 7
down 4
forward 7
down 9
up 8
down 5
forward 1
down 5
down 8
forward 3
up 6
forward 3
up 7
forward 6
forward 9
up 1
down 3
down 9
up 4
up 6
forward 5
down 6
down 3
down 4
up 1
forward 5
down 5
down 2
forward 6
down 8
down 3
up 8
forward 5
forward 6
down 6
down 6
down 6
forward 7
up 4
forward 7
up 4
down 2
forward 4
forward 2
down 6
up 1
down 1
down 4
up 8
down 6
forward 3
forward 6
down 6
forward 5
down 4
up 2
up 3
down 3
up 1
forward 2
up 1
forward 4
up 5
up 2
down 7
forward 3
up 2
forward 5
down 1
down 3
down 2
forward 5
down 1
up 5
forward 4
down 7
up 8
up 3
down 7
down 7
forward 9
forward 1
up 6
down 4
down 7
forward 1
down 4
forward 9
up 1
forward 3
down 1
up 3
down 6
down 8
down 6
forward 6
forward 6
up 2
down 8
forward 5"""

print(dive(input))
