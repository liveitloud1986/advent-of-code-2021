def problem_one():
    try:
        with open('data.txt', 'r') as f:
            lines = f.readlines()

            num_increases = 0
            for index, line in enumerate(lines):
                if index > 0:
                    if int(lines[index - 1]) < int(line):
                        num_increases += 1
            
            print(num_increases)
    except Exception as e:
        print(e.reason)

def problem_two():

    def get_three(lines):
        for i in range(0, len(lines), 1):
            yield lines[i:i+3]

    try:
        with open('data.txt', 'r') as f:
            lines = f.readlines()
            lines = [l.strip('\n') for l in lines]

            num_increases = 0
            list_of_threes = []
            for three_lines in get_three(lines):
                list_of_threes.append(three_lines)

            for index, three_lines in enumerate(list_of_threes):
                if index > 0:
                    if int(sum(int(l) for l in list_of_threes[index - 1])) < sum(int(l) for l in three_lines):
                        num_increases += 1

            print(num_increases)
    except Exception as e:
        print(e)

problem_one()
problem_two()