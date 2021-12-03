
def problem_one():
    try:
        with open('input.txt', 'r') as f:
            lines = f.readlines()
            lines = [l.strip('\n') for l in lines]

            depth = 0
            horizontal = 0

            for command in lines:
                cmd, amt = command.split(' ')
                if cmd == "forward":
                    horizontal += int(amt)
                elif cmd == "up":
                    depth -= int(amt)
                elif cmd == "down":
                    depth += int(amt)

            print(f'Depth: {depth}', f'Horizontal: {horizontal}', f'Multiplied: {depth * horizontal}')
    except Exception as e:
        print(e)

def problem_two():
    try:
        with open('input.txt', 'r') as f:
            lines = f.readlines()
            lines = [l.strip('\n') for l in lines]

            depth = 0
            horizontal = 0
            aim = 0

            for command in lines:
                cmd, amt = command.split(' ')
                if cmd == "forward":
                    horizontal += int(amt)
                    depth += int(amt) * aim
                elif cmd == "up":
                    aim -= int(amt)
                elif cmd == "down":
                    aim += int(amt)

            print(f'Depth: {depth}', f'Horizontal: {horizontal}', f'Aim: {aim}', f'Multiplied: {depth * horizontal}')
    except Exception as e:
        print(e)

problem_one()
problem_two()