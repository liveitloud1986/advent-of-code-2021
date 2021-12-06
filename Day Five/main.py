def problem_one():

    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [l.strip('\n').split('->') for l in lines]

        new_line = []

        for line in lines:
            x,y = line[0].strip(' ').split(',')
            x2,y2 = line[1].strip(' ').split(',')

            x = int(x)
            y = int(y)
            x2 = int(x2)
            y2 = int(y2)

            if x == x2:
                if y <= y2:
                    while y <= y2:
                        new_line.append((int(x), int(y)))
                        y += 1
                elif y >= y2:
                    while y >= y2:
                        new_line.append((int(x), int(y)))
                        y -= 1
            elif y == y2:
                if x <= x2:
                    while x <= x2:
                        new_line.append((int(x), int(y)))
                        x += 1
                elif x >= x2:
                    while x >= x2:
                        new_line.append((int(x), int(y)))
                        x -= 1
            elif x == x2 and y == y2:
                new_line.append((x, y))
            else: 
                continue

        intersections = {}
        for line in new_line:
            if line not in intersections:
                intersections[line] = 0
            intersections[line] += 1

        print(intersections)
        print(sum(1 for l,v in intersections.items() if v > 1))

def problem_two():

    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [l.strip('\n').split('->') for l in lines]
        
        new_line = []

        for line in lines:
            x,y = line[0].strip(' ').split(',')
            x2,y2 = line[1].strip(' ').split(',')

            x = int(x)
            y = int(y)
            x2 = int(x2)
            y2 = int(y2)

            if x == x2:
                if y <= y2:
                    while y <= y2:
                        new_line.append((int(x), int(y)))
                        y += 1
                elif y >= y2:
                    while y >= y2:
                        new_line.append((int(x), int(y)))
                        y -= 1
            elif y == y2:
                if x <= x2:
                    while x <= x2:
                        new_line.append((int(x), int(y)))
                        x += 1
                elif x >= x2:
                    while x >= x2:
                        new_line.append((int(x), int(y)))
                        x -= 1
            #elif x == x2 and y == y2:
                #new_line.append((x, y))
            else: 
                x_vals = []
                y_vals = []
                if x <= x2:
                    while x <= x2:
                        x_vals.append(x)
                        x += 1
                elif x >= x2:
                    while x >= x2:
                        x_vals.append(x)
                        x -= 1
                if y <= y2:
                    while y <= y2:
                        y_vals.append(y)
                        y += 1
                elif y >= y2:
                    while y >= y2:
                        y_vals.append(y)
                        y -= 1
                for i,x in enumerate(x_vals):
                    new_line.append((x, y_vals[i]))

        intersections = {}
        for line in new_line:
            if line not in intersections:
                intersections[line] = 0
            intersections[line] += 1

        print(intersections)
        print(sum(1 for l,v in intersections.items() if v > 1))
                
problem_one()    
problem_two()