def problem_one():
    try:
        with open('input.txt', 'r') as f:
            lines = f.readlines()
            lines = [l.strip('\n') for l in lines]

            counts = []

            row_size = len(lines[0])
            for i in range(0, row_size):
                counts.append([0,0])

            for l in lines:
                for index, c in enumerate(l):   
                    if int(c) == 0:
                        counts[index][0] += 1
                    elif int(c) == 1:
                        counts[index][1] += 1

            gamma_rate = "0"
            eplison_rate = "0"

            for cnt in counts:
                if cnt[0] > cnt[1]:
                    gamma_rate += "0"
                    eplison_rate += "1"
                else:
                    gamma_rate += "1"
                    eplison_rate += "0"

            gamma_rate_dec = int(gamma_rate, 2)
            eplison_rate_dec = int(eplison_rate, 2)

            print(f'Gama Rate: {gamma_rate} Eplison Rate: {eplison_rate} Multiplied: {gamma_rate_dec * eplison_rate_dec}')
    except Exception as e:
        print(str(e))

def problem_two():

    def return_oxygen_new_lines(index, lines):
        if len(lines) == 1:
            return lines

        included = list()

        zero = sum(1 for line in lines if int(line[index]) == 0) 
        one = sum(1 for line in lines if int(line[index]) == 1)

        oxygen_keep = get_oxygen_keep_list(zero, one)

        for l in lines:
            if int(l[index]) == oxygen_keep:
                included.append(l)
                
        if len(included) == 1:
            return included

        index += 1
        return return_oxygen_new_lines(index, included)

    def return_co2_new_lines(index, lines):
        if len(lines) == 1:
            return lines

        included = list()

        zero = sum(1 for line in lines if int(line[index]) == 0)
        one = sum(1 for line in lines if int(line[index]) == 1)

        co2_keep = get_co2_keep_list(zero, one)

        for l in lines:
            if int(l[index]) == co2_keep:
                included.append(l)
                
        if len(included) == 1:
            return included

        index += 1
        return return_co2_new_lines(index, included)
    

    def get_oxygen_keep_list(zero, one):
        if zero > one:
            return 0
        elif zero < one:
            return 1
        elif zero == one:
            return 1

    def get_co2_keep_list(zero, one):
        if zero > one:
            return 1
        elif zero < one:
            return 0
        elif zero == one:
            return 0

    try:
        with open('input.txt', 'r') as f:
            lines = f.readlines()
            lines = [l.strip('\n') for l in lines]

            oxygen_list = return_oxygen_new_lines(0, list(lines))
            co2_list = return_co2_new_lines(0, list(lines))

            oxygen = int(oxygen_list[0], 2)
            co2 = int(co2_list[0], 2)

            print(f'Oxygen List: {oxygen_list} C02 List {co2_list} Multiplied: {oxygen * co2}')
    except Exception as e:
        print(str(e))

problem_one()
problem_two()