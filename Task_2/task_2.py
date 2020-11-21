initial_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

count_of_elements = len(initial_list)
summary_list = [initial_list[number_in_list] for number_in_list in range(1, count_of_elements)
                if initial_list[number_in_list] > initial_list[number_in_list - 1]]

print(summary_list)