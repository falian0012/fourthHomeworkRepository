initial_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result_list = [item for item in initial_list if initial_list.count(item) == 1]

print(result_list)