def problem_one():
    def get_key(val, dict_vals):
        for key, value in dict_vals.items():
            if val == value:
                return key
    
        return "key doesn't exist"

    with open('input.txt', 'r') as f:
        lines = [int(v) for v in f.readlines()[0].split(',')]

        distances = {}

        for i, j in enumerate(lines):
            distances[i] = []

        for i, pos in enumerate(lines):
            for j in range(0, len(lines)):
                if j == i:
                    continue
                if pos > lines[j]:
                    distances[i].append(pos - lines[j])
                else:
                    distances[i].append(lines[j] - pos)

        sums = {}
        for i in range(9):
            sums[i] = 0

        for key, val in distances.items():
            sums[key] = sum(val)

        print(min(sums.values()))

def problem_two():
    def get_key(val, dict_vals):
        for key, value in dict_vals.items():
            if val == value:
                return key
    
        return "key doesn't exist"
    
    def get_fuel(val):
        total = 0
        for v in range(1, val):
            total += v

        total += val
        return total

    with open('input.txt', 'r') as f:
        lines = [int(v) for v in f.readlines()[0].split(',')]

        distances = {}

        for i, j in enumerate(lines):
            distances[i] = []

        for i, pos in enumerate(lines):
            for j in range(0, len(lines)):
                if j == i:
                    continue
                if pos > lines[j]:
                    distances[i].append(pos - lines[j])
                else:
                    distances[i].append(lines[j] - pos)

        sums = {}

        for key, val in distances.items():
            sums[key] = 0
            for i, v in enumerate(val):
                sums[key] += get_fuel(v)

        print(min(sums.values()))

problem_one()
problem_two()