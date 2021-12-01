import requests

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