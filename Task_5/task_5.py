from functools import reduce

initial_list = [item for item in range(100, 1002, 2)]

summary = reduce(lambda x, y: x * y, initial_list)

print(f'summary is : {summary}')