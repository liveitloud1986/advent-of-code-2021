def problem_one():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [int(l) for l in lines[0].strip('\n').split(',')]

        for _ in range(80):
            add_one = 0
            for i, line in enumerate(lines):
                if lines[i] == 0:
                    add_one += 1
                    lines[i] = 6
                else:
                    lines[i] -= 1

            for add in range(add_one):
                lines.append(8)

            add_one = 0

        print(len(lines))

def problem_two():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [int(l) for l in lines[0].strip('\n').split(',')]
        fishes = {}
        for i in range(9):
            fishes[i] = 0
        
        for i in lines:
            fishes[i] += 1

        new_fishes = {}
        for _ in range(256):
            for i in range(9):
                new_fishes[i] = 0

        new_fishes[8] += fishes[0]
        new_fishes[6] += fishes[0]

        for i in range(8):
            new_fishes[i] += fishes[i+1]
        
        fishes = dict(new_fishes)

        print(sum(fishes.values()))

problem_one()
problem_two() 