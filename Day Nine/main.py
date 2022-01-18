from functools import reduce

def problem_one():
    with open('input.txt', 'r') as f:
        lines = [v.replace('\n', '').split() for v in f.readlines()]
        matrix = []
        for ll in lines:
            new_l = []
            for d in ll:
                for dd in str(d):
                    new_l.append(int(dd))
            matrix.append(new_l)

        low_points = []
        low_point_coords = []
        for y, row in enumerate(matrix):
            for x, col in enumerate(row):
                left_adj = col < matrix[y][x-1] if x > 0 else True
                right_adj = col < matrix[y][x+1] if x < len(row) - 1 else True
                top_adj =  col < matrix[y-1][x] if y > 0 else True
                bottom_adj = col < matrix[y+1][x] if y < len(matrix) - 1 else True

                if all([left_adj, right_adj, top_adj, bottom_adj]):
                    low_points.append(col + 1)
                    low_point_coords.append((y, x))

        print(sum(low_points))
        print(low_point_coords)
        return low_point_coords

def problem_two(low_point_coords):

    def find_basin(input, x, y):
        visited = set()
        basin = []

        neighbors = [(x, y)]
        while len(neighbors) > 0:
            x, y = neighbors.pop()
            if (x, y) in visited:
                continue
            else:
                visited.add((x, y))
                if input[x][y] != 9:
                    basin.append((x, y))
                    neighbors = neighbors + get_neighbors(input, x, y)
        
        return basin

    def get_neighbors(input, x, y):
        neighbors = []
        if x > 0:
            neighbors.append((x-1, y))
        if x < len(input) - 1:
            neighbors.append((x+1, y))
        if y > 0:
            neighbors.append((x, y-1))
        if y < len(input[0]) - 1:
            neighbors.append((x, y+1))
        
        print(x, y, neighbors)
        return neighbors

    with open('input.txt', 'r') as f:
        lines = [v.replace('\n', '').split() for v in f.readlines()]
        matrix = []
        for ll in lines:
            new_l = []
            for d in ll:
                for dd in str(d):
                    new_l.append(int(dd))
            matrix.append(new_l)

        basins = []
        for x, y in low_point_coords:
            basins.append(find_basin(matrix, x, y))

        counts = sorted([len(b) for b in basins], reverse=True)
        print(basins)
        print(counts)
        print(reduce(lambda x,y: x * y, counts[0:3]))

coords = problem_one()
problem_two(coords)